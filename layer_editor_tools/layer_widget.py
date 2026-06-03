# ------------ IMPORT LIBRARIES/MODULES ------------
import webbrowser
from pathlib import Path

from maya import cmds, mel

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDrag, QIcon
from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QHBoxLayout,
                                QVBoxLayout, QCheckBox, QComboBox, QColorDialog,
                                QFileDialog, QMessageBox, QMenu, QFrame)

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.utils import hex_to_rgb, rgb_to_hex, shifted_background_color
from layer_editor_tools.constants import VISIBLE, HIDDEN, CONFIG_DROPDOWN, FOLDER_OPEN, BUG_REPORT_URL, HELP, BUG_REPORT

# Layer display types and their labels for the cycling button
LAYER_MODES = ["N", "T", "R"]

# ------------ LAYER WIDGET CLASS ------------

class LayerWidget(QWidget):

    # ------------ SIGNALS ------------
    selected = Signal(object)           # Emitted when the layer is selected
    path_changed = Signal(str, str)     # Emitted when export path changes: uuid, export_path

    def __init__(self, data: VFSLayerData):
        super().__init__()
        self.data = data
        self.setFixedHeight(45)
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

        self.color_button = QPushButton()
        self.color_button.setFixedWidth(20)

        self.name_edit = QLineEdit(self.data.maya_layer_name)

        self.visibility_button = QPushButton(QIcon(VISIBLE), "")
        self.visibility_button.setFixedWidth(24)
        self.visibility_button.setCheckable(True)

        self.mode_button = QPushButton(LAYER_MODES[self.data.display_type])
        self.mode_button.setFixedWidth(24)

        self.export_toggle = QPushButton(QIcon(CONFIG_DROPDOWN), "")
        self.export_toggle.setFixedWidth(24)
        self.export_toggle.setCheckable(True)

        self.export_button = QPushButton("Export")
        self.export_button.setFixedWidth(60)

        self.top_layout.addWidget(self.color_button)
        self.top_layout.addWidget(self.name_edit)
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

        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)
        self.path_edit.setPlaceholderText("No export path set")

        self.export_dropdown = QComboBox()
        self.export_dropdown.addItems(["Single File", "Multiple File"])
        self.export_dropdown.setFixedWidth(100)

        self.origin_checkbox = QCheckBox("Origin")

        self.bottom_layout.addWidget(self.path_button)
        self.bottom_layout.addWidget(self.path_edit)
        self.bottom_layout.addWidget(self.export_dropdown)
        self.bottom_layout.addWidget(self.origin_checkbox)

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
        self.export_dropdown.setCurrentText(self.data.export_mode)

        if self.data.export_path:
            self.path_edit.setText(self.data.export_path)
            self.export_toggle.setChecked(True)
            self.toggle_export_row(True)

        self.apply_color_styles()

    def connect_signals(self):
        self.color_button.clicked.connect(self.pick_color)
        self.name_edit.editingFinished.connect(self.rename_layer)
        self.visibility_button.toggled.connect(self.on_visibility_changed)
        self.mode_button.clicked.connect(self.cycle_layer_mode)
        self.export_toggle.toggled.connect(self.toggle_export_row)
        self.export_button.clicked.connect(self.export_layer)
        self.path_button.clicked.connect(self.pick_export_path)
        self.export_dropdown.currentTextChanged.connect(self.on_export_mode_changed)
        self.origin_checkbox.toggled.connect(self.on_origin_changed)

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
        self.setFixedHeight(75 if checked else 45)

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
        mel.eval("updateLayerEditor();")

    def on_export_mode_changed(self, text):
        self.data.export_mode = text

    def on_origin_changed(self, state):
        self.data.use_origin = state

    def rename_layer(self):
        new_name = self.name_edit.text()
        if not cmds.objExists(self.data.maya_layer_name):
            return
        new_layer_name = cmds.rename(self.data.maya_layer_name, new_name)
        self.data.maya_layer_name = new_layer_name

    # ------------ CONTEXT MENU ACTIONS ------------

    def select_all(self):
        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True) or []
        all_objects = []
        for obj in members:
            all_objects.append(obj)
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
                    # Only include if it has a shape as a direct child
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
        # Moving objects to defaultLayer effectively removes them from the current layer
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
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Export Folder",
            self.data.export_path or ""
        )
        if path:
            self.data.export_path = path
            self.path_edit.setText(path)
            self.path_changed.emit(self.data.uuid, path)

    # ------------ EXPORT ------------

    def _move_to_origin(self, members):
        """Move each object to (0,0,0) and return their original positions."""
        original_positions = {}
        for obj in members:
            pos = cmds.xform(obj, q=True, worldSpace=True, translation=True)
            original_positions[obj] = pos
            cmds.xform(obj, worldSpace=True, translation=(0, 0, 0))
        return original_positions

    def _restore_positions(self, original_positions):
        """Restore each object to its original position."""
        for obj, pos in original_positions.items():
            if cmds.objExists(obj):
                cmds.xform(obj, worldSpace=True, translation=pos)

    def export_layer(self):
        if not self.data.export_path:
            QMessageBox.warning(self, "Export Failed", "No export path set for this layer.")
            return

        if not Path(self.data.export_path).exists():
            QMessageBox.warning(self, "Export Failed", f"Export path does not exist:\n{self.data.export_path}")
            return

        members = cmds.editDisplayLayerMembers(self.data.maya_layer_name, q=True, fullNames=True)
        members = [obj for obj in members if cmds.nodeType(obj) == "transform"]
        if not members:
            QMessageBox.warning(self, "Export Failed", f"No objects found in layer {self.data.maya_layer_name}.")
            return

        previous_selection = cmds.ls(selection=True)
        original_positions = self._move_to_origin(members) if self.data.use_origin else {}

        try:
            if self.data.export_mode == "Single File":
                cmds.select(members)
                export_path = f"{self.data.export_path}/{self.data.maya_layer_name}.fbx"
                cmds.file(export_path, force=True, options="v=0", type="FBX export", exportSelected=True)

            elif self.data.export_mode == "Multiple File":
                for obj in members:
                    cmds.select(obj)
                    export_path = f"{self.data.export_path}/{obj}.fbx"
                    cmds.file(export_path, force=True, options="v=0", type="FBX export", exportSelected=True)

        finally:
            if original_positions:
                self._restore_positions(original_positions)
            if previous_selection:
                cmds.select(previous_selection)
            else:
                cmds.select(clear=True)

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
            drag.exec(Qt.MoveAction)