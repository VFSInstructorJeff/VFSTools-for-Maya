"""'Rigging' category: FK/IK, mirroring, Mixamo and Controlly tools. Called by plug-ins/vfs_rigging.py."""
from vfstools.core import lifecycle, paths, shelf

SHELF_NAME = "VFS_Rigging"
SHELF_FILE = paths.SHELF_DIR / "shelf_VFS_Rigging.mel"

WINDOWS = ("Karoly Controlly Editor",)

_state = {"active": False}


def install():
    _state["active"] = True
    lifecycle.run_when_idle(_install_ui)


def _install_ui():
    if not _state["active"] or lifecycle.is_batch():
        return
    lifecycle.safe("shelf " + SHELF_NAME, shelf.load_shelf, SHELF_NAME, SHELF_FILE)
    lifecycle.log("Rigging tools loaded.")


def uninstall():
    _state["active"] = False
    if not lifecycle.is_batch():
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)
    lifecycle.log("Rigging tools unloaded.")
