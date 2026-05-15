import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6 import QtWidgets


control_name = (
    "ChannelBoxLayerEditor|MainChannelsLayersLayout|"
    "ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout"
)

ptr = omui.MQtUtil.findControl(control_name)

if not ptr:
    print("Channel Box is not open/doesn't exist yet")

tab_widget = wrapInstance(int(ptr), QtWidgets.QTabWidget)

class MyCustomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Safe Custom Tab"))


if not hasattr(tab_widget, "_custom_tabs"):
    tab_widget._custom_tabs = []

my_widget = MyCustomWidget(parent=tab_widget)
tab_widget.addTab(my_widget, "My Tool")
tab_widget._custom_tabs.append(my_widget)

for i in range(tab_widget.count()):
    if tab_widget.tabText(i) == "My Tool":
        pass

