from maya import cmds
import maya.OpenMaya as om
import os
from layer_editor_tools import ui as layer_editor_tools_ui
from animation_tools import ui as anim_tools_ui

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

def merge_namespaces_on_import(*args):
    print("Merging namespaces...")
    cmds.namespace(setNamespace=':')
    namespaces = [namespace for namespace in cmds.namespaceInfo(listOnlyNamespaces=True) if namespace != "UI" and namespace != "shared"] 
    for namespace in namespaces:
        cmds.namespace(removeNamespace = namespace, mergeNamespaceWithRoot = True)
        print(namespace + " was merged with Root.")

def reopen_mixamo_editor(*args):
    if cmds.window("mixamoEditorWindow", exists=True):
        cmds.deleteUI("mixamoEditorWindow", window=True)
        anim_tools_ui.mixamo_anim_editor()
    else:
        print("Mixamo Editor is closed, no need to restart it.")

def import_workspaces(*args):
    # Create the absolute workspaces path to import from (.../VFSTools-for-Maya/)
    VFSTools_dir = os.getcwd()
    workspaces_dir = str(VFSTools_dir) + r"\workspaces"
    # Add all files in workspaces folder to a list
    workspaces = os.listdir(workspaces_dir)
    # For each workspace item in the workspaces folder list, import it 
    for workspace in workspaces:
        workspace_str = workspaces_dir + r"/" + workspace
        cmds.workspaceLayoutManager(i=workspace_str)

callbacks = []
def create_callbacks():
    namespace_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, merge_namespaces_on_import)
    mixamo_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, reopen_mixamo_editor)
    callbacks.append(namespace_callback)
    callbacks.append(mixamo_callback)

def deferred_functions():
    create_script_jobs()
    create_callbacks()
    import_workspaces()

# Use executeDeferred to ensure Maya is fully loaded
maya.utils.executeDeferred(deferred_functions())