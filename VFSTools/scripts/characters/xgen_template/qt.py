"""PySide6 / PySide2 compatibility, so the rest of the tool does not repeat the same try/except import."""

import collections

Qt = collections.namedtuple("Qt", "QtCore QtGui QtWidgets wrap_instance is_valid")


def load_qt():
    """Return the Qt modules of whichever PySide this Maya ships (PySide6 first, then PySide2)."""
    try:
        from PySide6 import QtCore, QtGui, QtWidgets
        import shiboken6 as shiboken
    except ImportError:
        from PySide2 import QtCore, QtGui, QtWidgets
        import shiboken2 as shiboken
    return Qt(QtCore, QtGui, QtWidgets, shiboken.wrapInstance, shiboken.isValid)


def find_widget(control_name, widget_class=None):
    """The Qt widget behind a named Maya control, or None if Maya has no such control."""
    import maya.OpenMayaUI as omui

    qt = load_qt()
    pointer = omui.MQtUtil.findControl(control_name)
    if not pointer:
        return None
    return qt.wrap_instance(int(pointer), widget_class or qt.QtWidgets.QWidget)


def main_window():
    """Maya's main window as a QWidget (parent for dialogs), or None."""
    import maya.OpenMayaUI as omui

    qt = load_qt()
    pointer = omui.MQtUtil.mainWindow()
    if not pointer:
        return None
    return qt.wrap_instance(int(pointer), qt.QtWidgets.QWidget)
