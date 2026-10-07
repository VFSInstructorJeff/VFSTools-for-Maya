"""'General' category: baking, UV and layer-editor tools. Called by plug-ins/vfs_general.py."""
import maya.cmds as cmds

from vfstools.core import lifecycle, paths, shelf, workspace

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
_script_job_ids = []


def _create_script_jobs():
    print("Creating script jobs...")
    _remove_script_jobs()
    for event in ("NewSceneOpened", "SceneOpened", "SceneSaved"):
        _script_job_ids.append(cmds.scriptJob(event=[event, on_scene_change], protected=True))


def _remove_script_jobs():
    # The jobs are 'protected', which means they can only be killed with force=True.
    for job_id in _script_job_ids:
        if cmds.scriptJob(exists=job_id):
            cmds.scriptJob(kill=job_id, force=True)
    del _script_job_ids[:]

# Attemp to initialise script jobs. Will print a warning if it goes wrong. Then builds UI when Maya is fully initialised.
def install():
    _state["active"] = True
    lifecycle.safe("script jobs", _create_script_jobs)
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

# Attempt
def uninstall():
    _state["active"] = False
    lifecycle.safe("script jobs", _remove_script_jobs)
    if not lifecycle.is_batch():
        lifecycle.safe("shelf " + SHELF_NAME, shelf.remove_shelf, SHELF_NAME)
        lifecycle.safe("close windows", lifecycle.close_windows, WINDOWS)
    lifecycle.log("General tools unloaded.")
