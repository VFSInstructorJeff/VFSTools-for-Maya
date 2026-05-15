from maya import cmds

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import ( QWidget,
                                QPushButton,
                                QLineEdit,
                                QHBoxLayout,
                                QCheckBox,
                                QComboBox,
                                QColorDialog )

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.utils import (  hex_to_rgb,
                                        rgb_to_hex,
                                        shifted_background_color )


class LayerWidget(QWidget):
    deleted = Signal(object)

    def __init__(self, data: VFSLayerData):
        super().__init__()
        self.data = data
        self.setFixedHeight(45)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout = QHBoxLayout(self)
        self.build_ui()
        self.populate_ui()
        self.connect_signals()


    # ------------ SETUP UI ------------


    def build_ui(self):
        # Create widgets
        self.color_button = QPushButton()
        self.name_edit = QLineEdit(self.data.maya_layer_name)
        self.visibility_checkbox = QCheckBox("Vis")
        self.sm_checkbox = QCheckBox("SM")
        self.ucx_checkbox = QCheckBox("UCX")
        self.export_dropdown = QComboBox()
        self.export_dropdown.addItems([ "Single File",
                                        "Multiple File" ])
        self.origin_checkbox = QCheckBox("Origin")
        self.path_button = QPushButton("...")
        self.export_button = QPushButton("Export")
        self.delete_button = QPushButton("X")

        # Add widgets to layout
        self.layout.addWidget(self.color_button)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.visibility_checkbox)
        self.layout.addWidget(self.sm_checkbox)
        self.layout.addWidget(self.ucx_checkbox)
        self.layout.addWidget(self.export_dropdown)
        self.layout.addWidget(self.origin_checkbox)
        self.layout.addWidget(self.path_button)
        self.layout.addWidget(self.export_button)
        self.layout.addWidget(self.delete_button)

    def populate_ui(self):
        # Make UI reflect layer data
        self.visibility_checkbox.setChecked(self.data.visibility)
        self.sm_checkbox.setChecked(self.data.is_sm)
        self.ucx_checkbox.setChecked(self.data.is_ucx)
        self.origin_checkbox.setChecked(self.data.use_origin)
        self.export_dropdown.setCurrentText(self.data.export_mode)
        self.apply_color_styles()

    def connect_signals(self):
        self.color_button.clicked.connect(self.pick_color)
        self.visibility_checkbox.toggled.connect(self.on_visibility_changed)
        self.sm_checkbox.toggled.connect(self.on_sm_changed)
        self.ucx_checkbox.toggled.connect(self.on_ucx_changed)
        self.origin_checkbox.toggled.connect(self.on_origin_changed)
        self.export_dropdown.currentTextChanged.connect(self.on_export_mode_changed)
        self.name_edit.editingFinished.connect(self.rename_layer)
        self.delete_button.clicked.connect(lambda: self.deleted.emit(self))

    # -----------------------------
    # Maya Updates
    # -----------------------------

    def on_visibility_changed(self, state):
        self.data.visibility = state
        cmds.setAttr(f"{self.data.maya_layer_name}.visibility", state)

    def on_sm_changed(self, state):
        self.data.is_sm = state
        # TODO: Add logic to display only static meshes, no UCX

    def on_ucx_changed(self, state):
        self.data.is_ucx = state
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
    # Color
    # -----------------------------

    def pick_color(self):
        # Get user selected color
        color = QColorDialog.getColor()

        # If it's not valid, return
        if not color.isValid():
            return

        # Convert Hex to RGB 0-1
        hex_color = color.name()    # a0a0a0)
        rgb = hex_to_rgb(hex_color) # 0.1, 0.1, 0.1
        self.data.color_rgb = rgb

        # Set the color of the outline of the objects in the layer
        cmds.setAttr(f"{self.data.maya_layer_name}.overrideRGBColors", 1)
        cmds.setAttr(f"{self.data.maya_layer_name}.overrideColorRGB", rgb[0], rgb[1], rgb[2])

        self.apply_color_styles()

    def apply_color_styles(self):
        # Convert RGB 0-1 back to Hex
        hex_color = rgb_to_hex(self.data.color_rgb)

        # Use the hex to set the color of the color button itself
        self.color_button.setStyleSheet(f"background-color: {hex_color};")

        # Shift the RGB color to a darker/lighter shade so the background of the layer widget is coloured but doesn't blend with the button, switch it to Hex again
        bg_rgb = shifted_background_color(self.data.color_rgb)
        bg_hex = rgb_to_hex(bg_rgb)

        self.setStyleSheet(f"background-color: {bg_hex};")

    # -----------------------------
    # Drag
    # -----------------------------

    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.exec(Qt.MoveAction)