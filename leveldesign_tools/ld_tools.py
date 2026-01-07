# ---------- IMPORT LIBRARIES/MODULES ----------

from typing import Optional, Union
from pathlib import Path
import sys

from maya import cmds
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as mixin

import shiboken6 as shib
from shiboken6 import wrapInstance # Wraps C++ in Python wrapper

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                               QLabel, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QPushButton, QRadioButton, QButtonGroup, QCheckBox,
                               QMenu, QToolBar, QComboBox, QSizePolicy)
from PySide6.QtGui import QIcon, QFont, QPixmap


# ---------- SETUP CONSTANTS ----------


# Colors
ORANGE = (0.247, 0.148, 0.029)
BLUE = (0.321, 0.521, 0.650) # Maya blue
LIGHTER_GRAY = (0.360, 0.360, 0.360) # Maya standard button light gray color
LIGHT_GRAY = (0.265, 0.265, 0.265) # Maya light gray
DARK_GRAY = (0.185, 0.185, 0.185) # Maya dark gray
MAGENTA = (0.200, 0.076, 0.228) # For debugging

# Directories
CURRENT_DIR = Path(__file__).parent # (...\Documents\maya\scripts\vfs_leveldesign_tools\)
ICON_DIR = str(CURRENT_DIR) + r"\icons"

# Maya Icons (Extract them from Maya and copy them to the custom icons folder as PySide requires a path)
CUBE = ICON_DIR + r'\polyCube.png'
CYLINDER = ICON_DIR + r'\polyCylinder.png'
SPHERE = ICON_DIR + r'\polySphere.png'
CONE = ICON_DIR + r'\polyCone.png'
TORUS = ICON_DIR + r'\polyTorus.png'
TYPE = ICON_DIR + r'\text.png'
COMBINE = ICON_DIR + r'\polyUnite.png'
SEPARATE = ICON_DIR + r'\polySeparate.png'
CENTER_PIVOT = ICON_DIR + r'\CenterPivot.png'
KILL_HIST = ICON_DIR + r'\DeleteHistory.png'
FREEZE = ICON_DIR + r'\FreezeTransform.png'
BOOL_DIFF = ICON_DIR + r'\polyBooleansDifference.png'
CIRCLE_CURVE = ICON_DIR + r'\circle.png'
CURVE_TOOL = ICON_DIR + r'\curveEP.png'
INSERT_KNOT = ICON_DIR + r'\insertKnot.png'
SWEEP_MESH = ICON_DIR + r'\polyHelix.png'
GRID = ICON_DIR + r'\Grid.png'
MATERIAL = ICON_DIR + r'\material_assign.png'

# Custom Icons
MAT_FLOOR = ICON_DIR + r'\Floor_grid_32.png'
MAT_WALL1 = ICON_DIR + r'\Wall01_grid_32.png'
MAT_WALL2 = ICON_DIR + r'\Wall02_grid_32.png'
MAT_WALL3 = ICON_DIR + r'\Wall03_grid_32.png'
MAT_WALL4 = ICON_DIR + r'\Wall04_grid_32.png'
MAT_WALL5 = ICON_DIR + r'\Wall05_grid_32.png'
MAT_MISC1 = ICON_DIR + r'\Misc01_grid_32.png'
MAT_MISC2 = ICON_DIR + r'\Misc02_grid_32.png'
MAT_MISC3 = ICON_DIR + r'\Misc03_grid_32.png'
MAT_MISC4 = ICON_DIR + r'\Misc04_grid_32.png'
MAT_MISC5 = ICON_DIR + r'\Misc05_grid_32.png'
MAT_MISC6 = ICON_DIR + r'\Misc06_grid_32.png'
MAT_MISC7 = ICON_DIR + r'\Misc07_grid_32.png'
MAT_MISC8 = ICON_DIR + r'\Misc08_grid_32.png'
MAT_MISC9 = ICON_DIR + r'\Misc09_grid_32.png'


# ---------- SETUP METHODS ----------


# Shiboken MainWindow Wrapper
def get_main_window() -> QtWidgets.QWidget:
    ptr = omui.MQtUtil.mainWindow() # Pointer to the Maya main window (Swig Object of type 'QWidget *' at 0x000002244EC30FF0)
    return wrapInstance(int(ptr), QtWidgets.QWidget) # Convert the pointer to an int (get only the address), feed the Python type for the C++ obj

# Defining Maya functions
global primScale
primScale = 100

def set_prim_scale(primScaleRaw):
    global primScale # Fetch global var
    newprimScale = primScaleRaw[:-2]
    primScale = int(newprimScale) # Set global var

def create_primitive(primTypeRaw):
    primType = primTypeRaw.lower()
    if primType == 'cube':
        createdPrim = cmds.polyCube()
        cmds.scale(primScale, primScale, primScale)
    elif primType == 'cylinder':
        createdPrim = cmds.polyCylinder()
        cmds.scale(primScale, primScale, primScale)
    elif primType == 'sphere':
        createdPrim = cmds.polySphere()
        cmds.scale(primScale, primScale, primScale)
    elif primType == 'cone':
        createdPrim = cmds.polyCone()
        cmds.scale(primScale, primScale, primScale)
    elif primType == 'torus':
        createdPrim = cmds.polyTorus()
        cmds.scale(primScale, primScale, primScale)
    elif primType == 'type':
        createdPrim = cmds.CreatePolygonType()
    else:
        print("Ruh-roh, something went wrong with create_primitive!")

def grid_setup(gridRaw):
    cmds.setAttr('perspShape.farClipPlane', 500000) # 5km
    cmds.setAttr('perspShape.nearClipPlane', 10) # 10cm

    if gridRaw == .5:
        cmds.grid(size = 10000, spacing = 50, divisions = 1) # 100m, grid every 0.5m
        cmds.displayColor('gridAxis', 4, dormant = True)
    if gridRaw == 1:
        cmds.grid(size = 10000, spacing = 100, divisions = 1) # 100m, grid every 1m
        cmds.displayColor('gridAxis', 4, dormant = True)
    if gridRaw == 2:
        cmds.grid(size = 10000, spacing = 200, divisions = 1) # 100m, grid every 2m
        cmds.displayColor('gridAxis', 4, dormant = True)
    if gridRaw == 4:
        cmds.grid(size = 10000, spacing = 400, divisions = 1) # 100m, grid every 4m
        cmds.displayColor('gridAxis', 4, dormant = True)
    else:
        print("Ruh-roh, something went wrong with grid_setup!")

def turn_on_texture():
    perspPanel = cmds.getPanel( withLabel='Persp View')
    frontPanel = cmds.getPanel( withLabel='Front View')
    topPanel = cmds.getPanel( withLabel='Top View')
    sidePanel = cmds.getPanel( withLabel='Side View')
    panel_list = [perspPanel, frontPanel, topPanel, sidePanel]
    
    for each in panel_list:
        cmds.modelEditor(each, edit = True, displayTextures = True)

def set_material(chosenMat):
    selected_objs = cmds.ls(selection = True)
    cmds.sets(selected_objs, edit = True, forceElement = chosenMat)
 
def make_UCX(selectionRaw):
    for each in selectionRaw:
        ucxMesh = cmds.duplicate(each)
        newName = "UCX_" + each
        cmds.rename(ucxMesh, newName)

def combine(*args):
    selected_items = cmds.ls(selection=True)
    parent=cmds.listRelatives(selected_items[0],parent=True)
    extensionless_names = []
    if '_' in selected_items[0]:
        substrings=selected_items[0].split('_')
        last_substring=substrings[-1]
        for item in selected_items:
            result='_'.join(item.split('_')[:-1])
            extensionless_names.append(result)
        extensionless_names.append(last_substring)
        selected_items=extensionless_names
    combination_name="_".join(selected_items)
    cmds.polyUnite(name=combination_name)
    if parent:
        cmds.parent(combination_name,parent,relative=True)
    cmds.select(combination_name, replace=True)
    cmds.CenterPivot()
    cmds.DeleteHistory()
    cmds.FreezeTransformations()

def separate(*args):
    selected_items = cmds.ls(selection=True)
    for item in selected_items:
        combination_name=item
        separated_names=combination_name.split("_")
        separated_nodes=cmds.polySeparate(n=combination_name)
        separated_nodes=separated_nodes[:-1]
        for index, node in enumerate(separated_nodes):
            if len(separated_nodes) < len(separated_names):
                extension=separated_names[-1]
                extension='_'+extension
                separated_names[index]+=extension
            cmds.rename(node,separated_names[index])
            parent_group=cmds.listRelatives(separated_names[index], parent=True)
            parent=cmds.listRelatives(parent_group, parent=True)
            if parent:
                cmds.parent(separated_names[index],parent,relative=True)
            else:
                cmds.parent(separated_names[index], world=True)
        if len(separated_nodes) < len(separated_names):
            separated_names=separated_names[:-1]
        cmds.select(separated_names,replace=True)
        cmds.CenterPivot()
        cmds.DeleteHistory()
        cmds.FreezeTransformations()

def center_pivot(*args):
    cmds.CenterPivot()

def delete_history(*args):
    cmds.DeleteHistory()

def freeze_transformations(*args):
    cmds.FreezeTransformations()

def boolean_difference(*args):
    cmds.PolygonBooleanDifference()

def circle_curve(*args):
    cmds.CreateNURBSCircle()

def curve_tool(*args):
    cmds.EPCurveTool()

def insert_knot(*args):
    cmds.InsertKnot()

def sweep_mesh(*args):
    cmds.CreateSweepMesh


# ---------- CREATE THE MAIN WINDOW ----------


class MainWindow(mixin, QtWidgets.QDialog):
    # Setup unique identifier as it is required by workspaceControl 
    UI_OBJECT_NAME = "LDToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):

        # Delete any existing instances to avoid conflict
        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")
        
        super().__init__(get_main_window() if not parent else parent)

        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("LD Tools")
        self.setFixedSize(500, 500)

        # Create the tab widget (pass self as parent so the widget is shown)
        self.tabs_layout = QTabWidget(self)
        # Create widgets to be the tabs
        self.ldworkflow_tab = QWidget()
        self.modularkit_tab = QWidget()
        # Add the widgets as tabs
        self.tabs_layout.addTab(self.ldworkflow_tab, "LD Workflow")
        self.tabs_layout.addTab(self.modularkit_tab, "Modular Kit")
        # Setup each tab
        self.ldworkflow_tab_setup()
        self.modularkit_tab_setup()

        self.initUI()

    def initUI(self):
        super(MainWindow, self).show(dockable=True)
        cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", e=True)

        self.tabs_layout.setFixedSize(500,500)


    def ldworkflow_tab_setup(self):
        # Create the tab layout and parent it to the tab widget
        ldworkflow_tab_layout = QVBoxLayout(self.ldworkflow_tab)

        # Primitives Layout
        primitives_layout = QGridLayout()
        ldworkflow_tab_layout.addLayout(primitives_layout)

        # Primitives widgets (label, dropdown menu, buttons)
        size_dropdown_label = QLabel("Primitive Scale:")
        size_dropdown = QComboBox()
        size_dropdown.addItems(['50cm', '100cm', '200cm', '400cm'])
        size_dropdown.setCurrentIndex(1)
        button_cube = QPushButton(icon=QIcon(CUBE), text="Cube")
        button_cylinder = QPushButton(icon=QIcon(CYLINDER), text="Cylinder")
        button_sphere = QPushButton(icon=QIcon(SPHERE), text="Sphere")
        button_cone = QPushButton(icon=QIcon(CONE), text="Cone")
        button_torus = QPushButton(icon=QIcon(TORUS), text="Torus")
        button_type = QPushButton(icon=QIcon(TYPE), text="Type")

        # Set icon and button sizes
        primitives_btnarray = {button_cube, button_cylinder, button_sphere,
                               button_cone, button_torus, button_type}
        for btn in primitives_btnarray:
            btn.setIconSize(QSize(64, 64))

        # Connect widgets and methods
        button_cube.clicked.connect(lambda: create_primitive('cube'))
        button_cylinder.clicked.connect(lambda: create_primitive('cylinder'))
        button_sphere.clicked.connect(lambda: create_primitive('sphere'))
        button_cone.clicked.connect(lambda: create_primitive('cone'))
        button_torus.clicked.connect(lambda: create_primitive('torus'))
        button_type.clicked.connect(lambda: create_primitive('type'))
        size_dropdown.currentTextChanged.connect(set_prim_scale)   
        
        # Parent the buttons to the layout
        primitives_layout.addWidget(size_dropdown_label, 0, 0) # widget, row, column
        primitives_layout.addWidget(size_dropdown, 0, 1) 
        primitives_layout.addWidget(button_cube, 1, 0)      
        primitives_layout.addWidget(button_cylinder, 1, 1)
        primitives_layout.addWidget(button_sphere, 1, 2)
        primitives_layout.addWidget(button_cone, 2, 0)
        primitives_layout.addWidget(button_torus, 2, 1)
        primitives_layout.addWidget(button_type, 2, 2)

        # Tools layout
        curve_tools_layout = QHBoxLayout()
        ldworkflow_tab_layout.addLayout(curve_tools_layout)

        # Tools buttons
        button_combine = QPushButton(icon=QIcon(COMBINE))
        button_separate = QPushButton(icon=QIcon(SEPARATE))
        button_centerpivot = QPushButton(icon=QIcon(CENTER_PIVOT))
        button_killhistory = QPushButton(icon=QIcon(KILL_HIST))
        button_freeze = QPushButton(icon=QIcon(FREEZE))
        button_booldiff = QPushButton(icon=QIcon(BOOL_DIFF))
        button_circlecurve = QPushButton(icon=QIcon(CIRCLE_CURVE))
        button_curvetool = QPushButton(icon=QIcon(CURVE_TOOL))
        button_addknot = QPushButton(icon=QIcon(INSERT_KNOT))
        button_sweepmesh = QPushButton(icon=QIcon(SWEEP_MESH))

        # Set icon and button sizes
        tools_btnarray = {button_combine, button_separate, button_centerpivot,
                        button_killhistory, button_freeze, button_booldiff,
                        button_circlecurve, button_curvetool, button_addknot, button_sweepmesh}
        for btn in tools_btnarray:
            btn.setIconSize(QSize(64, 64))
            btn.setMaximumSize(50, 40)

        # Connect buttons and methods
        button_combine.clicked.connect(combine)
        button_separate.clicked.connect(separate)
        button_centerpivot.clicked.connect(center_pivot)
        button_killhistory.clicked.connect(delete_history)
        button_freeze.clicked.connect(freeze_transformations)
        button_booldiff.clicked.connect(boolean_difference)
        button_circlecurve.clicked.connect(circle_curve)
        button_curvetool.clicked.connect(curve_tool)
        button_addknot.clicked.connect(insert_knot)
        button_sweepmesh.clicked.connect(sweep_mesh)
       
        # Parenting widgets to layout
        for btn in tools_btnarray:
            curve_tools_layout.addWidget(btn)

        # Grid Options
        



    def modularkit_tab_setup(self):
        pass

    def checkbox_changed(self, state):
        print(state)
        if state == 2:
            print("You like food")
        else:
            print("You don't like food")

    def on_click(self):
        print("button clicked :D")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Goobie")


        
def main():
    MainWindow()

if __name__ == "__main__":
    main()