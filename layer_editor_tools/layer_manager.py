import json

from maya import cmds

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.layer_widget import LayerWidget


class LayerManager:

    FILE_INFO_KEY = "VFSLayers"

    def __init__(self):
        self.layers = []
        self.selected_entry = None

    # --------------------------------
    # Create
    # --------------------------------

    def create_layer(self, empty=True, name="Layer"):
        maya_layer = cmds.createDisplayLayer(e=empty, n=name, mc=True)

        uuid = cmds.ls(maya_layer, uuid=True)[0]
        data = VFSLayerData(uuid=uuid, maya_layer_name=maya_layer)

        widget = LayerWidget(data)
        widget.selected.connect(self.on_layer_selected)

        entry = {"data": data, "widget": widget}
        self.layers.insert(0, entry)

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

        layer_name = entry["data"].maya_layer_name

        if cmds.objExists(layer_name):
            cmds.delete(layer_name)

        widget.setParent(None)
        widget.deleteLater()

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

        layer_a = self.layers[index]["data"].maya_layer_name
        layer_b = self.layers[new_index]["data"].maya_layer_name

        order_a = cmds.getAttr(f"{layer_a}.displayOrder")
        order_b = cmds.getAttr(f"{layer_b}.displayOrder")

        # Check if the two layers are actually adjacent in Maya's order
        # If not, find the real adjacent layer by displayOrder
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

        # Tell Maya's layer editor to refresh
        from maya import mel
        mel.eval("updateLayerEditor();")

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
                payload = json.loads(raw[0])
                saved = {item["uuid"]: item for item in payload}
            except json.JSONDecodeError:
                pass

        # Maya's layer stack is the source of truth
        maya_layers = [l for l in cmds.ls(type="displayLayer") if l != "defaultLayer"]

        # Sort by displayOrder descending so highest = first in the VFS list
        maya_layers.sort(key=lambda l: cmds.getAttr(f"{l}.displayOrder"), reverse=True)

        widgets = []
        for layer_name in maya_layers:
            uuid = cmds.ls(layer_name, uuid=True)[0]

            if uuid in saved:
                # Known layer — restore saved settings, then sync Maya-native fields
                data = VFSLayerData.from_dict(saved[uuid])
                data.maya_layer_name = layer_name
            else:
                # New layer created outside the tool — use defaults
                data = VFSLayerData(uuid=uuid, maya_layer_name=layer_name)

            # Always overwrite Maya-native fields with live values
            self._sync_from_maya(data)

            widget = LayerWidget(data)
            widget.selected.connect(self.on_layer_selected)

            entry = {"data": data, "widget": widget}
            self.layers.append(entry)
            widgets.append(widget)

        return widgets

    def _sync_from_maya(self, data: VFSLayerData):
        """Overwrite Maya-native fields with current values from the layer stack."""
        layer = data.maya_layer_name

        data.visibility = cmds.getAttr(f"{layer}.visibility")
        data.display_type = cmds.getAttr(f"{layer}.displayType")

        if cmds.getAttr(f"{layer}.overrideRGBColors"):
            r, g, b = cmds.getAttr(f"{layer}.overrideColorRGB")[0]
            data.color_rgb = (r, g, b)