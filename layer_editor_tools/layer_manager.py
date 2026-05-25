import json

from maya import cmds
from maya.api import OpenMaya as om

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.layer_widget import LayerWidget


# Module-level session cache — persists across tool open/close within the same Maya session
_session_cache = {}  # uuid -> export_path


class LayerManager:

    FILE_INFO_KEY = "VFSLayers"

    def __init__(self):
        self.layers = []
        self.selected_entry = None
        self._attr_callbacks = {}  # uuid -> (attr_cb_id, name_cb_id)
        self._creating = False

    # --------------------------------
    # Create
    # --------------------------------

    def create_layer(self, empty=True, name="Layer"):
        self._creating = True
        try:
            maya_layer = cmds.createDisplayLayer(e=empty, n=name)

            uuid = cmds.ls(maya_layer, uuid=True)[0]
            data = VFSLayerData(uuid=uuid, maya_layer_name=maya_layer)

            widget = LayerWidget(data)
            widget.selected.connect(self.on_layer_selected)
            widget.path_changed.connect(self.update_session_cache)

            entry = {"data": data, "widget": widget}
            self.layers.insert(0, entry)

            self._attach_node_callback(entry)
        finally:
            self._creating = False

        return widget

    # --------------------------------
    # Remove
    # --------------------------------

    def remove_selected(self):
        if not self.selected_entry:
            return
        self.remove_layer(self.selected_entry["widget"])
        self.selected_entry = None

    def remove_layer(self, widget):
        entry = next(
            (x for x in self.layers if x["widget"] == widget),
            None
        )

        if not entry:
            return

        uuid = entry["data"].uuid
        layer_name = entry["data"].maya_layer_name

        # Remove node callbacks
        self._remove_node_callback(uuid)

        if cmds.objExists(layer_name):
            cmds.delete(layer_name)

        widget.setParent(None)
        widget.deleteLater()

        # Remove from session cache
        if uuid in _session_cache:
            del _session_cache[uuid]

        self.layers.remove(entry)

    # --------------------------------
    # Selection
    # --------------------------------

    def on_layer_selected(self, widget):
        # Deselect previous
        if self.selected_entry:
            self.selected_entry["widget"].set_selected(False)

        self.selected_entry = next(
            (x for x in self.layers if x["widget"] == widget),
            None
        )

        # Select new
        if self.selected_entry:
            self.selected_entry["widget"].set_selected(True)

    # --------------------------------
    # Reorder
    # --------------------------------

    def move_selected_up(self):
        if not self.selected_entry:
            return
        self.move_layer(self.selected_entry["widget"], "up")

    def move_selected_down(self):
        if not self.selected_entry:
            return
        self.move_layer(self.selected_entry["widget"], "down")

    def move_layer(self, widget, direction):
        index = next(
            (i for i, x in enumerate(self.layers) if x["widget"] == widget),
            None
        )

        if index is None:
            return
        if direction == "up" and index == 0:
            return
        if direction == "down" and index == len(self.layers) - 1:
            return

        new_index = index - 1 if direction == "up" else index + 1

        # Swap displayOrder values in Maya between the two affected layers
        layer_a = self.layers[index]["data"].maya_layer_name
        layer_b = self.layers[new_index]["data"].maya_layer_name

        order_a = cmds.getAttr(f"{layer_a}.displayOrder")
        order_b = cmds.getAttr(f"{layer_b}.displayOrder")

        # Find the truly adjacent layer in Maya's order if not contiguous
        if abs(order_a - order_b) != 1:
            offset = 1 if direction == "up" else -1
            target_order = order_a + offset
            for entry in self.layers:
                name = entry["data"].maya_layer_name
                if cmds.getAttr(f"{name}.displayOrder") == target_order:
                    layer_b = name
                    order_b = target_order
                    break

        cmds.setAttr(f"{layer_a}.displayOrder", order_b)
        cmds.setAttr(f"{layer_b}.displayOrder", order_a)

        # Reorder in self.layers to match
        self.layers.insert(new_index, self.layers.pop(index))

        # Refresh Maya's layer editor
        from maya import mel
        mel.eval("updateLayerEditor();")

    # --------------------------------
    # Node Callbacks
    # --------------------------------

    def _attach_node_callback(self, entry):
        data = entry["data"]

        try:
            sel = om.MSelectionList()
            sel.add(data.maya_layer_name)
            node = sel.getDependNode(0)

            attr_cb_id = om.MNodeMessage.addAttributeChangedCallback(
                node,
                lambda msg, plug, other, cd: self._on_node_attr_changed(plug, data, entry["widget"])
            )

            name_cb_id = om.MNodeMessage.addNameChangedCallback(
                node,
                lambda node, old_name, cd: self._on_node_renamed(node, old_name, data, entry["widget"])
            )

            self._attr_callbacks[data.uuid] = (attr_cb_id, name_cb_id)
        except Exception as e:
            print(f"Failed to attach callback to {data.maya_layer_name}: {e}")

    def _remove_node_callback(self, uuid):
        if uuid in self._attr_callbacks:
            attr_cb_id, name_cb_id = self._attr_callbacks.pop(uuid)
            om.MMessage.removeCallback(attr_cb_id)
            om.MMessage.removeCallback(name_cb_id)

    def _on_node_attr_changed(self, plug, data, widget):
        if self._creating:
            return
        try:
            attr_name = plug.partialName()

            if attr_name == "v":  # visibility
                maya_vis = cmds.getAttr(f"{data.maya_layer_name}.visibility")
                if data.visibility != maya_vis:
                    data.visibility = maya_vis
                    widget.visibility_checkbox.blockSignals(True)
                    widget.visibility_checkbox.setChecked(maya_vis)
                    widget.visibility_checkbox.blockSignals(False)

            elif attr_name == "dt":  # displayType
                data.display_type = cmds.getAttr(f"{data.maya_layer_name}.displayType")

            elif attr_name == "c":  # index color
                color_index = cmds.getAttr(f"{data.maya_layer_name}.color")
                data.color_rgb = self._index_to_rgb(color_index)
                widget.apply_color_styles()

            elif attr_name in ("ovcr", "ovcg", "ovcb"):  # RGB color channels
                if cmds.getAttr(f"{data.maya_layer_name}.overrideRGBColors"):
                    r, g, b = cmds.getAttr(f"{data.maya_layer_name}.overrideColorRGB")[0]
                    data.color_rgb = (r, g, b)
                    widget.apply_color_styles()

        except RuntimeError:
            pass  # Widget already deleted during tool shutdown, safe to ignore

    def _on_node_renamed(self, node, old_name, data, widget):
        if self._creating:
            return
        try:
            new_name = om.MFnDependencyNode(node).name()
            data.maya_layer_name = new_name
            widget.name_edit.setText(new_name)
        except RuntimeError:
            pass  # Widget already deleted during tool shutdown, safe to ignore

    def _index_to_rgb(self, index):
        """Convert Maya color index to RGB 0-1 tuple."""
        r, g, b = cmds.colorIndex(index, q=True)
        return (r, g, b)

    # --------------------------------
    # Session Cache
    # --------------------------------

    def update_session_cache(self, uuid, export_path):
        """Called whenever a layer's export path changes."""
        _session_cache[uuid] = export_path

    def _apply_session_cache(self, data):
        """Fill in export_path from session cache if not already set."""
        if not data.export_path and data.uuid in _session_cache:
            data.export_path = _session_cache[data.uuid]

    # --------------------------------
    # Save
    # --------------------------------

    def save(self):
        payload = [x["data"].to_dict() for x in self.layers]
        cmds.fileInfo(self.FILE_INFO_KEY, json.dumps(payload))

    # --------------------------------
    # Load
    # --------------------------------

    def load(self):
        # Read fileInfo, keyed by UUID for quick lookup
        saved = {}
        raw = cmds.fileInfo(self.FILE_INFO_KEY, q=True)
        if raw:
            try:
                raw_str = raw[0].replace('\\"', '"')
                payload = json.loads(raw_str)
                saved = {item["uuid"]: item for item in payload}
            except (json.JSONDecodeError, Exception) as e:
                print(f"Failed to parse fileInfo: {e}")

        # Maya's layer stack is the source of truth
        maya_layers = [l for l in cmds.ls(type="displayLayer") if l != "defaultLayer"]

        # Sort by displayOrder descending so highest = first in the VFS list
        maya_layers.sort(key=lambda l: cmds.getAttr(f"{l}.displayOrder"), reverse=True)

        widgets = []
        for layer_name in maya_layers:
            uuid = cmds.ls(layer_name, uuid=True)[0]

            if uuid in saved:
                data = VFSLayerData.from_dict(saved[uuid])
                data.maya_layer_name = layer_name
            else:
                data = VFSLayerData(uuid=uuid, maya_layer_name=layer_name)

            # Always overwrite Maya-native fields with live values
            self._sync_from_maya(data)

            # Fill in export_path from session cache if not set by fileInfo
            self._apply_session_cache(data)

            widget = LayerWidget(data)
            widget.selected.connect(self.on_layer_selected)
            widget.path_changed.connect(self.update_session_cache)

            entry = {"data": data, "widget": widget}
            self.layers.append(entry)
            widgets.append(widget)

            self._attach_node_callback(entry)

        return widgets

    def _sync_from_maya(self, data: VFSLayerData):
        """Overwrite Maya-native fields with current values from the layer stack."""
        layer = data.maya_layer_name

        data.visibility = cmds.getAttr(f"{layer}.visibility")
        data.display_type = cmds.getAttr(f"{layer}.displayType")

        if cmds.getAttr(f"{layer}.overrideRGBColors"):
            r, g, b = cmds.getAttr(f"{layer}.overrideColorRGB")[0]
            data.color_rgb = (r, g, b)
        else:
            color_index = cmds.getAttr(f"{layer}.color")
            data.color_rgb = self._index_to_rgb(color_index)