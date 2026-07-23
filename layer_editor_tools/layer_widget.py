# ------------ IMPORT LIBRARIES/MODULES ------------
import webbrowser
from pathlib import Path

from maya import cmds, mel

from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QDrag, QIcon
from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QHBoxLayout,
                                QVBoxLayout, QCheckBox, QComboBox, QColorDialog,
                                QFileDialog, QMessageBox, QMenu, QFrame, QLabel,
                                QSizePolicy)

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.utils import hex_to_rgb, rgb_to_hex, shifted_background_color
from layer_editor_tools.constants import VISIBLE, HIDDEN, CONFIG_DROPDOWN, FOLDER_OPEN, BUG_REPORT_URL, HELP, BUG_REPORT, DRAG_HANDLE, UNDO

# Layer display types and their labels for the cycling button
LAYER_MODES = ["N", "T", "R"]


# ------------ LAYER NAME EDIT ------------
# Subclassed to emit editingFinished on focus loss so clicking outside confirms rename

class LayerNameEdit(QLineEdit):
    def focusOutEvent(self, event):
        if not self.isReadOnly():
            self.editingFinished.emit()
        super().focusOutEvent(event)


# ------------ LAYER WIDGET CLASS ------------

class LayerWidget(QWidget):

    # ------------ SIGNALS ------------
    selected = Signal(object)           # Emitted when the layer is selected
    path_changed = Signal(str, str)     # Emitted when export path changes: uuid, export_path
    legc_path_changed = Signal(str, str)  # uuid, legc_export_path
    legc_state_changed = Signal(str, bool)  # uuid, legc_applied

    def __init__(self, data: VFSLayerData):
        super().__init__()
        self.data = data
        self.setFixedHeight(30)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(2)
        self.main_layout.setContentsMargins(4, 4, 4, 4)
        self.build_ui()
        self.populate_ui()
        self.connect_signals()

    # ------------ BUILD UI ------------

    def build_ui(self):

        # ---- TOP ROW ----
        self.top_row = QWidget()
        self.top_layout = QHBoxLayout(self.top_row)
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        '''
        TODO: Get draggable feature working. For now, just commenting this out since it doesn't work currently.
        drag_handle_icon = QIcon(DRAG_HANDLE)
        drag_handle_pixmap = drag_handle_icon.pixmap(20, 20)
        self.drag_handle = QLabel()
        self.drag_handle.setPixmap(drag_handle_pixmap)
        self.drag_handle.setFixedWidth(16)
        self.drag_handle.setCursor(Qt.SizeVerCursor)
        self.top_layout.insertWidget(0, self.drag_handle)
        '''

        self.color_button = QPushButton()
        self.color_button.setFixedWidth(20)
        self.color_button.setToolTip("Pick layer color")

        self.name_edit = LayerNameEdit(self.data.maya_layer_name)
        self.name_edit.setMinimumWidth(80)
        self.name_edit.setReadOnly(True)
        self.name_edit.setStyleSheet("QLineEdit { border: none; background: rgba(255, 255, 255, 10); }")
        self.name_edit.setToolTip("Layer name — double click to rename")
        self.name_edit.installEventFilter(self)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.visibility_button = QPushButton(QIcon(VISIBLE), "")
        self.visibility_button.setFixedWidth(24)
        self.visibility_button.setCheckable(True)
        self.visibility_button.setToolTip("Toggle layer visibility")

        self.mode_button = QPushButton(LAYER_MODES[self.data.display_type])
        self.mode_button.setFixedWidth(24)
        self.mode_button.setToolTip("Cycle layer mode: Normal / Template / Reference")

        self.export_toggle = QPushButton(QIcon(CONFIG_DROPDOWN), "")
        self.export_toggle.setFixedWidth(24)
        self.export_toggle.setCheckable(True)
        self.export_toggle.setToolTip("Toggle export settings")

        self.export_button = QPushButton("Export")
        self.export_button.setFixedWidth(60)
        self.export_button.setToolTip("Export layer")

        # self.top_layout.addWidget(self.drag_handle)
        self.top_layout.addWidget(self.color_button)
        self.top_layout.addWidget(self.name_edit)
        self.top_layout.addWidget(spacer)
        self.top_layout.addWidget(self.visibility_button)
        self.top_layout.addWidget(self.mode_button)
        self.top_layout.addWidget(self.export_toggle)
        self.top_layout.addWidget(self.export_button)

        # --- SEPARATOR ---
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setStyleSheet("color: rgba(255, 255, 255, 40);")
        self.separator.setVisible(False)

        # ---- BOTTOM ROW (export settings, hidden by default) ----
        self.bottom_row = QWidget()
        self.bottom_layout = QHBoxLayout(self.bottom_row)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)

        self.path_button = QPushButton(QIcon(FOLDER_OPEN), "")
        self.path_button.setFixedWidth(24)
        self.path_button.setToolTip("Set export folder")

        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)
        self.path_edit.setPlaceholderText("No export path set")
        self.path_edit.setToolTip("Export path")

        self.legc_path_edit = QLineEdit()
        self.legc_path_edit.setReadOnly(True)
        self.legc_path_edit.setPlaceholderText("No LEGC export path set")
        self.legc_path_edit.setToolTip("LEGC export path")
        self.legc_path_edit.setVisible(False)

        self.origin_checkbox = QCheckBox("Origin")
        self.origin_checkbox.setToolTip("Move objects to origin before exporting")

        self.legc_checkbox = QCheckBox("LEGC")
        self.legc_checkbox.setToolTip("Run LEGC UV operation on export")

        self.legc_undo_label = QLabel("LEGC")
        self.legc_undo_label.setVisible(False)

        self.legc_undo_button = QPushButton(QIcon(UNDO), "")
        self.legc_undo_button.setFixedWidth(20)
        self.legc_undo_button.setToolTip("Undo LEGC")
        self.legc_undo_button.setVisible(False)
        
        self.bottom_layout.addWidget(self.path_button)
        self.bottom_layout.addWidget(self.path_edit)
        self.bottom_layout.addWidget(self.legc_path_edit)
        self.bottom_layout.addWidget(self.origin_checkbox)
        self.bottom_layout.addWidget(self.legc_checkbox)
        self.bottom_layout.addWidget(self.legc_undo_button)
        self.bottom_layout.addWidget(self.legc_undo_label)

        self.bottom_row.setVisible(False)

        # ---- ADD ROWS TO MAIN LAYOUT ----
        self.main_layout.addWidget(self.top_row)
        self.main_layout.addWidget(self.separator)
        self.main_layout.addWidget(self.bottom_row)

    def populate_ui(self):
        # Visibility button reflects current state
        self.visibility_button.setChecked(not self.data.visibility)
        self.visibility_button.setIcon(QIcon(HIDDEN) if not self.data.visibility else QIcon(VISIBLE))

        self.mode_button.setText(LAYER_MODES[self.data.display_type])
        self.origin_checkbox.setChecked(self.data.use_origin)

        if self.data.export_path:
            self.path_edit.setText(self.data.export_path)
            self.export_toggle.setChecked(True)
            self.toggle_export_row(True)

        if self.data.legc_export_path:
            self.legc_path_edit.setText(self.data.legc_export_path)

        if self.data.legc_applied:
            self.legc_checkbox.setVisible(False)
            self.legc_undo_label.setVisible(True)
            self.legc_undo_button.setVisible(True)

        self.name_edit.setCursorPosition(0)
        self.apply_color_styles()

    def connect_signals(self):
        self.color_button.clicked.connect(self.pick_color)
        self.name_edit.editingFinished.connect(self.finish_rename)
        self.visibility_button.toggled.connect(self.on_visibility_changed)
        self.mode_button.clicked.connect(self.cycle_layer_mode)
        self.export_toggle.toggled.connect(self.toggle_export_row)
        self.export_button.clicked.connect(self.export_layer)
        self.path_button.clicked.connect(self.pick_export_path)
        self.origin_checkbox.toggled.connect(self.on_origin_changed)
        self.legc_checkbox.toggled.connect(self.on_legc_toggled)
        self.legc_undo_button.clicked.connect(self.undo_legc)

    # ------------ EVENT FILTER ------------

    def eventFilter(self, obj, event):
        if obj == self.name_edit:
            if event.type() == QEvent.Type.MouseButtonDblClick:
                self.start_rename()
                return True
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self.selected.emit(self)
        return super().eventFilter(obj, event)

    # ------------ RENAME ------------

    def start_rename(self):
        self.name_edit.setReadOnly(False)
        self.name_edit.setStyleSheet("")
        self.name_edit.setFocus()
        self.name_edit.selectAll()

    def finish_rename(self):
        self.name_edit.setReadOnly(True)
        self.name_edit.setStyleSheet("QLineEdit { border: none; background: rgba(255, 255, 255, 10); }")
        self.name_edit.setCursorPosition(0)
        self.rename_layer()

    # ------------ SELECTION ------------

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selected.emit(self)
        elif event.button() == Qt.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())
        super().mousePressEvent(event)

    def set_selected(self, is_selected: bool):
        """Toggle visual selected state."""
        self.setProperty("selected", is_selected)
        self.style().unpolish(self)
        self.style().polish(self)

    # ------------ CONTEXT MENU ------------

    def show_context_menu(self, pos):
        menu = QMenu(self)

        # Title — disabled so it acts as a label
        title = menu.addAction("VFS Layer Tools")
        title.setEnabled(False)
        menu.addSeparator()

        menu.addAction("Select All", self.select_all)
        menu.addAction("Select SM", self.select_sm)
        menu.addAction("Select UCX", self.select_ucx)
        menu.addSeparator()
        menu.addAction("Add To Layer", self.add_selection_to_layer)
        menu.addAction("Remove From Layer", self.remove_selection_from_layer)
        menu.addAction("Empty Layer", self.empty_layer)
        menu.addSeparator()
        menu.addAction("Help", self.open_help)
        menu.addAction("Report A Bug", self.report_bug)

        menu.exec(pos)

    # ------------ EXPORT ROW TOGGLE ------------

    def toggle_export_row(self, checked):
        self.bottom_row.setVisible(checked)
        self.separator.setVisible(checked)
        self.export_toggle.setIcon(QIcon(CONFIG_DROPDOWN))
        self.setFixedHeight(60 if checked else 30)

    # ------------ LEGC TOGGLE ------------

    def on_legc_toggled(self, checked):
        self.path_edit.setVisible(not checked)
        self.legc_path_edit.setVisible(checked)

    # ------------ MAYA UPDATES ------------

    def on_visibility_changed(self, hidden):
        # Button is checked when layer is HIDDEN, so we invert
        self.data.visibility = not hidden
        cmds.setAttr(f"{self.data.maya_layer_name}.visibility", not hidden)
        self.visibility_button.setIcon(QIcon(HIDDEN) if hidden else QIcon(VISIBLE))
        mel.eval("updateLayerEditor();")

    def cycle_layer_mode(self):
        # Cycle through Normal (0) -> Template (1) -> Reference (2) -> Normal (0)
        next_mode = (self.data.display_type + 1) % len(LAYER_MODES)
        self.data.display_type = next_mode
        self.mode_button.setText(LAYER_MODES[next_mode])
        cmds.setAttr(f"{self.data.maya_layer_name}.displayType", next_mode)

    def on_origin_changed(self, checked):
        self.data.use_origin = checked

    def rename_layer(self):
        new_name = self.name_edit.text()
        if not cmds.objExists(self.data.maya_layer_name):
            return
        new_layer_name = cmds.rename(self.data.maya_layer_name, new_name)
        self.data.maya_layer_name = new_layer_name

    # ------------ CONTEXT MENU ACTIONS ------------

    def select_all(self):
        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        all_objects = [obj for obj in members]
        for obj in members:
            descendants = cmds.listRelatives(obj, allDescendents=True, fullPath=True) or []
            all_objects.extend(descendants)
        if all_objects:
            cmds.select(all_objects)
        else:
            cmds.select(clear=True)

    def select_sm(self):
        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        sm_members = []
        for obj in members:
            all_nodes = [obj] + (cmds.listRelatives(obj, allDescendents=True, fullPath=True) or [])
            for node in all_nodes:
                short_name = node.split("|")[-1]
                if not short_name.startswith("UCX_") and cmds.nodeType(node) == "transform":
                    children = cmds.listRelatives(node, children=True, fullPath=True) or []
                    has_shape = any(cmds.nodeType(c) in ("mesh", "nurbsSurface", "nurbsCurve", "lattice") for c in children)
                    if has_shape:
                        sm_members.append(node)
        if sm_members:
            cmds.select(sm_members)
        else:
            cmds.select(clear=True)

    def select_ucx(self):
        """Select all UCX meshes in this layer."""
        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        ucx_members = []
        for obj in members:
            children = cmds.listRelatives(obj, allDescendents=True, fullPath=True) or []
            for child in children:
                if child.split("|")[-1].startswith("UCX_"):
                    ucx_members.append(child)
        if ucx_members:
            cmds.select(ucx_members)
        else:
            cmds.select(clear=True)

    def add_selection_to_layer(self):
        """Add currently selected Maya objects to this layer."""
        selection = cmds.ls(selection=True)
        if not selection:
            QMessageBox.warning(self, "Add To Layer", "Nothing is currently selected.")
            return
        cmds.editDisplayLayerMembers(self.data.maya_layer_name, *selection)

    def remove_selection_from_layer(self):
        """Remove currently selected Maya objects from this layer."""
        selection = cmds.ls(selection=True)
        if not selection:
            QMessageBox.warning(self, "Remove From Layer", "Nothing is currently selected.")
            return
        cmds.editDisplayLayerMembers("defaultLayer", *selection)

    def empty_layer(self):
        """Remove all objects from this layer."""
        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        if not members:
            QMessageBox.warning(self, "Empty Layer", "Layer is already empty.")
            return
        confirm = QMessageBox.question(
            self,
            "Empty Layer",
            f"Remove all {len(members)} object(s) from {self.data.maya_layer_name}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            cmds.editDisplayLayerMembers("defaultLayer", *members)

    def open_help(self):
        # TODO: Add documentation URL
        pass

    def report_bug(self):
        webbrowser.open(BUG_REPORT_URL)

    # ------------ EXPORT PATH ------------

    def pick_export_path(self):
        is_legc = self.legc_checkbox.isChecked()
        current_path = self.data.legc_export_path if is_legc else self.data.export_path

        path = QFileDialog.getExistingDirectory(
            self,
            "Select LEGC Export Folder" if is_legc else "Select Export Folder",
            current_path or ""
        )
        if path:
            if is_legc:
                self.data.legc_export_path = path
                self.legc_path_edit.setText(path)
                self.legc_path_changed.emit(self.data.uuid, path)
            else:
                self.data.export_path = path
                self.path_edit.setText(path)
                self.path_changed.emit(self.data.uuid, path)

    # ------------ EXPORT HELPERS ------------

    def _get_top_level_members(self, members):
        """Filter members down to top-level transforms only, excluding shape nodes
        and transforms whose parent is also in the layer."""
        member_set = set(members)
        top_level = []
        for obj in members:
            if cmds.nodeType(obj) != "transform":
                continue
            parent = cmds.listRelatives(obj, parent=True, fullPath=True)
            if parent and parent[0] in member_set:
                continue
            top_level.append(obj)
        return top_level

    def _move_to_origin(self, members):
        """Move each top-level object to origin and return their original positions."""
        top_level = self._get_top_level_members(members)
        original_positions = {}
        for obj in top_level:
            pos = cmds.xform(obj, q=True, worldSpace=True, rotatePivot=True)
            original_positions[obj] = pos
            cmds.move(0, 0, 0, obj, worldSpace=True, rotatePivotRelative=True)
        return original_positions

    def _restore_positions(self, original_positions):
        """Restore each top-level object to its original position."""
        for obj, pos in original_positions.items():
            if cmds.objExists(obj):
                cmds.move(pos[0], pos[1], pos[2], obj, worldSpace=True, rotatePivotRelative=True)

    def _capture_shading_groups(self, valid_shapes):
        """Capture per-face and per-mesh shading group assignments for valid shapes."""
        # Build lookup sets for shapes and their parent transform names
        valid_shape_set = set(valid_shapes)
        valid_shape_short = {s.split("|")[-1] for s in valid_shapes}
        valid_transform_short = set()
        for shape in valid_shapes:
            try:
                parent = cmds.listRelatives(shape, parent=True, fullPath=True)
                if parent:
                    valid_transform_short.add(parent[0].split("|")[-1])
            except ValueError as value_error_msg:
                QMessageBox.warning(
                    self,
                    "LEGC Material Saving Failed",
                    f"Something went wrong with the LEGC Material Saving procedure.\n\n{value_error_msg}"
                )

        # Get all SGs connected to valid shapes, deduplicated
        all_sgs = set()
        for shape in valid_shapes:
            sgs = cmds.listConnections(shape, type="shadingEngine") or []
            all_sgs.update(sgs)

        original_shading_groups = {}  # sg -> [components]

        for sg in all_sgs:
            sg_members = cmds.sets(sg, q=True) or []
            relevant_components = []

            for member in sg_members:
                if "." in member:
                    # Face-level assignment: node name before "." is the transform name
                    node_name = member.split(".")[0]
                    node_name = node_name.split("|")[-1]
                    if node_name in valid_transform_short:
                        relevant_components.append(member)
                else:
                    # Whole mesh assignment: check against shape names
                    short = member.split("|")[-1]
                    if member in valid_shape_set or short in valid_shape_short:
                        relevant_components.append(member)

            if relevant_components:
                original_shading_groups[sg] = relevant_components

        return original_shading_groups

    def _restore_shading_groups(self, original_shading_groups):
        """Restore per-face and per-mesh shading group assignments."""
        for sg, components in original_shading_groups.items():
            if not cmds.objExists(sg):
                continue
            valid_components = [c for c in components if cmds.objExists(c.split(".")[0])]
            if valid_components:
                cmds.sets(valid_components, edit=True, forceElement=sg)
        # Force viewport refresh to clear any stale shading group visualization
        cmds.refresh(force=True)

    # ------------ LEGC ------------

    def _run_legc(self, members):
        """Run LEGC: duplicate map1 as uvSet1, layout all shells together,
        freeze transforms, delete history, then assign standardSurface1."""

        # ---- LAYOUT SETTINGS (adjust here if needed) ----
        LAYOUT_RESOLUTION = 256
        # Spacing and Margin are Shell Padding or Tile Padding divided by Map Size (in this case, 8/2048 = 0.00390625)
        LAYOUT_SHELL_SPACING = 0.00390625
        LAYOUT_TILE_MARGIN = 0.00390625 
        LAYOUT_MUTATIONS = 1
        LAYOUT_SCALE = 1

        # Get top level transforms only
        top_level = self._get_top_level_members(members)

        # Expand to include all descendant transforms
        all_transforms = []
        for obj in top_level:
            all_transforms.append(obj)
            descendants = cmds.listRelatives(obj, allDescendents=True, fullPath=True, type="transform") or []
            all_transforms.extend(descendants)

        skipped = []
        valid_shapes = []

        for transform in all_transforms:
            short_name = transform.split("|")[-1]

            # Skip UCX and group nodes by transform name
            if short_name.startswith("UCX_") or short_name.endswith("_grp"):
                continue

            # Get shape nodes from this transform
            shapes = cmds.listRelatives(transform, shapes=True, fullPath=True, type="mesh") or []

            for shape in shapes:
                existing_uvsets = cmds.polyUVSet(shape, q=True, allUVSets=True) or []
                if "uvSet1" in existing_uvsets:
                    skipped.append(short_name)
                    continue

                if not existing_uvsets:
                    continue

                first_uvset = existing_uvsets[0]

                # We're creating a new UV set instead of duplicating the existing map1 to avoid a Maya bug
                # Where reordering the UV sets overrides them, undoing the layout of the LEGC UV set
                
                # Create new empty UV set called uvSet1
                cmds.select(shape)
                cmds.polyUVSet(create=True, uvSet = "uvSet1")
                cmds.polyCopyUV(shape, uvSetNameInput = first_uvset, uvSetName = "uvSet1")

                # Reorder uvSet1 to be first
                mel.eval(f'polyUVSet -reorder -uvSet "uvSet1" -newUVSet "{first_uvset}" {shape};')

                # Set uvSet1 as current
                cmds.polyUVSet(shape, currentUVSet=True, uvSet="uvSet1")

                valid_shapes.append(shape)

        if skipped:
            QMessageBox.warning(
                self,
                "LEGC Skipped",
                "The following meshes already have a uvSet1 and were skipped:\n\n" +
                "\n".join(skipped)
            )

        if not valid_shapes:
            return {}

        try:
            # Layout all valid mesh UV shells together in a single operation
            #uv_faces = [f"{shape}.f[*]" for shape in valid_shapes]
            cmds.select(valid_shapes)
            cmds.polyUVSet(currentUVSet=True, uvSet="uvSet1")
            cmds.u3dLayout( valid_shapes,
                            scl = LAYOUT_SCALE,
                            resolution=LAYOUT_RESOLUTION,
                            shellSpacing=LAYOUT_SHELL_SPACING,
                            tileMargin=LAYOUT_TILE_MARGIN,
                            mutations=LAYOUT_MUTATIONS,
                            box=(0, 1, 0, 1)
                            )
        except RuntimeError as runtime_error_msg:
            QMessageBox.warning(
                self,
                "LEGC Layout Failed",
                f"Something went wrong with the LEGC Layout procedure.\n\n{runtime_error_msg}"
            )

        # Get transforms from valid shapes
        valid_transforms = [
            cmds.listRelatives(shape, parent=True, fullPath=True)[0]
            for shape in valid_shapes
        ]

        # Freeze transforms
        cmds.makeIdentity(valid_transforms, apply=True, translate=True, rotate=True, scale=True, normal=False)

        # Delete history
        cmds.delete(valid_transforms, constructionHistory=True)

        # Capture per-face shading group assignments before material assignment
        original_shading_groups = self._capture_shading_groups(valid_shapes)

        # Assign standardSurface1 to all valid meshes
        cmds.select(valid_transforms)
        cmds.hyperShade(assign="standardSurface1")

        return {
            "valid_shapes": valid_shapes,
            "valid_transforms": valid_transforms,
            "original_shading_groups": original_shading_groups
        }

    def undo_legc(self):
        confirm = QMessageBox.question(
            self,
            "Undo LEGC",
            "This will delete uvSet1 from all valid meshes in this layer. Are you sure?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        if not members:
            QMessageBox.warning(self, "Undo LEGC", "No objects found in this layer.")
            return

        # Get all transforms
        top_level = self._get_top_level_members(members)
        all_transforms = []
        for obj in top_level:
            all_transforms.append(obj)
            descendants = cmds.listRelatives(obj, allDescendents=True, fullPath=True, type="transform") or []
            all_transforms.extend(descendants)

        processed = []
        skipped = []

        for transform in all_transforms:
            short_name = transform.split("|")[-1]
            if short_name.startswith("UCX_") or short_name.endswith("_grp"):
                continue

            shapes = cmds.listRelatives(transform, shapes=True, fullPath=True, type="mesh") or []
            for shape in shapes:
                try:
                    existing_uvsets = cmds.polyUVSet(shape, q=True, allUVSets=True) or []
                    if "uvSet1" not in existing_uvsets:
                        skipped.append(short_name)
                        continue

                    # If uvSet1 is on top, move map1 to top first
                    if existing_uvsets[0] == "uvSet1" and "map1" in existing_uvsets:
                        mel.eval(f'polyUVSet -reorder -uvSet "map1" -newUVSet "uvSet1" {shape};')
                        cmds.polyUVSet(shape, currentUVSet=True, uvSet="map1")

                    # Delete uvSet1
                    cmds.polyUVSet(shape, delete=True, uvSet="uvSet1")
                    processed.append(short_name)

                except RuntimeError as e:
                    QMessageBox.warning(self, "Undo LEGC Failed",
                        f"Could not undo LEGC on {short_name}:\n\n{e}")

        # Swap button back to checkbox
        self.legc_undo_button.setVisible(False)
        self.legc_undo_label.setVisible(False)
        self.legc_checkbox.setVisible(True)
        self.data.legc_applied = False
        self.legc_state_changed.emit(self.data.uuid, False)

        # Build result message
        msg_parts = []
        if processed:
            msg_parts.append(f"uvSet1 removed from: {', '.join(processed)}")
        if skipped:
            msg_parts.append(f"No uvSet1 found on: {', '.join(skipped)}")

        cmds.inViewMessage(
            amg="LEGC <hl>undone</hl> successfully.",
            pos="topCenter",
            fade=True
        )

    # ------------ EXPORT ------------

    def export_layer(self):
        if not self.data.export_path:
            QMessageBox.warning(self, "Export Failed", "No export path set for this layer.")
            return

        if not Path(self.data.export_path).exists():
            QMessageBox.warning(self, "Export Failed", f"Export path does not exist:\n{self.data.export_path}")
            return

        # LEGC path validation
        if self.legc_checkbox.isChecked():
            if not self.data.legc_export_path:
                QMessageBox.warning(self, "Export Failed", "No LEGC export path set for this layer.")
                return
            if not Path(self.data.legc_export_path).exists():
                QMessageBox.warning(self, "Export Failed", f"LEGC export path does not exist:\n{self.data.legc_export_path}")
                return

        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True)
        members = [obj for obj in members if cmds.nodeType(obj) == "transform"]
        if not members:
            QMessageBox.warning(self, "Export Failed", f"No objects found in layer {self.data.maya_layer_name}.")
            return

        previous_selection = cmds.ls(selection=True)
        original_positions = self._move_to_origin(members) if self.data.use_origin else {}

        legc_ran = False
        try:
            if self.legc_checkbox.isChecked():
                # Run LEGC and capture state for restoration
                legc_ran = True
                self.data.legc_applied = True
                print(f"Emitting legc_state_changed: {self.data.uuid}, True")
                self.legc_state_changed.emit(self.data.uuid, True)
                legc_result = self._run_legc(members)
                valid_shapes = legc_result.get("valid_shapes", [])
                valid_transforms = legc_result.get("valid_transforms", [])
                original_shading_groups = legc_result.get("original_shading_groups", {})

                # LEGC export
                cmds.select(members)
                legc_export_path = f"{self.data.legc_export_path}/{self.data.maya_layer_name}_LEGC.fbx"
                cmds.file(legc_export_path, force=True, options="v=0;smoothingGroups=1", type="FBX export", exportSelected=True)

                # Restore original materials
                self._restore_shading_groups(original_shading_groups)

                # Restore UV order: map1 on top, uvSet1 below, map1 as current
                for shape in valid_shapes:
                    if cmds.objExists(shape):
                        existing_uvsets = cmds.polyUVSet(shape, q=True, allUVSets=True) or []
                        if "uvSet1" in existing_uvsets and "map1" in existing_uvsets:
                            mel.eval(f'polyUVSet -reorder -uvSet "map1" -newUVSet "uvSet1" {shape};')
                        cmds.polyUVSet(shape, currentUVSet=True, uvSet="map1")

                # Freeze and delete history again after UV restore
                if valid_transforms:
                    existing_transforms = [t for t in valid_transforms if cmds.objExists(t)]
                    if existing_transforms:
                        cmds.makeIdentity(existing_transforms, apply=True, translate=True, rotate=True, scale=True, normal=False)
                        cmds.delete(existing_transforms, constructionHistory=True)

            # Regular export
            cmds.select(members)
            export_path = f"{self.data.export_path}/{self.data.maya_layer_name}.fbx"
            cmds.file(export_path, force=True, options="v=0;smoothingGroups=1", type="FBX export", exportSelected=True)
            cmds.inViewMessage(amg='LEGC and Regular FBX files exported <hl>successfully</hl>.', pos='topCenter', fade=True)

        finally:
            if original_positions:
                self._restore_positions(original_positions)
            if previous_selection:
                cmds.select(previous_selection)
            else:
                cmds.select(clear=True)
            self.legc_checkbox.setChecked(False)
            if legc_ran:
                self.legc_checkbox.setVisible(False)
                self.legc_undo_label.setVisible(True)
                self.legc_undo_button.setVisible(True)

            # Reset LEGC checkbox after export regardless of success or failure
            self.legc_checkbox.setChecked(False)

    # ------------ COLOR ------------

    def pick_color(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return

        hex_color = color.name()
        rgb = hex_to_rgb(hex_color)
        self.data.color_rgb = rgb

        cmds.setAttr(f"{self.data.maya_layer_name}.overrideRGBColors", 1)
        cmds.setAttr(f"{self.data.maya_layer_name}.overrideColorRGB", rgb[0], rgb[1], rgb[2])

        self.apply_color_styles()

    def apply_color_styles(self):
        hex_color = rgb_to_hex(self.data.color_rgb)
        self.color_button.setStyleSheet(f"background-color: {hex_color};")

        bg_rgb = shifted_background_color(self.data.color_rgb)
        bg_hex = rgb_to_hex(bg_rgb)

        self.setStyleSheet(f"""
            LayerWidget {{
                background-color: {bg_hex};
            }}
            LayerWidget[selected=true] {{
                background-color: {bg_hex};
                border: 2px solid white;
            }}
        """)

    # ------------ DRAG ------------

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.exec(Qt.MoveAction)  # TODO: Implement drag-to-reorder