# ---------- IMPORT LIBRARIES/MODULES ----------

from typing import Optional, Union
from pathlib import Path
import colorsys
import sys
import json
import base64

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as mixin

import shiboken6 as shib
from shiboken6 import wrapInstance # Wraps C++ in Python wrapper

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QSize, Signal, QMimeData
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                               QLabel, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QPushButton, QRadioButton, QButtonGroup, QCheckBox,
                               QMenu, QToolBar, QComboBox, QSizePolicy, QFrame, QSpacerItem,
                               QColorDialog, QLineEdit, QFileDialog, QToolButton)
from PySide6.QtGui import QIcon, QFont, QPixmap, QDrag

# ---------- SETUP CONSTANTS ----------

# Directories
ICON_DIR = r"C:\Users\Public\Repos\VFSTools-for-Maya\icons"

# Maya Icons (Extract them from Maya and copy them to the custom icons folder as PySide requires a path)
LAYER_UP = ICON_DIR + r'\moveLayerUp.png'
LAYER_DOWN = ICON_DIR + r'\moveLayerDown.png'
LAYER_NEW = ICON_DIR + r'\newLayerEmpty.png'
LAYER_ADD = ICON_DIR + r'\newLayerSelected.png'
LAYER_DELETE = ICON_DIR + r'\delete.png' # Could also use deleteActive.png (seems bigger)
LAYER_VISIBLE = ICON_DIR + r'\visible.png'
GONK = ICON_DIR + r'\gonk.png'

# ---------- SETUP METHODS ----------

# Shiboken MainWindow Wrapper
def get_main_window() -> QtWidgets.QWidget:
    ptr = omui.MQtUtil.mainWindow() # Pointer to the Maya main window (Swig Object of type 'QWidget *' at 0x000002244EC30FF0)
    return wrapInstance(int(ptr), QtWidgets.QWidget) # Convert the pointer to an int (get only the address), feed the Python type for the C++ obj

def browser_file_dialog(*args):
    # open new window with file dialog for that layer
    cmds.fileDialog2(dialogStyle=2, fileMode=3, okCaption="Select Folder")

def save_layer_path_to_file(*args):
    # save the file dialog path to file
    # will probably save it to the userPrefs. Alternatively, save it to the maya file but make it user specific?.
    pass
    
def hex_to_rgb(value):
    # Remove the '#' if it exists
    value = value.lstrip('#')
    rgb_255 = tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    rgb_01 = tuple(v / 255.0 for v in rgb_255)
    return rgb_01


# ---------- CREATE LAYER MANAGER ----------

class LayerManager(QWidget):
    def __init__(self):
        super().__init__()
        self.vfs_layers = []
        self.maya_layers = []
    
    def LoadInfo(self):
        # Read all Maya layers and add them to list
        maya_layer_ls = cmds.ls(type="displayLayer")
        self.maya_layers = [layer for layer in maya_layer_ls if layer != "defaultLayer"]

        # Read all VFS layers if they exist
        try:
            raw_data = cmds.fileInfo("VFSLayers", q=True)[0]
            loaded_data = json.loads(raw_data)
            for data in loaded_data:
                self.vfs_layers.append(data)
            
        except:
            print("ACKTSHUALLY, this fileInfo thing doesn't exist, Buddy :/")


    def SyncInfo(self):

        # Make UUID : LayerObj dictionaries of the VFS Layers and the Maya Layers
        vfs_layers_dict = {
            vfs_layer.layerIDNumber: vfs_layer
            for vfs_layer in self.vfs_layers
        }

        maya_layers_dict = {
            cmds.ls(maya_layers, uuid=True)[0]: maya_layers
            for maya_layer in self.maya_layers
        }

        # Get only keys and make them into a set for easier matching
        vfs_layers_ids = set(vfs_layers_dict.keys())
        maya_layers_ids = set(maya_layers_dict.keys())

        # Sync matching layers
        for layer_id in maya_layers_ids & vfs_layers_ids:

            # Get Maya layer with that id, get VFS with the SAME id, update the VFS one accordingly
            maya_layer = maya_layers_dict[layer_id]
            vfs_layer = vfs_layers_dict[layer_id]

            self.UpdateInfo(vfs_layer, maya_layer)

        # Create new VFS layers if there are new Maya layers
        for layer_id in maya_layers_ids - vfs_layers_ids:

            maya_layer = maya_layers_dict[layer_id]

            self.createVFSLayer(True, maya_layer)

        # Delete VFS layers if they were deleted in Maya
        for layer_id in vfs_layers_ids - maya_layers_ids:

            vfs_layer = vfs_layers_dict[layer_id]

            self.RemoveVFSLayer(vfs_layer) # Kill VFS Layer UI
            self.vfs_layers.remove(vfs_layer) # Remove VFS Layer from vfs_layers list
            vfs_layers_ids.remove(vfs_layer._id) # Remove VFS Layer ID from vfs_layers_ids set 

    def UpdateInfo(self, vfsLayer, mayaLayer):
        vfsLayer.visibility = mayaLayer.visibility
        vfsLayer.displayType = mayaLayer.displayType
        vfsLayer.overrideColorRGB = mayaLayer.overrideColorRGB
        vfsLayer.displayOrder = mayaLayer.displayOrder

    def SaveInfo(self):
        VFSLayersVar = {}

        for _layer in self.vfs_layers:
            layer_info = {
                "name" : _layer,
                "color" : "Red",
                "visibility" : True ,
                "sm" : False,
                "ucx" : False,
                "singMult" : "Single",
                "origin" : True,
                "path" : "Meow",
                }
            json_str = json.dumps(layer_info)
            VFSLayersVar[f"{_layer.layerIDNumber}"] = json_str
        
        cmds.fileInfo("VFSLayers", VFSLayersVar)

    def CreateVFSLayer(self, isEmpty, layerName="Layer"):
        # Add Children param
        newMayaLayer = cmds.createDisplayLayer(e=isEmpty, n=layerName, mc=True)
        newLayerID = cmds.ls(newMayaLayer, uuid=True)[0]
        newLayer = BaseLayer(newMayaLayer, newLayerID)
        self.master_layer_layout.addWidget(newLayer, alignment=Qt.AlignmentFlag.AlignTop)
        self.maya_layers.append(newMayaLayer)
        self.vfs_layers.append(newLayer)

    def RemoveVFSLayer(self, layer):
        # TODO: Add a confirmation window before deleting
        cmds.delete(layer)

# ---------- CREATE DRAGGABLE QWIDGET FOR LAYERS ----------

class BaseLayer(QWidget):
    def __init__(self, baseLayerName="Layer", _id="0"):
        super().__init__()
        # Set general settings
        self.setFixedHeight(45)
        self.layerLayout = QHBoxLayout(self)
        self.setAttribute(Qt.WA_StyledBackground, True) # Allow background color to be changed
        
        # Maya Layer attributes
        # DEFAULT: Visible, regular display type, white color, at the bottom
        self.layerIDNumber = _id
        self.visibility = True
        self.displayType = 0
        self.overrideColorRGB = [1.0, 1.0, 1.0]
        self.displayOrder = "1"

        # Add widgets
        self.layerColorButton = QPushButton()
        self.layerColorButton.clicked.connect(self.call_color_picker)
        self.layerNameEdit = QLineEdit(text=baseLayerName)
        self.layerSelectAllButton = QPushButton(text="Select All")
        self.layerVisibilityCheckbox = QCheckBox(text="Vis")
        self.layerSMCheckbox = QCheckBox(text="SM")
        self.layerUCXCheckbox = QCheckBox(text="UCX")
        self.layerExportDropdown = QComboBox()
        self.layerExportDropdown.addItems(['Single File', 'Multiple File'])
        self.layerOriginCheckbox = QCheckBox(text="Origin")
        self.layerPathBrowser = QPushButton(text="...")
        self.layerPathBrowser.clicked.connect(browser_file_dialog)
        self.layerExportButton = QPushButton(text="Export")

        # Connect widgets
        self.layerLayout.addWidget(self.layerColorButton)
        self.layerLayout.addWidget(self.layerNameEdit)
        self.layerLayout.addWidget(self.layerSelectAllButton)
        self.layerLayout.addWidget(self.layerVisibilityCheckbox)
        self.layerLayout.addWidget(self.layerSMCheckbox)
        self.layerLayout.addWidget(self.layerUCXCheckbox)
        self.layerLayout.addWidget(self.layerExportDropdown)
        self.layerLayout.addWidget(self.layerOriginCheckbox)
        self.layerLayout.addWidget(self.layerPathBrowser)
        self.layerLayout.addWidget(self.layerExportButton)
    
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)
    
    def change_layer_color(self, rgb_color):
        # TODO: Replace with actual UI value later
        layer_name = "layer1"

        if not cmds.objExists(layer_name):
            print("Layer does not exist:", layer_name)
            return

        # Enable RGB mode
        cmds.setAttr("%s.overrideRGBColors" %layer_name, 1)

        # Apply color (0–1 range)
        cmds.setAttr("%s.overrideColorRGB" %layer_name, rgb_color[0], rgb_color[1], rgb_color[2])

    def call_color_picker(self):
        # Use preexisting QColorDialog's getColor() method
        new_color = QColorDialog.getColor()
    
        if new_color.isValid():
            # Get hex string (#X0X0X0) to set the StyleSheet
            hex_color = new_color.name()

            # Set button BG color using the hext string
            self.layerColorButton.setStyleSheet("background-color: %s;" %hex_color)
            
            # Convert the hex to RGB (0–1 range) to set the layer outlines color in Maya
            rgb_color = hex_to_rgb(hex_color)

            # Apply the RBG color to Maya layer outlines
            self.change_layer_color(rgb_color)

            # Convert the RGB01 to HSV to check the value to see if we can set the widget bg color to a slightly different shade
            hsv_color = colorsys.rgb_to_hsv(rgb_color[0], rgb_color[1], rgb_color[2])

            # Do the value check (doing it at 50% value)
            shifted_rgb = []
            if (hsv_color[2] > .5):
                for value in rgb_color:
                    value = value * 0.5
                    if (value < 0):
                        value = 0
                    shifted_rgb.append(value)
            else:
                for value in rgb_color:
                    if (value <= 0):
                        value = .075
                    value = value * 1.5
                    if (value > 1):
                        value = 1
                    shifted_rgb.append(value)

            shifted_hex = []
            for value in shifted_rgb:
                value = int(value * 255)
                shifted_hex.append(value)
                
            shifted_hex = '#{:02x}{:02x}{:02x}'.format(shifted_hex[0], shifted_hex[1], shifted_hex[2])
            print("HEX: " + str(hex_color))
            print("RGB: " + str(rgb_color))
            print("HSV: " + str(hsv_color))
            print("SHIFTED RGB: " + str(shifted_rgb))
            print("SHIFTED HEX: " + str(shifted_hex))

            self.setStyleSheet("background-color: %s;" %shifted_hex)
            self.layerExportDropdown.setStyleSheet("border: 1px solid lightgray;")

        else:
            print("Invalid Color!")


# ---------- CREATE THE MAIN WINDOW ----------

class MainWindow(mixin, QtWidgets.QWidget):
    # Setup unique identifier as it is required by workspaceControl 
    UI_OBJECT_NAME = "LayerToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):

        # Delete any existing instances to avoid conflict
        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")
        
        super().__init__(get_main_window() if not parent else parent)

        # Setup draggable functionality
        self.setAcceptDrops(True)

        # Setup general settings
        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("VFS Layer Tools")

        # Setup layout
        self.window_layout = QVBoxLayout(self)
        self.window_layout.setSpacing(0)

        # Add Widgets
        self.top_menu = QToolBar()
        self.master_layer = QWidget()
        self.window_layout.addWidget(self.top_menu)
        self.window_layout.addWidget(self.master_layer)
        
        # Setup each widget
        self.top_menu_setup()
        self.layer_setup()

        self.initUI()

    def initUI(self):
        super(MainWindow, self).show(dockable=True)
        cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", e=True)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        self.master_layer_layout.removeWidget(widget)

        for n in range(self.master_layer_layout.count()):
            # Get the widget at each index in turn.
            w = self.master_layer_layout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2:
                # We didn't drag past this widget.
                # insert to the left of it.
                break
        else:
            # We aren't on the left hand side of any widget,
            # so we're at the end. Increment 1 to insert after.
            n += 1

        self.master_layer_layout.insertWidget(n, widget)

        e.accept()

    def top_menu_setup(self):
        # create local object toolbar and make it the same as the self.top_menu QToolBar widget
        toolbar = self.top_menu
        toolbar.setIconSize(QSize(20, 20))

        # Spacer so all menu buttons are on the top right instead of top left
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        move_layer_up = toolbar.addAction(QIcon(LAYER_UP), "")
        move_layer_down = toolbar.addAction(QIcon(LAYER_DOWN), "")
        new_layer = toolbar.addAction(QIcon(LAYER_NEW), "")
        add_layer = toolbar.addAction(QIcon(LAYER_ADD), "")
        delete_layer = toolbar.addAction(QIcon(LAYER_DELETE), "")

        move_layer_up.triggered.connect(lambda: mel.eval("layerEditorMoveDisplayLayer 1;"))
        move_layer_down.triggered.connect(lambda: mel.eval("layerEditorMoveDisplayLayer 0;"))
        new_layer.triggered.connect(lambda: self.VFS(True))
        add_layer.triggered.connect(lambda: self.VFS(False))
        delete_layer.triggered.connect(lambda: print("DELETING WHATEVER LAYER THIS IS!!!!!"))

    def layer_setup(self):
        self.master_layer_layout = QVBoxLayout()
        self.windowLayerManager = LayerManager()
        self.master_layer_layout.addWidget(self.windowLayerManager)
        button1 = QPushButton()
        button2 = QPushButton()
        button3 = QPushButton()
        self.master_layer_layout.addWidget(button1)
        self.master_layer_layout.addWidget(button2)
        self.master_layer_layout.addWidget(button3)


def main():
    MainWindow()

if __name__ == "__main__":
    main()