from maya import cmds
from maya import utils
import maya.OpenMaya as om
import os
from layer_editor_tools import ui as layer_editor_tools_ui
from animation_tools import ui as anim_tools_ui
from leveldesign_tools import ld_tools as ld

def load_hotkeys(*args):
    hotkeys_dir = str(os.path.expanduser('~')) + r"/Documents/maya/VFSTools/VFS_Hotkeys.mhk"
    hotkeys_dir = hotkeys_dir.replace("\\", "/")

    hksets = cmds.hotkeySet(q=True, hsa=True)

    if "VFS_Hotkeys" not in hksets:
        print("Importing VFS_Hotkeys...")
        cmds.hotkeySet(e=True, ip=hotkeys_dir)

    cmds.hotkeySet("VFS_Hotkeys", current=True)

def on_scene_change():
    load_hotkeys()
    print("Scene changed...")
    if not cmds.workspaceControl(layer_editor_tools_ui.DISPLAY_LAYER_WORKSPACE_CONTROL_NAME, exists=True):
        return
    layer_editor_tools_ui.update_display_layer_ui()

def create_script_jobs():
    print("Creating script jobs...")
    cmds.scriptJob(event=["NewSceneOpened", on_scene_change], protected=True)
    cmds.scriptJob(event=["SceneOpened", on_scene_change], protected=True)
    cmds.scriptJob(event=["SceneSaved", on_scene_change], protected=True)
    cmds.scriptJob( e=["DagObjectCreated", UCX_name_fix], protected=True)

def UCX_name_fix():
    str_ucx = "UCX_"
    suffix_str = 'None'
    # Select object created
    selection_name = cmds.ls(sl=True)[0]
    children = cmds.listRelatives(children=True, type='transform', fullPath=True)
    if (children == None):
        return
    if (len(children) == 1):
        new_child_name = (str_ucx + selection_name)
        cmds.rename(str(children[0]), new_child_name)
    else:
        for index, child in enumerate(children):
            if str_ucx in child:
                if ((index + 1) < 10):
                    suffix_str = f"_0{index + 1}"
                else:
                    suffix_str = f"_{index + 1}"
                new_child_name = (str_ucx + selection_name + suffix_str)
                cmds.rename(str(child), new_child_name)

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
    # Create the absolute workspaces path to import from (.../VFSTools/)
    print("Importing workspaces...")
    workspaces_dir = str(os.path.expanduser('~')) + r"/Documents/maya/VFSTools/workspaces"
    workspaces_dir = workspaces_dir.replace("\\", "/")
    
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
utils.executeDeferred(deferred_functions())