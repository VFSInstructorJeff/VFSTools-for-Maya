# ------------ IMPORT LIBRARIES/MODULES ------------
import json
import re

from maya import cmds
from maya.api import OpenMaya as om

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QGuiApplication

from environments.layer_editor.layer_data import VFSLayerData, LayerTemplate      # Import data
from environments.layer_editor.layer_widget import LayerWidget     # Import UI
from environments.layer_editor.constants import HIDDEN, VISIBLE    # Import icons

# _var is to indicate a private var
# Putting this dict at module level so the information is saved even if the tool is closed
# The info only exists during the Maya session, if Maya is closed without saving it will be erased
_session_cache = {}  #  uuid (key) -> export_path (value)
_legc_session_cache = {}

# ------------ LAYER MANAGER CLASS ------------

class LayerManager:
    # Setup the variable name to look for in the .ma to check if there's saved layer information to pull from
    FILE_INFO_KEY = "VFSLayers"
    TEMPLATE_FILE_INFO_KEY = "VFSTemplateLayer"

    def __init__(self):
        self.layers = []
        self.selected_entries = []        # Selected layers, in the order they are listed (top to bottom)
        self.anchor_entry = None          # Where Shift+click ranges start from
        self.on_selection_changed = None  # Optional callback so the UI can update (e.g. the Export Selected button)
        self.template = LayerTemplate()   # TEMPLATE LAYER settings (not a real layer, never in self.layers)
        self._attr_callbacks = {}   # uuid (key) -> (attr_cb_id, name_cb_id) (tuple value)
        self._creating = False      # Checking if a layer is being created to delay other callbacks so there isn't conflict

    # ------------ CREATE LAYER METHOD ------------

    # Pass only name and if it should be empty or if it should contain the user selection
    def create_layer(self, empty=True, name="layer"):
        self._creating = True
        try:
            # The TEMPLATE LAYER's name (if set) replaces the default: Name_01, Name_02, ...
            name = self._next_template_layer_name() or name

            # Make Maya layer
            maya_layer = cmds.createDisplayLayer(e=empty, n=name)

            # Get the maya layer UUID (best way of consistently keeping track of any changes made to a layer, since all other info is mutable)
            uuid = cmds.ls(maya_layer, uuid=True)[0]
            # Make VFS layer data using the Maya layer UUID and name
            data = VFSLayerData(uuid=uuid, maya_layer_name=maya_layer)

            # Read the real values Maya gave the new layer (color, visibility, mode) instead of keeping
            # the dataclass defaults, so the widget matches what load() will read when the scene reopens
            self._sync_from_maya(data)

            # Copy the settings the user applied in the TEMPLATE LAYER over the presets
            self.apply_template(data)

            # Build the widget with the data
            widget = LayerWidget(data)
            # Connect LayerManager methods to LayerWidget Signals so widgets can emit signals to the manager
            self.connect_widget(widget)

            # Create entry layer with data from VFSLayerData and widget from LayerWidget
            entry = {"data": data, "widget": widget}
            # Insert at position 0 to mimick native Maya layer ordering
            self.layers.insert(0, entry)
            self._attach_node_callback(entry)

            if not empty:
                cmds.select(clear=True)

        finally:
            # Set _creating to False when done
            self._creating = False

        return widget

    def connect_widget(self, widget):
        """Connect a LayerWidget's signals to the manager (selection + session cache)."""
        widget.selected.connect(self.on_layer_selected)
        widget.path_changed.connect(self.update_session_cache)
        widget.legc_path_changed.connect(self.update_session_cache_legc_path)
        widget.legc_state_changed.connect(self.update_session_cache_legc)
        widget.legc_on_export_changed.connect(self.update_session_cache_legc_on_export)

    # ------------ TEMPLATE LAYER ------------

    @staticmethod
    def _safe_node_name(name):
        """Make a string usable as a Maya node name."""
        name = re.sub(r"[^0-9A-Za-z_]", "_", name.strip())
        if name and name[0].isdigit():
            name = "_" + name
        return name

    def _next_template_layer_name(self):
        """Next free 'Name_NN' for a new layer, or None if the TEMPLATE LAYER has no name."""
        base = self._safe_node_name(self.template.applied.get("layer_name", ""))
        if not base:
            return None
        pattern = re.compile(rf"^{re.escape(base)}_(\d+)$")
        numbers = [int(m.group(1)) for m in (pattern.match(l) for l in cmds.ls(type="displayLayer")) if m]
        number = max(numbers, default=0) + 1
        while cmds.objExists(f"{base}_{number:02d}"):
            number += 1
        return f"{base}_{number:02d}"

    def apply_template(self, data):
        """New layers: copy the applied TEMPLATE LAYER settings onto this layer's data AND its Maya node.
        Settings the user never set are left alone (normal presets)."""
        applied = self.template.apply_to(data)
        if not applied:
            return

        layer = data.maya_layer_name

        if "visibility" in applied:
            cmds.setAttr(f"{layer}.visibility", data.visibility)
        if "display_type" in applied:
            cmds.setAttr(f"{layer}.displayType", data.display_type)
        if "color_rgb" in applied:
            if data.color_rgb is None:
                cmds.setAttr(f"{layer}.overrideRGBColors", 0)
                cmds.setAttr(f"{layer}.color", 0)
            else:
                r, g, b = data.color_rgb
                cmds.setAttr(f"{layer}.overrideRGBColors", 1)
                cmds.setAttr(f"{layer}.overrideColorRGB", r, g, b)

        # Keep the session cache in step so these survive closing/reopening the tool unsaved
        if "export_path" in applied:
            self.update_session_cache(data.uuid, data.export_path)
        if "legc_export_path" in applied:
            self.update_session_cache_legc_path(data.uuid, data.legc_export_path)
        if "legc_on_export" in applied:
            self.update_session_cache_legc_on_export(data.uuid, data.legc_on_export)

        if {"visibility", "display_type", "color_rgb"} & set(applied):
            from maya import mel
            mel.eval("updateLayerEditor();")

    def apply_overrides(self, field_names):
        """Existing layers: push the applied TEMPLATE LAYER values for these settings onto ALL layers."""
        from maya import mel

        cmds.undoInfo(openChunk=True, chunkName="VFSTemplateOverride")
        try:
            for entry in self.layers:
                for name in field_names:
                    if name == "layer_name":
                        continue
                    entry["widget"].apply_template_value(name, self.template.applied[name])

            if "layer_name" in field_names:
                self._rename_all_layers(self.template.applied["layer_name"])

            mel.eval("updateLayerEditor();")
        finally:
            cmds.undoInfo(closeChunk=True)

    def _rename_all_layers(self, base):
        """Rename every layer to Name_01, Name_02, ... (the oldest/bottom layer gets 01, like new layers do)."""
        base = self._safe_node_name(base)
        if not base:
            return

        ordered = [e for e in reversed(self.layers) if cmds.objExists(e["data"].maya_layer_name)]

        # Two passes through temporary names so a layer can't collide with another layer's old name
        for i, entry in enumerate(ordered):
            entry["data"].maya_layer_name = cmds.rename(entry["data"].maya_layer_name, f"__vfs_rename_{i}__")

        width = max(2, len(str(len(ordered))))
        for i, entry in enumerate(ordered, 1):
            new_name = cmds.rename(entry["data"].maya_layer_name, f"{base}_{i:0{width}d}")
            entry["data"].maya_layer_name = new_name
            entry["widget"].name_edit.setText(new_name)
            entry["widget"].name_edit.setCursorPosition(0)

    # Saved straight away on Apply (not only before a scene save), so it survives closing/reopening the tool.
    # fileInfo lives in the scene, so a new scene starts with a blank TEMPLATE LAYER.
    def save_template(self):
        cmds.fileInfo(self.TEMPLATE_FILE_INFO_KEY, json.dumps(self.template.to_dict()))

    def load_template(self):
        raw = cmds.fileInfo(self.TEMPLATE_FILE_INFO_KEY, q=True)
        loaded = {}
        if raw:
            try:
                loaded = json.loads(raw[0].replace('\\"', '"'))
            except Exception as e:
                print(f"Failed to parse TEMPLATE LAYER fileInfo: {e}")
        self.template.load_dict(loaded)

    # ------------ REMOVE LAYER METHODS ------------

    def remove_selected(self):
        # If no layers are selected, return
        if not self.selected_entries:
            return
        # Remove every selected layer (a copy of the list, since remove_layer edits the selection)
        for entry in list(self.selected_entries):
            self.remove_layer(entry["widget"])
    
    def remove_layer(self, widget):
        """
            There are 5 steps to layer removal:
            1. Removing all callbacks associated with the layer
            2. Removing the Maya layer
            3. Removing the PySide/VFS layer widget
            4. Removing the layer info from the _session_cache (the current Maya session's unsaved info)
            5. Removing the layer info from the Layer Manager
        """
        # Iterate through layers until the widget info matches the selected widget, if none match, make entry = None
        # Using next() to get the first result that matches and then stop iterating
        entry = next(
            (x for x in self.layers if x["widget"] == widget),
            None
        )

        if not entry:
            return

        # Get UUID and name from the entry's data
        uuid = entry["data"].uuid
        layer_name = entry["data"].maya_layer_name

        # Remove node callbacks
        self._remove_node_callback(uuid)

        # Delete the Maya layer
        if cmds.objExists(layer_name):
            cmds.delete(layer_name)

        # Unparent widget from UI and schedule deletion
        widget.setParent(None)
        widget.deleteLater()

        # Remove from session cache
        if uuid in _session_cache:
            del _session_cache[uuid]
        
        if uuid in _legc_session_cache:
            del _legc_session_cache[uuid]

        # Remove it from Layer Manager list (and the selection)
        self.layers.remove(entry)
        if entry in self.selected_entries:
            self.selected_entries.remove(entry)
            self._notify_selection_changed()
        if self.anchor_entry is entry:
            self.anchor_entry = None

    # ------------ SELECT LAYER METHOD ------------

    def on_layer_selected(self, widget):
        """A layer was clicked. Works like a file browser:
            click            -> only this layer
            Ctrl+click       -> add/remove this layer
            Shift+click      -> every layer from the last clicked one to this one
            Ctrl+Shift+click -> add that range to the current selection
        """
        entry = next((x for x in self.layers if x["widget"] == widget), None)
        if entry is None:
            return

        modifiers = QGuiApplication.keyboardModifiers()
        ctrl = bool(modifiers & Qt.ControlModifier)
        shift = bool(modifiers & Qt.ShiftModifier)

        if shift and self.anchor_entry in self.layers:
            start = self.layers.index(self.anchor_entry)
            end = self.layers.index(entry)
            low, high = min(start, end), max(start, end)
            selection = self.layers[low:high + 1]
            if ctrl:
                selection = list(self.selected_entries) + [e for e in selection if e not in self.selected_entries]
            # The anchor stays put, so the range can be adjusted with further Shift+clicks
        elif ctrl:
            selection = list(self.selected_entries)
            if entry in selection:
                selection.remove(entry)
            else:
                selection.append(entry)
            self.anchor_entry = entry
        else:
            selection = [entry]
            self.anchor_entry = entry

        self._set_selection(selection)

    def clear_selection(self):
        self._set_selection([])
        self.anchor_entry = None

    def _set_selection(self, entries):
        chosen = [e for e in self.layers if e in entries]   # Keep list order (top to bottom)
        for entry in self.layers:
            entry["widget"].set_selected(entry in chosen)
        self.selected_entries = chosen
        self._notify_selection_changed()

    def _notify_selection_changed(self):
        if self.on_selection_changed:
            self.on_selection_changed()

    # ------------ REORDER LAYERS METHODS ------------

    def move_selected_up(self):
        self._move_selected("up")

    def move_selected_down(self):
        self._move_selected("down")

    def _move_selected(self, direction):
        """Move all selected layers one step, keeping them in the same order relative to each other.
        A selected layer that is blocked (at the edge, or behind another blocked one) stays where it is."""
        if not self.selected_entries:
            return

        selected_ids = {id(e) for e in self.selected_entries}
        indices = [i for i, e in enumerate(self.layers) if id(e) in selected_ids]
        if direction == "down":
            indices.reverse()       # Start from the bottom so layers don't step on each other

        step = -1 if direction == "up" else 1
        for index in indices:
            neighbour = index + step
            if neighbour < 0 or neighbour >= len(self.layers):
                continue
            if id(self.layers[neighbour]) in selected_ids:
                continue
            self.move_layer(self.layers[index]["widget"], direction)

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

    # ------------ NODE CALLBACKS ------------

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
                    widget.visibility_button.blockSignals(True)
                    widget.visibility_button.setChecked(not maya_vis)
                    widget.visibility_button.setIcon(QIcon(HIDDEN) if not maya_vis else QIcon(VISIBLE))
                    widget.visibility_button.blockSignals(False)

            elif attr_name == "dt":  # displayType
                data.display_type = cmds.getAttr(f"{data.maya_layer_name}.displayType")
                widget.mode_button.setText(["N", "T", "R"][data.display_type])

            elif attr_name in ("c", "ovrgb", "ovcr", "ovcg", "ovcb"):  # index color, RGB toggle, RGB channels
                data.color_rgb = self._read_layer_color(data.maya_layer_name)
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

    def _read_layer_color(self, layer):
        """The layer's color as an RGB 0-1 tuple, or None when it has no custom color.

        Layers that were never given a color sit on color index 0, Maya's default. That index is
        deliberately NOT converted to an RGB value (the converted value never matched what Maya shows,
        which made the color shift when a scene was reopened), the layer is simply treated as uncolored.
        """
        if cmds.getAttr(f"{layer}.overrideRGBColors"):
            r, g, b = cmds.getAttr(f"{layer}.overrideColorRGB")[0]
            return (r, g, b)
        color_index = cmds.getAttr(f"{layer}.color")
        if color_index == 0:
            return None
        return self._index_to_rgb(color_index)

    def _index_to_rgb(self, index):
        """Convert Maya color index to RGB 0-1 tuple."""
        r, g, b = cmds.colorIndex(index, q=True)
        return (r, g, b)

    # ------------ SESSION CACHE ------------

    def update_session_cache(self, uuid, export_path):
        """Called whenever a layer's export path changes."""
        if uuid not in _session_cache or isinstance(_session_cache[uuid], str):
            _session_cache[uuid] = {}
        _session_cache[uuid]["export_path"] = export_path

    def update_session_cache_legc(self, uuid, legc_applied):
        if uuid not in _session_cache or isinstance(_session_cache[uuid], str):
            _session_cache[uuid] = {}
        _session_cache[uuid]["legc_applied"] = legc_applied

    def update_session_cache_legc_on_export(self, uuid, legc_on_export):
        if uuid not in _session_cache or isinstance(_session_cache[uuid], str):
            _session_cache[uuid] = {}
        _session_cache[uuid]["legc_on_export"] = legc_on_export

    def update_session_cache_legc_path(self, uuid, legc_export_path):
        if uuid not in _session_cache  or isinstance(_session_cache[uuid], str):
            _session_cache[uuid] = {}
        _session_cache[uuid]["legc_export_path"] = legc_export_path

    def _apply_session_cache(self, data):
        """Fill in export_path from session cache if not already set."""
        # Add temporarily to _apply_session_cache at the top
        if data.uuid in _session_cache:
            cached = _session_cache[data.uuid]
            if isinstance(cached, str):
                # Legacy format (plain string was the export path)
                data.export_path = cached
                return
            if "export_path" in cached:
                data.export_path = cached["export_path"]
            if "legc_export_path" in cached:
                data.legc_export_path = cached["legc_export_path"]
            if "legc_applied" in cached:
                data.legc_applied = cached["legc_applied"]
            if "legc_on_export" in cached:
                data.legc_on_export = cached["legc_on_export"]
                
    # ------------ SAVE ------------

    def save(self):
        payload = [x["data"].to_dict() for x in self.layers]
        cmds.fileInfo(self.FILE_INFO_KEY, json.dumps(payload))

    # ------------ LOAD ------------

    def _read_saved_layers(self):
        """The layer data saved in the scene's fileInfo, keyed by UUID."""
        saved = {}
        raw = cmds.fileInfo(self.FILE_INFO_KEY, q=True)
        if raw:
            try:
                raw_str = raw[0].replace('\\"', '"')
                payload = json.loads(raw_str)
                saved = {item["uuid"]: item for item in payload}
            except (json.JSONDecodeError, Exception) as e:
                print(f"Failed to parse fileInfo: {e}")
        return saved

    def _make_entry(self, layer_name, uuid, saved_item=None):
        """Build the data + widget for an existing Maya layer and attach its callbacks (not added to self.layers)."""
        if saved_item:
            data = VFSLayerData.from_dict(saved_item)
            data.maya_layer_name = layer_name
        else:
            data = VFSLayerData(uuid=uuid, maya_layer_name=layer_name)

        # Always overwrite Maya-native fields with live values
        self._sync_from_maya(data)

        # Fill in export_path from session cache if not set by fileInfo
        self._apply_session_cache(data)

        widget = LayerWidget(data)
        self.connect_widget(widget)

        entry = {"data": data, "widget": widget}
        self._attach_node_callback(entry)
        return entry

    def load(self):
        # Read fileInfo, keyed by UUID for quick lookup
        saved = self._read_saved_layers()

        # Maya's layer stack is the source of truth
        maya_layers = [l for l in cmds.ls(type="displayLayer") if l != "defaultLayer"]

        # Sort by displayOrder descending so highest = first in the VFS list
        maya_layers.sort(key=lambda l: cmds.getAttr(f"{l}.displayOrder"), reverse=True)

        widgets = []
        for layer_name in maya_layers:
            uuid = cmds.ls(layer_name, uuid=True)[0]

            entry = self._make_entry(layer_name, uuid, saved.get(uuid))
            self.layers.append(entry)
            widgets.append(entry["widget"])

        return widgets

    def resync(self):
        """Make the tool match the layers that actually exist in Maya (after layers were deleted, restored
        with undo, or otherwise changed outside of this tool):
            1. rows whose Maya layer is gone are removed (the layer's cached paths are kept in case it comes back)
            2. Maya layers that have no row yet get one
            3. every other row re-reads its name, visibility, mode and color from Maya
            4. rows follow Maya's layer order
        Returns (added layer names, removed layer names)."""
        maya_layers = [l for l in cmds.ls(type="displayLayer") if l != "defaultLayer"]
        maya_by_uuid = {cmds.ls(l, uuid=True)[0]: l for l in maya_layers}

        # 1. Layers deleted in Maya
        removed = []
        for entry in list(self.layers):
            if entry["data"].uuid not in maya_by_uuid:
                removed.append(entry["data"].maya_layer_name)
                self._discard_entry(entry)

        # 2. Layers that exist in Maya but not here (data comes from the scene's saved info + session cache)
        known = {entry["data"].uuid for entry in self.layers}
        saved = self._read_saved_layers()
        added = []
        for uuid, layer_name in maya_by_uuid.items():
            if uuid not in known:
                self.layers.append(self._make_entry(layer_name, uuid, saved.get(uuid)))
                added.append(layer_name)

        # 3. Everything else: re-read from Maya, re-attach callbacks (a restored node can leave stale ones)
        for entry in self.layers:
            data = entry["data"]
            if data.maya_layer_name in added:
                continue
            data.maya_layer_name = maya_by_uuid[data.uuid]
            self._sync_from_maya(data)
            entry["widget"].refresh_from_data()
            try:
                self._remove_node_callback(data.uuid)
            except Exception:
                pass    # Stale callback ids are fine, we attach fresh ones below
            self._attach_node_callback(entry)

        # 4. Maya's order: highest displayOrder first, like load()
        self.layers.sort(key=lambda e: cmds.getAttr(f"{e['data'].maya_layer_name}.displayOrder"), reverse=True)

        return added, removed

    def _discard_entry(self, entry):
        """Drop a row whose Maya layer no longer exists. Unlike remove_layer() this never touches Maya,
        and keeps the session cache (so the layer's paths come back if the deletion is undone)."""
        try:
            self._remove_node_callback(entry["data"].uuid)
        except Exception:
            pass    # The node is already gone, its callbacks may be too

        widget = entry["widget"]
        widget.setParent(None)
        widget.deleteLater()

        self.layers.remove(entry)
        if entry in self.selected_entries:
            self.selected_entries.remove(entry)
            self._notify_selection_changed()
        if self.anchor_entry is entry:
            self.anchor_entry = None

    def _sync_from_maya(self, data: VFSLayerData):
        """Overwrite Maya-native fields with current values from the layer stack."""
        layer = data.maya_layer_name

        data.visibility = cmds.getAttr(f"{layer}.visibility")
        data.display_type = cmds.getAttr(f"{layer}.displayType")

        data.color_rgb = self._read_layer_color(layer)