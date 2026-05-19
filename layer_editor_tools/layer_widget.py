from maya import cmds, mel

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QHBoxLayout,
                                QVBoxLayout, QCheckBox, QComboBox, QColorDialog,
                                QFileDialog)

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.utils import hex_to_rgb, rgb_to_hex, shifted_background_color


class LayerWidget(QWidget):

    selected = Signal(object)

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

    # ------------ SETUP UI ------------

    def build_ui(self):
        # Top row — all controls
        self.controls_row = QWidget()
        self.layout = QHBoxLayout(self.controls_row)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.color_button = QPushButton()
        self.name_edit = QLineEdit(self.data.maya_layer_name)
        self.visibility_checkbox = QCheckBox("Vis")
        self.sm_checkbox = QCheckBox("SM")
        self.ucx_checkbox = QCheckBox("UCX")
        self.export_dropdown = QComboBox()
        self.export_dropdown.addItems(["Single File", "Multiple File"])
        self.origin_checkbox = QCheckBox("Origin")
        self.path_button = QPushButton("...")
        self.export_button = QPushButton("Export")
        self.path_toggle = QPushButton("▶")
        self.path_toggle.setFixedWidth(16)
        self.path_toggle.setCheckable(True)

        self.layout.addWidget(self.color_button)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.visibility_checkbox)
        self.layout.addWidget(self.sm_checkbox)
        self.layout.addWidget(self.ucx_checkbox)
        self.layout.addWidget(self.export_dropdown)
        self.layout.addWidget(self.origin_checkbox)
        self.layout.addWidget(self.path_button)
        self.layout.addWidget(self.export_button)
        self.layout.addWidget(self.path_toggle)

        # Bottom row — export path display, hidden by default
        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)
        self.path_edit.setPlaceholderText("No export path set")
        self.path_edit.setFixedHeight(16)
        self.path_edit.setStyleSheet(
            "font-size: 9px; background: transparent; border: none; color: grey;"
        )
        self.path_edit.setVisible(False)

        self.main_layout.addWidget(self.controls_row)
        self.main_layout.addWidget(self.path_edit)

    def populate_ui(self):
        self.visibility_checkbox.setChecked(self.data.visibility)
        self.sm_checkbox.setChecked(self.data.select_sm)
        self.ucx_checkbox.setChecked(self.data.select_ucx)
        self.origin_checkbox.setChecked(self.data.use_origin)
        self.export_dropdown.setCurrentText(self.data.export_mode)
        if self.data.export_path:
            self.path_edit.setText(self.data.export_path)
        self.apply_color_styles()

    def connect_signals(self):
        self.color_button.clicked.connect(self.pick_color)
        self.visibility_checkbox.toggled.connect(self.on_visibility_changed)
        self.sm_checkbox.toggled.connect(self.on_sm_changed)
        self.ucx_checkbox.toggled.connect(self.on_ucx_changed)
        self.origin_checkbox.toggled.connect(self.on_origin_changed)
        self.export_dropdown.currentTextChanged.connect(self.on_export_mode_changed)
        self.name_edit.editingFinished.connect(self.rename_layer)
        self.path_button.clicked.connect(self.pick_export_path)
        self.path_toggle.toggled.connect(self.toggle_path_row)

    # -----------------------------
    # Selection
    # -----------------------------

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selected.emit(self)
        super().mousePressEvent(event)

    def set_selected(self, is_selected: bool):
        """Toggle visual selected state. Style via LayerWidget[selected='true'] in stylesheet."""
        self.setProperty("selected", is_selected)
        self.style().unpolish(self)
        self.style().polish(self)

    # -----------------------------
    # Path Row Toggle
    # -----------------------------

    def toggle_path_row(self, checked):
        self.path_edit.setVisible(checked)
        self.path_toggle.setText("▼" if checked else "▶")
        self.setFixedHeight(75 if checked else 45)

    # -----------------------------
    # Maya Updates
    # -----------------------------

    def on_visibility_changed(self, state):
        self.data.visibility = state
        cmds.setAttr(f"{self.data.maya_layer_name}.visibility", state)
        mel.eval("updateLayerEditor();")

    def on_sm_changed(self, state):
        self.data.select_sm = state
        # TODO: Add logic to display only static meshes, no UCX

    def on_ucx_changed(self, state):
        self.data.select_ucx = state
        # TODO: Add logic to display only meshes that start with UCX_, no regular meshes

    def on_origin_changed(self, state):
        self.data.use_origin = state

    def on_export_mode_changed(self, text):
        self.data.export_mode = text

    def rename_layer(self):
        new_name = self.name_edit.text()

        if not cmds.objExists(self.data.maya_layer_name):
            return

        new_layer_name = cmds.rename(self.data.maya_layer_name, new_name)
        self.data.maya_layer_name = new_layer_name

    # -----------------------------
    # Export Path
    # -----------------------------

    def pick_export_path(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Export Folder",
            self.data.export_path or ""
        )

        if path:
            self.data.export_path = path
            self.path_edit.setText(path)

    # -----------------------------
    # Color
    # -----------------------------

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

    # -----------------------------
    # Drag
    # -----------------------------

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.exec(Qt.MoveAction)