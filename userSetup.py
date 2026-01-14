from maya import cmds
from layer_editor_tools import ui as layer_editor_tools_ui

def on_scene_change():
    print("Scene changed...")
    if not cmds.workspaceControl(layer_editor_tools_ui.DISPLAY_LAYER_WORKSPACE_CONTROL_NAME, exists=True):
        return
    layer_editor_tools_ui.update_display_layer_ui()

def create_script_jobs():
    print("Creating script jobs...")
    cmds.scriptJob(event=["NewSceneOpened", on_scene_change], protected=True)
    cmds.scriptJob(event=["SceneOpened", on_scene_change], protected=True)
    cmds.scriptJob(event=["SceneSaved", on_scene_change], protected=True)

# Use executeDeferred to ensure Maya is fully loaded
maya.utils.executeDeferred(create_script_jobs())