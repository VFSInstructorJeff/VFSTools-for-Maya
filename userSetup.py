from maya import cmds
import maya.OpenMaya as om
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

callbacks = []
def create_callbacks():
    namespace_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, merge_namespaces_on_import)
    mixamo_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, reopen_mixamo_editor)
    callbacks.append(namespace_callback)
    callbacks.append(mixamo_callback)

def deferred_functions():
    create_script_jobs()
    create_callbacks()

# Use executeDeferred to ensure Maya is fully loaded
maya.utils.executeDeferred(deferred_functions())