"""'Level Design' category: LD shelf, materials, scene callbacks, workspace, hotkeys, modular kit.

Called by plug-ins/vfs_leveldesign.py. The shelf also contains two UV buttons that use
general.uv; those import on demand, so they work whether or not the General plug-in is loaded.
"""
from core import favorites, lifecycle, paths, shelf, workspace
from leveldesign import callbacks, hotkeys

SHELF_NAME = "VFS_LD"
SHELF_FILE = paths.SHELF_DIR / "shelf_VFS_LD.mel"
WORKSPACE_FILE = paths.WORKSPACE_DIR / "VFS_LD.json"
MODULAR_KIT_DIR = paths.ASSETS_DIR / "modular_kit"

WINDOWS = ("LDToolsWindow",)

_state = {"active": False}


def install():
    _state["active"] = True
    lifecycle.safe("scene callbacks", callbacks.install)
    lifecycle.run_when_idle(_install_ui)


def _install_ui():
    if not _state["active"] or lifecycle.is_batch():
        return
    # Order matters: the workspace points the Content Browser at the modular kit favorite.
    lifecycle.safe("content browser favorite", favorites.add_favorite, MODULAR_KIT_DIR) # First add favorite to prefs/favs.json
    lifecycle.safe("workspace VFS_LD", workspace.import_workspace, WORKSPACE_FILE,      # Import the LD workspace
                   {"REPLACETHISLINE": paths.posix(MODULAR_KIT_DIR)})                   # REPLACETHISLINE for the MODULAR_KIT_DIR (instead of doing it with a separate script)
    lifecycle.safe("shelf " + SHELF_NAME, shelf.load_shelf, SHELF_NAME, SHELF_FILE)     # Add LD shelf
    lifecycle.safe("hotkeys", hotkeys.install)                                          # Install hotkeys
    lifecycle.log("Level Design tools loaded.")


def uninstall():
    _state["active"] = False
    lifecycle.safe("scene callbacks", callbacks.remove)
    if not lifecycle.is_batch():
        lifecycle.safe("hotkeys", hotkeys.uninstall)                                    # Switch back to the previous hotkey set
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)           # Remove LD shelf
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)               # Close the LD tools window
    lifecycle.log("Level Design tools unloaded.")
