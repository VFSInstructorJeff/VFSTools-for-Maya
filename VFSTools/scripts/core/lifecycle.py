"""Small helpers shared by every category's install()/uninstall()."""
import sys
import traceback

import maya.cmds as cmds
import maya.utils

TAG = "[VFS Tools]"


def log(message):
    print("{} {}".format(TAG, message))

# Make sure any failures are reported instead of silently failing
def safe(label, func, *args, **kwargs):
    """Run one setup step. A failure is reported loudly but doesn't stop the remaining steps.

    (The old userSetup.py failed silently when something it referenced was missing.)
    """
    try:
        return func(*args, **kwargs)
    except Exception:
        traceback.print_exc()
        cmds.warning("{} '{}' failed - see the Script Editor for details.".format(TAG, label))
        return None

# Check if Maya is running in Batch mode
def is_batch():
    return bool(cmds.about(batch=True))

# Run code once Maya is idle, i.e. after startup has finished (e.g. building the UI)
def run_when_idle(func):
    """Run func once Maya is idle, i.e. after the main window/shelves exist when loading at startup."""
    maya.utils.executeDeferred(func)


def purge_modules(package):
    """Forget a package's imported modules so the next load picks up edited code.

    Call this from uninitializePlugin. Never purge 'core' since it's shared.
    """
    # Python keeps imported modules in a cache called sys.modules. We're removing this package's entries from it (not the whole cache).
    # Get a list of modules in sys.modules where each element either has the same name as the package or starts with the package name followed by a dot (i.e. its submodules)
    prefix = package + "."
    for name in [m for m in sys.modules if m == package or m.startswith(prefix)]:
        del sys.modules[name]


def close_windows(names):
    """Close tool windows / dockable controls by name so no UI outlives its plug-in (best effort)."""
    for name in names:
        try:
            if cmds.workspaceControl(name, exists=True):
                cmds.deleteUI(name, control=True)
            elif cmds.window(name, exists=True):
                cmds.deleteUI(name, window=True)
            else:
                _close_qt_widget(name)
        except Exception as exc:
            cmds.warning("{} Could not close '{}': {}".format(TAG, name, exc))


def _close_qt_widget(object_name):
    # Tools built directly with PySide set an objectName instead of registering a Maya window.
    try:
        from PySide6 import QtWidgets          # Maya 2025+
    except ImportError:
        try:
            from PySide2 import QtWidgets      # Maya 2024 and older
        except ImportError:
            return                             # no Qt available (e.g. mayapy): nothing to close
    for widget in QtWidgets.QApplication.allWidgets():
        if widget.objectName() == object_name and widget.isWindow():
            widget.close()
            widget.deleteLater()
