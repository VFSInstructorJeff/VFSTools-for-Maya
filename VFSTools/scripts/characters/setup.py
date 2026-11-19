"""'Characters' category: XGen hair-card tools. Called by plug-ins/vfs_characters.py.

The tool module (xgen_template_tool) imports xgenm, which only exists once Maya's XGen plug-in is
loaded, so it is NOT imported here. The shelf button imports it on demand.
"""
from core import lifecycle, paths, shelf

SHELF_NAME = "VFS_Characters"
SHELF_FILE = paths.SHELF_DIR / "shelf_VFS_Characters.mel"

# Windows / dockable controls closed on unload
WINDOWS = ("xGenToolsWorkspaceControl",)        # X-Gen Template Tool

_state = {"active": False}


def install():
    _state["active"] = True
    lifecycle.run_when_idle(_install_ui)


def _install_ui():
    if not _state["active"] or lifecycle.is_batch():
        return
    lifecycle.safe("shelf " + SHELF_NAME, shelf.load_shelf, SHELF_NAME, SHELF_FILE)
    lifecycle.log("Characters tools loaded.")


def uninstall():
    _state["active"] = False
    if not lifecycle.is_batch():
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)
    lifecycle.log("Characters tools unloaded.")
