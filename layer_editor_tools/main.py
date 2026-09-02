from typing import Optional
import webbrowser

from maya import cmds
from maya.api import OpenMaya as om
from maya.app.general.mayaMixin import (MayaQWidgetDockableMixin as mixin)

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolBar, QScrollArea, QLabel, QColorDialog

from shiboken6 import isValid

from layer_editor_tools.constants import *
from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.layer_manager import LayerManager
from layer_editor_tools.layer_widget import LayerWidget
from layer_editor_tools.utils import get_main_window

# Tracks the single live MainWindow instance so its scene callbacks can be
# torn down explicitly before the UI is deleted. cmds.deleteUI() on a
# workspaceControl does NOT reliably fire Qt's closeEvent, so relying on
# closeEvent alone leaked a full set of om.MSceneMessage/MEventMessage
# callbacks (all still pointing at a dead widget) every time the tool
# was relaunched.
_current_instance = None

# ------------ MAIN WINDOW ------------

class MainWindow(mixin, QWidget):

    UI_OBJECT_NAME = "LayerToolsWindow"

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        global _current_instance

        # Clean up the previous instance's callbacks *before* its UI gets
        # torn down, since deleteUI won't do this for us.
        if _current_instance is not None:
            _current_instance._teardown_callbacks()
            _current_instance = None

        if cmds.workspaceControl(self.UI_OBJECT_NAME + "WorkspaceControl", exists=True):
            cmds.deleteUI(self.UI_OBJECT_NAME + "WorkspaceControl")

        super().__init__(get_main_window() if not parent else parent)

        self.setObjectName(self.UI_OBJECT_NAME)
        self.setWindowTitle("VFS Layer Tools")
        self.setAcceptDrops(True)
        self.resize(600, 600)

        self.window_layout = QVBoxLayout(self)

        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(20, 20))
        self.window_layout.addWidget(self.toolbar)

        self.layer_container = QWidget()
        self.layer_layout = QVBoxLayout(self.layer_container)
        self.layer_layout.setAlignment(Qt.AlignTop)
        self.layer_layout.setSpacing(2)
        self.layer_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.layer_container)
        self.scroll_area.setWidgetResizable(True)                               # Make container stretch to fill the scroll area width
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    # No horizontal scrollbar since layers should always
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)       # Scrollbar only appears when there's more layers than the window can show
        self.window_layout.addWidget(self.scroll_area)

        self.hint_label = QLabel("Right click layer for more options")
        self.window_layout.addWidget(self.hint_label)

        self.tool_version = QLabel("VFS Layer Tools v2.0.0 [FEATURE BRANCH]")
        self.window_layout.addWidget(self.tool_version)

        self.layer_manager = LayerManager()
        self._refreshing = False

        self._setup_color_palette()
        self.setup_toolbar()
        self.load_existing_layers()

        # Scene callbacks
        self._save_callback = om.MSceneMessage.addCallback(
            om.MSceneMessage.kBeforeSave,
            lambda *args: self.layer_manager.save()
        )
        self._new_callback = om.MSceneMessage.addCallback(
            om.MSceneMessage.kAfterNew,
            lambda *args: QTimer.singleShot(0, self.refresh_layers)
        )
        self._open_callback = om.MSceneMessage.addCallback(
            om.MSceneMessage.kAfterOpen,
            lambda *args: QTimer.singleShot(0, self.refresh_layers)
        )

        # Maya layer callbacks
        self._layer_added_callback = om.MEventMessage.addEventCallback(
            "displayLayerAdded",
            lambda *args: self.on_maya_layer_added()
        )

        _current_instance = self

        self.show(dockable=True)

    # --------------------------------
    # Setup Custom Color Palette
    # --------------------------------

    def _setup_color_palette(self):
        index = 0
        for row in LAYER_PALETTE:
            for hex_color in row:
                QColorDialog.setStandardColor(index, QColor(hex_color))
                index += 1

    # --------------------------------
    # Toolbar
    # --------------------------------

    def setup_toolbar(self):
        new_layer = self.toolbar.addAction(QIcon(LAYER_NEW), "")
        add_layer = self.toolbar.addAction(QIcon(LAYER_ADD), "")
        delete_layer = self.toolbar.addAction(QIcon(LAYER_DELETE), "")
        move_up = self.toolbar.addAction(QIcon(LAYER_UP), "")
        move_down = self.toolbar.addAction(QIcon(LAYER_DOWN), "")

        new_layer.triggered.connect(lambda: self.add_layer(empty=True))
        add_layer.triggered.connect(lambda: self.add_layer(empty=False))
        delete_layer.triggered.connect(self.delete_selected_layer)
        move_up.triggered.connect(self.move_selected_up)
        move_down.triggered.connect(self.move_selected_down)

        # Push subsequent buttons to the right
        spacer = QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.toolbar.addWidget(spacer)

        help_btn = self.toolbar.addAction(QIcon(HELP), "")
        bug_btn = self.toolbar.addAction(QIcon(BUG_REPORT), "")

        help_btn.triggered.connect(lambda: webbrowser.open(HELP_URL) if HELP_URL else None) # TODO: Add documentation
        bug_btn.triggered.connect(lambda: webbrowser.open(BUG_REPORT_URL))

        new_layer.setToolTip("Create new empty layer")
        add_layer.setToolTip("Create new layer from selection")
        delete_layer.setToolTip("Delete selected layer")
        move_up.setToolTip("Move selected layer up")
        move_down.setToolTip("Move selected layer down")
        help_btn.setToolTip("Open documentation")
        bug_btn.setToolTip("Report a bug")

    # --------------------------------
    # Layer Operations
    # --------------------------------

    def add_layer(self, empty=True):
        widget = self.layer_manager.create_layer(empty=empty)
        self.layer_layout.insertWidget(0, widget, alignment=Qt.AlignTop)

    def delete_selected_layer(self):
        entry = self.layer_manager.selected_entry
        if not entry:
            return
        widget = entry["widget"]
        self.layer_manager.remove_selected()
        self.layer_layout.removeWidget(widget)

    def move_selected_up(self):
        entry = self.layer_manager.selected_entry
        if not entry:
            return
        widget = entry["widget"]
        index = self.layer_layout.indexOf(widget)
        if index <= 0:
            return
        self.layer_manager.move_selected_up()
        self.layer_layout.removeWidget(widget)
        self.layer_layout.insertWidget(index - 1, widget, alignment=Qt.AlignTop)

    def move_selected_down(self):
        entry = self.layer_manager.selected_entry
        if not entry:
            return
        widget = entry["widget"]
        index = self.layer_layout.indexOf(widget)
        if index == self.layer_layout.count() - 1:
            return
        self.layer_manager.move_selected_down()
        self.layer_layout.removeWidget(widget)
        self.layer_layout.insertWidget(index + 1, widget, alignment=Qt.AlignTop)

    def load_existing_layers(self):
        widgets = self.layer_manager.load()
        for widget in widgets:
            self.layer_layout.addWidget(widget, alignment=Qt.AlignTop)

    def refresh_layers(self):
        self._refreshing = True
        try:
            for entry in self.layer_manager.layers:
                self.layer_manager._remove_node_callback(entry["data"].uuid)
                widget = entry["widget"]
                if isValid(widget):
                    widget.setParent(None)
                    widget.deleteLater()
    
            self.layer_manager.layers = []
            self.layer_manager.selected_entry = None
    
            self.load_existing_layers()
        finally:
            self._refreshing = False

    # --------------------------------
    # Maya Layer Sync
    # --------------------------------

    def on_maya_layer_added(self):
        if self.layer_manager._creating or self._refreshing:
            return
        try:
            maya_layers = [l for l in cmds.ls(type="displayLayer") if l != "defaultLayer"]
            known_names = {entry["data"].maya_layer_name for entry in self.layer_manager.layers}

            for layer_name in maya_layers:
                if layer_name not in known_names:
                    uuid = cmds.ls(layer_name, uuid=True)[0]
                    data = VFSLayerData(uuid=uuid, maya_layer_name=layer_name)
                    self.layer_manager._sync_from_maya(data)

                    widget = LayerWidget(data)
                    widget.selected.connect(self.layer_manager.on_layer_selected)
                    widget.path_changed.connect(self.layer_manager.update_session_cache)
                    widget.legc_path_changed.connect(self.layer_manager.update_session_cache_legc_path)
                    widget.legc_state_changed.connect(self.layer_manager.update_session_cache_legc)

                    entry = {"data": data, "widget": widget}
                    self.layer_manager.layers.insert(0, entry)
                    self.layer_manager._attach_node_callback(entry)

                    self.layer_layout.insertWidget(0, widget, alignment=Qt.AlignTop)

        except RuntimeError:
            pass  # Fired during scene switch before refresh completed, safe to ignore

    # --------------------------------
    # Cleanup
    # --------------------------------

    def closeEvent(self, event):
        global _current_instance
        self._teardown_callbacks()
        if _current_instance is self:
            _current_instance = None
        super().closeEvent(event)

    def _teardown_callbacks(self):
        """Remove node + scene callbacks. Called from closeEvent, and also
        called directly on the previous instance from __init__ since
        cmds.deleteUI() does not reliably trigger closeEvent."""
        # Remove node callbacks for all layers
        for entry in self.layer_manager.layers:
            uuid = entry["data"].uuid
            self.layer_manager._remove_node_callback(uuid)

        for cb in (self._save_callback, self._new_callback, self._open_callback):
            try:
                om.MSceneMessage.removeCallback(cb)
            except RuntimeError:
                pass  # Already removed
        try:
            om.MEventMessage.removeCallback(self._layer_added_callback)
        except RuntimeError:
            pass  # Already removed


def main():
    window = MainWindow()
    return window


if __name__ == "__main__":
    main()