from typing import Optional

from maya import cmds
from maya import mel
from maya.app.general.mayaMixin import (MayaQWidgetDockableMixin as mixin)

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import ( QWidget,
                                QVBoxLayout,
                                QToolBar )

from layer_editor_tools.constants import *
from layer_editor_tools.layer_manager import LayerManager
from layer_editor_tools.utils import get_main_window


class MainWindow(mixin, QWidget):

    UI_OBJECT_NAME = "LayerToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):

        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")

        super().__init__(get_main_window() if not parent else parent)

        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("VFS Layer Tools")
        self.setAcceptDrops(True)
        self.resize(900, 600)
        self.window_layout = QVBoxLayout(self)

        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(20, 20))
        self.window_layout.addWidget(self.toolbar)

        self.layer_container = QWidget()
        self.layer_layout = QVBoxLayout(self.layer_container)
        self.window_layout.addWidget(self.layer_container)

        self.layer_manager = LayerManager()

        self.setup_toolbar()

        self.load_existing_layers()

        self.show(dockable=True)

    # --------------------------------
    # Toolbar
    # --------------------------------

    def setup_toolbar(self):

        move_up = self.toolbar.addAction(QIcon(LAYER_UP), "")
        move_down = self.toolbar.addAction(QIcon(LAYER_DOWN), "")
        new_layer = self.toolbar.addAction(QIcon(LAYER_NEW), "")
        add_layer = self.toolbar.addAction(QIcon(LAYER_ADD), "")
        delete_layer = self.toolbar.addAction(QIcon(LAYER_DELETE), "")

        move_up.triggered.connect(lambda: mel.eval("layerEditorMoveDisplayLayer 1;"))
        move_down.triggered.connect(lambda: mel.eval("layerEditorMoveDisplayLayer 0;"))
        new_layer.triggered.connect(lambda: self.add_layer(True))
        add_layer.triggered.connect(lambda: self.add_layer(False))

    # --------------------------------
    # Layer Operations
    # --------------------------------

    def add_layer(self, empty=True):
        widget = self.layer_manager.create_layer(empty=empty)

        self.layer_layout.addWidget(widget, alignment=Qt.AlignTop)

    def load_existing_layers(self):
        widgets = self.layer_manager.load()

        for widget in widgets:
            self.layer_layout.addWidget(widget, alignment=Qt.AlignTop)


def main():

    window = MainWindow()
    return window

if __name__ == "__main__":
    main()