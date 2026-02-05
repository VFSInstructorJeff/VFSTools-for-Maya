from PySide2 import QtWidgets, QtCore, QtGui
import shiboken2
import maya.OpenMayaUI as omui
import maya.cmds as cmds

# ------------------------------
# Maya main window helper
# ------------------------------
def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)

# ------------------------------
# Maya index colors (0-29)
# ------------------------------
maya_index_colors = {
    0: (0.0, 0.0, 0.1), 1: (0.0, 0.0, 0.0), 2: (0.3, 0.3, 0.3), 3: (0.5, 0.5, 0.5),
    4: (0.5, 0.0, 0.0), 5: (0.0, 0.0, 0.2), 6: (0.0, 0.0, 1.0), 7: (0.0, 0.2, 0.0),
    8: (0.1, 0.0, 0.2), 9: (1.0, 0.0, 1.0), 10: (0.5, 0.2, 0.0), 11: (0.2, 0.1, 0.0),
    12: (0.7, 0.2, 0.0), 13: (1.0, 0.0, 0.0), 14: (0.0, 1.0, 0.0), 15: (0.0, 0.2, 0.7),
    16: (1.0, 1.0, 1.0), 17: (1.0, 1.0, 0.0), 18: (0.0, 1.0, 1.0), 19: (0.0, 1.0, 0.5),
    20: (1.0, 0.7, 0.7), 21: (0.9, 0.7, 0.5), 22: (1.0, 1.0, 0.5), 23: (0.0, 0.6, 0.3),
    24: (0.6, 0.4, 0.2), 25: (0.6, 0.6, 0.2), 26: (0.4, 0.6, 0.2), 27: (0.2, 0.6, 0.4),
    28: (0.2, 0.6, 0.6), 29: (0.2, 0.4, 0.6)
}

# ------------------------------
# Color selector popup
# ------------------------------
class ColorSelector(QtWidgets.QWidget):
    color_selected = QtCore.Signal(tuple)
    def __init__(self, parent=None):
        super(ColorSelector, self).__init__(parent, QtCore.Qt.Window)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle("Select Color")
        self.setFixedSize(300, 100)

        layout = QtWidgets.QGridLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(5,5,5,5)

        row, col = 0, 0
        for idx in range(30):
            color = maya_index_colors[idx]
            btn = QtWidgets.QPushButton()
            btn.setFixedSize(26,26)
            btn.setStyleSheet(f"background-color: rgb({int(color[0]*255)},{int(color[1]*255)},{int(color[2]*255)});")
            btn.clicked.connect(lambda *_, c=color: self.select_color(c))
            layout.addWidget(btn,row,col)
            col += 1
            if col > 10:
                col = 0
                row += 1

    def select_color(self,color):
        self.color_selected.emit(color)
        self.close()

# ------------------------------
# Add Layer Popup
# ------------------------------
class AddLayerPopup(QtWidgets.QDialog):
    layer_added = QtCore.Signal(str, tuple)
    def __init__(self, parent=None):
        super(AddLayerPopup, self).__init__(parent)
        self.setWindowTitle("Add Layer")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setFixedSize(280,130)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Layer Name:"))
        self.name_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.name_edit)

        layout.addWidget(QtWidgets.QLabel("Layer Color:"))
        self.color_btn = QtWidgets.QPushButton()
        self.color_btn.setFixedSize(28,28)
        self.selected_color = (1.0, 1.0, 0.0)
        self.update_color_button()
        self.color_btn.clicked.connect(self.open_color_selector)
        layout.addWidget(self.color_btn)

        btn_layout = QtWidgets.QHBoxLayout()
        ok_btn = QtWidgets.QPushButton("OK")
        ok_btn.clicked.connect(self.add_layer)
        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def open_color_selector(self):
        self.selector = ColorSelector(self)
        self.selector.color_selected.connect(self.set_color)
        self.selector.show()

    def set_color(self,color):
        self.selected_color = color
        self.update_color_button()

    def update_color_button(self):
        r,g,b = [int(c*255) for c in self.selected_color]
        self.color_btn.setStyleSheet(f"background-color: rgb({r},{g},{b}); border:1px solid #888;")

    def add_layer(self):
        name = self.name_edit.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(self,"Error","Layer name cannot be empty.")
            return
        self.layer_added.emit(name,self.selected_color)
        self.close()

# ------------------------------
# Drop Indicator
# ------------------------------
class DropIndicator(QtWidgets.QFrame):
    def __init__(self):
        super(DropIndicator,self).__init__()
        self.setFixedHeight(10)
        self.setStyleSheet("background-color: orange;")
        self.setVisible(False)

# ------------------------------
# Layer Tab
# ------------------------------
class LayerTab(QtWidgets.QWidget):
    clicked_with_reference = QtCore.Signal(object)
    def __init__(self,name,color=(1.0,1.0,0.0),locked=False):
        super(LayerTab,self).__init__()
        self.setFixedHeight(40)
        self.layer_name = name
        self.current_color = color
        self.locked = locked
        self.drag_start_pos = QtCore.QPoint()

        # Outer frame
        self.frame = QtWidgets.QFrame()
        self.frame.setLayout(QtWidgets.QHBoxLayout())
        self.frame.layout().setContentsMargins(5,5,5,5)
        self.frame.layout().setSpacing(6)
        self.update_frame_color()

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(self.frame)

        # Name button & edit
        self.name_button = QtWidgets.QPushButton(name)
        self.name_button.setCheckable(True)
        self.name_button.setFixedHeight(28)
        self.name_button.setMinimumWidth(80)
        self.update_name_button_color()
        if not locked:
            self.name_button.clicked.connect(lambda: self.clicked_with_reference.emit(self))
            self.name_button.installEventFilter(self)

        self.name_edit = QtWidgets.QLineEdit(name)
        self.name_edit.setFixedHeight(28)
        self.name_edit.setMinimumWidth(80)
        self.name_edit.setVisible(False)
        self.name_edit.editingFinished.connect(self.finish_edit)

        self.stack = QtWidgets.QStackedLayout()
        self.stack.addWidget(self.name_button)
        self.stack.addWidget(self.name_edit)
        self.frame.layout().addLayout(self.stack)

        # Color button
        self.color_button = QtWidgets.QPushButton()
        self.color_button.setFixedSize(28,28)
        self.update_color_button()
        if not locked:
            self.color_button.clicked.connect(self.open_color_selector)
        else:
            r,g,b = [int(c*255) for c in color]
            self.color_button.setStyleSheet(f"background-color: rgb({r},{g},{b}); border:1px solid #888; opacity:0.5;")

        self.frame.layout().addWidget(self.color_button)

        # Checkboxes
        self.checkboxes = {}
        labels_and_tips = {"V":"Visible","SM":"Select Members","UCX":"Use Custom Settings","O":"Override"}
        for label,tip in labels_and_tips.items():
            cb = QtWidgets.QCheckBox(label)
            cb.setToolTip(tip)
            cb.setStyleSheet("QCheckBox { color:white; }")
            self.checkboxes[label] = cb
            self.frame.layout().addWidget(cb)

        # Export button
        self.export_button = QtWidgets.QPushButton("Export")
        self.export_button.setFixedHeight(28)
        self.export_button.setMinimumWidth(100)
        self.update_export_button_color()
        self.export_button.clicked.connect(self.export_layer)
        self.export_button.setEnabled(not locked)
        self.frame.layout().addWidget(self.export_button)

        self.frame.layout().addStretch()

    # ------------------------------
    # Edit layer name
    # ------------------------------
    def start_edit(self):
        self.name_edit.setText(self.name_button.text())
        self.stack.setCurrentWidget(self.name_edit)
        self.name_edit.setFocus()
        self.name_edit.selectAll()

    def finish_edit(self):
        new_name = self.name_edit.text().strip()
        if new_name:
            if cmds.objExists(self.layer_name):
                try: cmds.rename(self.layer_name,new_name)
                except: pass
            self.layer_name = new_name
            self.name_button.setText(new_name)
        self.stack.setCurrentWidget(self.name_button)

    def eventFilter(self,obj,event):
        if self.locked: return False
        if obj == self.name_button and event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.start_edit()
            return True
        return super(LayerTab,self).eventFilter(obj,event)

    # ------------------------------
    # Color management
    # ------------------------------
    def set_color(self,color):
        self.current_color = color
        self.update_color_button()
        self.update_name_button_color()
        self.update_export_button_color()
        self.update_frame_color()
        if cmds.objExists(self.layer_name):
            idx = next((i for i,v in maya_index_colors.items() if v==color),None)
            if idx is not None:
                try: cmds.setAttr(f"{self.layer_name}.color",idx)
                except: pass

    def update_color_button(self):
        r,g,b = [int(c*255) for c in self.current_color]
        self.color_button.setStyleSheet(f"background-color: rgb({r},{g},{b}); border:1px solid #888;")

    def update_name_button_color(self):
        r,g,b = [int(c*255*0.9) for c in self.current_color]
        self.name_button.setStyleSheet(f"QPushButton {{ background-color: rgb({r},{g},{b}); color:white; border:none; }}")

    def update_export_button_color(self):
        r,g,b = [int(c*255*0.85) for c in self.current_color]
        self.export_button.setStyleSheet(f"QPushButton {{ background-color: rgb({r},{g},{b}); color:white; border-radius:3px; }}")

    def update_frame_color(self):
        r,g,b = [int(c*255*0.7) for c in self.current_color]
        self.frame.setStyleSheet(f"QFrame {{ border:1px solid #888; border-radius:5px; background-color: rgb({r},{g},{b}); }}")

    def open_color_selector(self):
        self.selector = ColorSelector(self)
        self.selector.color_selected.connect(self.set_color)
        self.selector.show()

    # ------------------------------
    # Drag & selection
    # ------------------------------
    def mousePressEvent(self,event):
        self.drag_start_pos = event.pos()
        super(LayerTab,self).mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.locked: return
        if not (event.buttons() & QtCore.Qt.LeftButton): return
        if (event.pos()-self.drag_start_pos).manhattanLength() < QtWidgets.QApplication.startDragDistance(): return
        drag = QtGui.QDrag(self)
        mime = QtCore.QMimeData()
        mime.setText(self.layer_name)
        drag.setMimeData(mime)
        drag.setHotSpot(event.pos())
        drag.exec_(QtCore.Qt.MoveAction)

    def select(self):
        self.name_button.setChecked(True)

    def deselect(self):
        self.name_button.setChecked(False)

    # ------------------------------
    # Export placeholder
    # ------------------------------
    def export_layer(self):
        print(f"{self.layer_name} Layer Exported")


# ------------------------------
# Reorderable layer list
# ------------------------------
class ReorderableList(QtWidgets.QWidget):
    def __init__(self):
        super(ReorderableList,self).__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(10,10,10,10)
        self.setAcceptDrops(True)

        self.indicator = DropIndicator()
        self.layout.addWidget(self.indicator)
        self.selected_tab = None

        self.add_tab("All Layers",color=(0.5,0.5,0.5),locked=True)

        maya_layers = cmds.ls(type="displayLayer")
        for layer_name in maya_layers:
            if layer_name=="defaultLayer": continue
            try:
                idx = cmds.getAttr(f"{layer_name}.color")
                color_rgb = maya_index_colors.get(idx,(1.0,1.0,0.0))
            except: color_rgb=(1.0,1.0,0.0)
            self.add_tab(layer_name,color_rgb)

    def add_tab(self,name,color=(1.0,1.0,0.0),locked=False):
        tab = LayerTab(name,color,locked)
        tab.clicked_with_reference.connect(self.set_selected_tab)
        insert_index = 1 if not locked and self.layout.count()>1 else self.layout.count()-1
        self.layout.insertWidget(insert_index,tab)

    def set_selected_tab(self,tab):
        if self.selected_tab and self.selected_tab != tab:
            self.selected_tab.deselect()
        self.selected_tab = tab
        tab.select()

    def remove_selected_tab(self):
        if self.selected_tab and not self.selected_tab.locked:
            if cmds.objExists(self.selected_tab.layer_name):
                try: cmds.delete(self.selected_tab.layer_name)
                except: pass
            self.layout.removeWidget(self.selected_tab)
            self.selected_tab.deleteLater()
            self.selected_tab = None

    # Drag & drop events
    def dragEnterEvent(self,event):
        if event.mimeData().hasText(): event.acceptProposedAction()
    def dragMoveEvent(self,event):
        event.acceptProposedAction()
        pos=event.pos()
        insert_at=self.find_insert_index(pos)
        self.show_drop_indicator(insert_at)
    def dropEvent(self,event):
        event.acceptProposedAction()
        source_tab=event.source()
        if not isinstance(source_tab,LayerTab) or source_tab.locked: return
        insert_at=self.find_insert_index(event.pos())
        if insert_at==0: insert_at=1
        self.layout.removeWidget(source_tab)
        self.layout.insertWidget(insert_at,source_tab)
        self.indicator.setVisible(False)
    def find_insert_index(self,pos):
        for i in range(self.layout.count()):
            item=self.layout.itemAt(i)
            widget=item.widget()
            if isinstance(widget,DropIndicator) or widget is None: continue
            if pos.y()<widget.y()+widget.height()//2: return i
        return self.layout.count()-1
    def show_drop_indicator(self,index):
        self.layout.removeWidget(self.indicator)
        self.layout.insertWidget(index,self.indicator)
        self.indicator.setVisible(True)

# ------------------------------
# Layer Editor Window
# ------------------------------
class LayerEditorWindow(QtWidgets.QDialog):
    def __init__(self,parent=get_maya_main_window()):
        super(LayerEditorWindow,self).__init__(parent)
        self.setWindowTitle("VFS Layer Editor")
        self.setFixedSize(440,420)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        main_layout = QtWidgets.QVBoxLayout(self)
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        main_layout.addWidget(self.scroll_area)

        self.layer_list = ReorderableList()
        self.scroll_area.setWidget(self.layer_list)

        btn_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(btn_layout)

        add_btn = QtWidgets.QPushButton("Add Layer")
        add_btn.clicked.connect(self.open_add_layer_popup)
        btn_layout.addWidget(add_btn)

        remove_btn = QtWidgets.QPushButton("Remove Layer")
        remove_btn.clicked.connect(self.layer_list.remove_selected_tab)
        btn_layout.addWidget(remove_btn)

    def open_add_layer_popup(self):
        self.popup = AddLayerPopup(self)
        self.popup.layer_added.connect(self.add_layer)
        self.popup.show()

    def add_layer(self,name,color):
        self.layer_list.add_tab(name,color)
        try:
            cmds.createDisplayLayer(name=name,empty=True)
            idx = next((i for i,v in maya_index_colors.items() if v==color),None)
            if idx is not None: cmds.setAttr(f"{name}.color",idx)
        except: pass

# ------------------------------
# Show editor
# ------------------------------
def show_layer_editor():
    for w in QtWidgets.QApplication.allWidgets():
        if isinstance(w,LayerEditorWindow): w.close()
    win = LayerEditorWindow()
    win.show()

# Run UI
show_layer_editor()
