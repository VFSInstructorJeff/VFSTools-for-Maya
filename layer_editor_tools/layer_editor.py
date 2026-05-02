# ---------- IMPORT LIBRARIES/MODULES ----------

from typing import Optional, Union
from pathlib import Path
import sys

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as mixin

import shiboken6 as shib
from shiboken6 import wrapInstance # Wraps C++ in Python wrapper

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                               QLabel, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QPushButton, QRadioButton, QButtonGroup, QCheckBox,
                               QMenu, QToolBar, QComboBox, QSizePolicy, QFrame, QSpacerItem,
                               QColorDialog, QLineEdit, QFileDialog, QToolButton)
from PySide6.QtGui import QIcon, QFont, QPixmap

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

def edit_layer_name(*args):
    # Allow user to double click the Layer Name to edit it
    # Make it a QLabel that can't be edited
    # On double click, make it a QLineEdit (?)
    # On Enter or on click outside, make that a QLabel again with the new value
    # call rename_objs()
    pass

def rename_objs(*args):
    # Rename all objs if layer has been renamed
    pass

def select_all(*args):
    # Select all meshes in layer (can probably steal the Maya command for this)
    pass

def set_visibility(*args):
    # hide/unhide, can prob steal from Maya
    pass

def select_static_meshes(*args):
    # select all meshes in the layer that dont contain the UCX prefix
    pass

def select_ucx(*args):
    # select all meshes in the layer that contain the UCX prefix
    pass

def export_single_file(*args):
    # export everything in the layer as a single FBX file.
    # Check move to origin? If so, move the entire thing to origin?
    # remember to unparent stuff from parent group so parent doesn't get exported with selection
    pass

def export_multiple_files(*args):
    # export everything individually in FBX files
    # Check move to origin
    # remember to unparent stuff from parent group so parent doesn't get exported with selection
    pass

def set_up_axis(*args):
    # Set up axis Y or Z (maybe use Unity vs Unreal language instead of Y/Z?)
    pass

def move_to_origin(*args):
    # move rotation and transf to 0
    pass

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


# ---------- CREATE THE MAIN WINDOW ----------


class MainWindow(mixin, QtWidgets.QWidget):
    # Setup unique identifier as it is required by workspaceControl 
    UI_OBJECT_NAME = "LayerToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):

        # Delete any existing instances to avoid conflict
        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")
        
        super().__init__(get_main_window() if not parent else parent)

        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("VFS Layer Tools")

        # Create the vertical widget (pass self as parent so the widget is shown)
        self.window_layout = QVBoxLayout(self)   
        # Add a widget to be the top menu, and one to be the Master Layer
        self.top_menu = QToolBar()
        self.master_layer = QWidget()
        self.window_layout.addWidget(self.top_menu)
        self.window_layout.addWidget(self.master_layer)
        # Setup each one of those
        self.top_menu_setup()
        self.master_layer_setup()

        self.initUI()

    def initUI(self):
        super(MainWindow, self).show(dockable=True)
        cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", e=True)

    def call_color_picker(self):
        # Use preexisting QColorDialog's getColor() method
        new_color = QColorDialog.getColor(parent=self)
    
        if new_color.isValid():
            # Get hex string (#X0X0X0)
            hex_color = new_color.name()

            # Set button BG color
            self.color_display.setStyleSheet("background-color: %s;" %hex_color)

            # Convert the hex to RGB (0–1 range) to set the layer outlines color in Maya
            rgb_color = hex_to_rgb(hex_color)

            # Apply the RBG color to Maya layer
            self.change_layer_color(rgb_color)

        else:
            print("Invalid Color!")

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

    def top_menu_setup(self):
        # create local object toolbar and make it the same as the self.top_menu QToolBar widget
        toolbar = self.top_menu
        toolbar.setIconSize(QSize(20, 20))
        # TODO: CHANGE THIS DISGUSTING COLOR LATER
        toolbar.setStyleSheet("background-color: #fcba03")

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
        new_layer.triggered.connect(lambda: mel.eval("layerEditorCreateLayer 1;"))
        add_layer.triggered.connect(lambda: mel.eval("layerEditorCreateLayer 2;"))
        delete_layer.triggered.connect(lambda: print("DELETING WHATEVER LAYER THIS IS!!!!!"))


        # UPDATING SELECTED LAYERS
        # layerEditorDisplayLayerManagerChange;
        # updateCurrentDisplayLayer layerManager.currentDisplayLayer;
        
        # DELETING LAYERS
        # layerEditorDeleteLayer layer11;
        # delete layer11; 

    def master_layer_setup(self):
        # Create the tab layout and parent it to the tab widget
        master_layer_layout = QHBoxLayout(self.master_layer)
        self.master_layer.setStyleSheet("background-color: #03fca1")
        self.master_layer.setFixedHeight(40)

        # Make some stuff
        self.color_display = QPushButton()
        self.color_display.clicked.connect(self.call_color_picker)
        layer_name = QLineEdit(text="LayerName")
        select_all_button = QPushButton(text="SelectAll")
        visibility_checkbox = QCheckBox(text="Vis")
        sm_checkbox = QCheckBox(text="SM")
        ucx_checkbox = QCheckBox(text="UCX")
        sf_mf_dropdown = QComboBox()
        sf_mf_dropdown.addItems(['Single File', 'Multiple File'])
        origin_checkbox = QCheckBox(text="Origin")
        path_browser = QPushButton(text="...")
        path_browser.clicked.connect(browser_file_dialog)
        export_button = QPushButton(text="Export")

        # Add stuff to layout
        master_layer_layout.addWidget(self.color_display)
        master_layer_layout.addWidget(layer_name)
        master_layer_layout.addWidget(select_all_button)   
        master_layer_layout.addWidget(visibility_checkbox)   
        master_layer_layout.addWidget(sm_checkbox)   
        master_layer_layout.addWidget(ucx_checkbox)   
        master_layer_layout.addWidget(sf_mf_dropdown)   
        master_layer_layout.addWidget(origin_checkbox)   
        master_layer_layout.addWidget(path_browser)   
        master_layer_layout.addWidget(export_button) 


def main():
    MainWindow()

if __name__ == "__main__":
    main()