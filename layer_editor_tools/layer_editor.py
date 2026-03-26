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
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                               QLabel, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QPushButton, QRadioButton, QButtonGroup, QCheckBox,
                               QMenu, QToolBar, QComboBox, QSizePolicy, QFrame, QSpacerItem)
from PySide6.QtGui import QIcon, QFont, QPixmap

# ---------- SETUP CONSTANTS ----------

# ---------- SETUP METHODS ----------
# Shiboken MainWindow Wrapper
def get_main_window() -> QtWidgets.QWidget:
    ptr = omui.MQtUtil.mainWindow() # Pointer to the Maya main window (Swig Object of type 'QWidget *' at 0x000002244EC30FF0)
    return wrapInstance(int(ptr), QtWidgets.QWidget) # Convert the pointer to an int (get only the address), feed the Python type for the C++ obj

# ---------- CREATE THE MAIN WINDOW ----------


class MainWindow(mixin, QtWidgets.QDialog):
    # Setup unique identifier as it is required by workspaceControl 
    UI_OBJECT_NAME = "LayerToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):

        # Delete any existing instances to avoid conflict
        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")
        
        super().__init__(get_main_window() if not parent else parent)

        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("LD Tools")

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

        # Separator Primitives/Tools
        separator2_layout = QVBoxLayout()
        ldworkflow_tab_layout.addLayout(separator2_layout)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setFrameShadow(QFrame.Shadow.Sunken)
        separator2_layout.addWidget(separator2)

        # Tools layout
        curve_tools_layout = QHBoxLayout()
        ldworkflow_tab_layout.addLayout(curve_tools_layout)
        curve_tools_layout.setSpacing(BUTTON_SPACING)

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
        tools_btnarray = [button_combine, button_separate, button_centerpivot,
                        button_killhistory, button_freeze, button_booldiff,
                        button_circlecurve, button_curvetool, button_addknot, button_sweepmesh]
        for btn in tools_btnarray:
            btn.setIconSize(QSize(64, 64))
            btn.setMaximumSize(40, 40)

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
       
        # Parenting widgets to layout (adding it with a for loop randomizes the position everytime the tool is started)
        for button in tools_btnarray:
            curve_tools_layout.addWidget(button)

        # Separator Tools/Grid
        separator2_layout = QVBoxLayout()
        ldworkflow_tab_layout.addLayout(separator2_layout)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setFrameShadow(QFrame.Shadow.Sunken)
        separator2_layout.addWidget(separator2)

        # Grid Options layout
        grid_layout = QHBoxLayout()
        ldworkflow_tab_layout.addLayout(grid_layout)
        grid_layout.setContentsMargins(0, 0, 300, 0) # left, top, right, bottom

        # Grid widgets
        grid_pixmap = QPixmap(GRID)
        grid_icon = QLabel()
        grid_icon.setPixmap(grid_pixmap)
        grid_dropdown_label = QLabel("Grid Division: ")
        grid_dropdown = QComboBox()
        grid_dropdown.addItems(['50cm', '100cm', '200cm', '400cm', 'Custom'])
        grid_dropdown.setCurrentIndex(1)

        # Connect widgets and methods
        grid_dropdown.currentTextChanged.connect(grid_setup)

        # Add widget to layout
        grid_layout.addWidget(grid_icon)
        grid_layout.addWidget(grid_dropdown_label)
        grid_layout.addWidget(grid_dropdown)

def main():
    MainWindow()

if __name__ == "__main__":
    main()