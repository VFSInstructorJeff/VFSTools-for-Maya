"""'General' category: baking, UV and layer-editor tools. Called by plug-ins/vfs_general.py."""

from core import lifecycle, paths, shelf, workspace

SHELF_NAME = "VFS_Tools"
SHELF_FILE = paths.SHELF_DIR / "shelf_VFS_Tools.mel"
WORKSPACES = ("Coding.json",)

# Windows / dockable controls closed on unload
WINDOWS = (
    "bake_test_ui", "bake_tester_dock_control",             # baking tools
    "uv_editing_tool_ui",                                    # UV tools
    "LayerToolsWindow",                                      # layer editor
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
    for name in WORKSPACES:
        lifecycle.safe("workspace " + name, workspace.import_workspace, paths.WORKSPACE_DIR / name)
    lifecycle.safe("shelf " + SHELF_NAME, shelf.load_shelf, SHELF_NAME, SHELF_FILE)
    lifecycle.log("General tools loaded.")

# Attempt to remove shelf and close the tool windows listed in WINDOWS (doesn't remove Coding workspace)
def uninstall():
    _state["active"] = False
    if not lifecycle.is_batch():
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)
    lifecycle.log("General tools unloaded.")
