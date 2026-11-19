"""'Environments' category: baking, UV and layer-editor tools. Called by plug-ins/vfs_environments.py."""

from core import lifecycle, paths, shelf

SHELF_NAME = "VFS_Environments"
SHELF_FILE = paths.SHELF_DIR / "shelf_VFS_Environments.mel"
LEGACY_SHELVES = ("VFS_Tools",)    # pre-2.0.0 shelf name; removed so renamed shelves don't show up twice

# Windows / dockable controls closed on unload
WINDOWS = (
    "bake_test_ui", "bake_tester_dock_control",             # baking tools
    "uv_editing_tool_ui",                                   # UV tools
    "LayerToolsWindowWorkspaceControl",                     # layer editor
)

_state = {"active": False}

# Builds the UI once Maya is idle (i.e. startup has finished). The new layer editor registers its own scene callbacks, so no script jobs are needed.
def install():
    _state["active"] = True
    lifecycle.run_when_idle(_install_ui)

# Attempt to load workspace and shelf
def _install_ui():
    # Runs deferred. Skip if the plug-in was unloaded in the meantime, or there is no UI (batch).
    if not _state["active"] or lifecycle.is_batch():
        return
    for legacy in LEGACY_SHELVES:
        lifecycle.safe("legacy shelf " + legacy, shelf.remove_shelf, legacy)
    lifecycle.safe("shelf " + SHELF_NAME, shelf.load_shelf, SHELF_NAME, SHELF_FILE)
    lifecycle.log("Environments tools loaded.")

# Attempt to remove shelf and close the tool windows listed in WINDOWS 
def uninstall():
    _state["active"] = False
    if not lifecycle.is_batch():
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)
    lifecycle.log("Environments tools unloaded.")
