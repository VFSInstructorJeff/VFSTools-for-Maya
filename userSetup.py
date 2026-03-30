from maya import cmds
from maya import mel
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
    #cmds.scriptJob( e=["DagObjectCreated", UCX_name_fix], protected=True)

def UCX_name_fix():
    # Define prefix and suffix
    str_ucx = "UCX_"
    suffix_str = 'None'

    # Select object created
    selection_name = cmds.ls(sl=True)
    # Check selection isn't null (.e.g: creating a camera)
    if not selection_name:
        return
    else:
        # Select only the first index so we have an actual obj instead of a list with a single value in it
        selection_name = selection_name[0]
    
    # Get the obj's children
    children_ls = cmds.listRelatives(children=True, type='transform', fullPath=True)
    # Check if children are null (e.g.: creating a regular polyCube)
    if (children_ls == None):
        return
    
    # Check if there's only a single child    
    if (len(children_ls) == 1):
        # Get grandchild from child to check what type it is
        grandchild = cmds.listRelatives(children_ls, children=True, fullPath=True)
        grandchild_type = cmds.objectType(grandchild[0])
        # If it's not a mesh or a transform, ignore it (e.g.: creating a camera, grandchild will be 'camera' type)
        if ((grandchild_type != 'mesh') and (grandchild_type != 'transform')):
            print("Not a mesh. Ignoring UCX rename function.")
            return
        if str_ucx in str(children_ls[0]):
            # Rename the child so it matches its parent
            new_child_name = (str_ucx + selection_name)
            cmds.rename(str(children_ls[0]), new_child_name)
    else:
        for index, child in enumerate(children_ls):
            # Check if children have UCX_ prefix
            if str_ucx in child:
                # Check if children index is less than 10, if so append a 0 before the suffix
                if ((index + 1) < 10):
                    suffix_str = f"_0{index + 1}"
                else:
                    suffix_str = f"_{index + 1}"
                # Rename each child in children to prefix + parentName + suffix
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

def import_LD_mats(*args):
    # Set import settings
    mel.eval('optionVar -cat "Files/Projects" -iv "removeDuplicateShadingNetworksOnImport" 1')
    # Get path to mat
    all_mats = ["Floor_grid", "Misc01_grid", "Misc02_grid", "Misc03_grid", "Misc04_grid", "Misc05_grid", "Misc06_grid",
                "Misc07_grid", "Misc08_grid", "Misc09_grid", "Wall01_grid", "Wall02_grid", "Wall03_grid", "Wall04_grid"]
    mat_count = 0
    for material in all_mats:
        if cmds.objExists(material):
            print(f"{material} already exist.")
            mat_count = mat_count + 1
    
    if (mat_count == 14):
        print("VFS Materials already exist. Skipping import.")
        check_mat_duplicates()
        return
    else:
        mats_dir = str(os.path.expanduser('~')) + r"/Documents/maya/VFSTools/MayaLDToolsMaterials.ma"
        mats_dir = mats_dir.replace("\\", "/")
        cmds.file(mats_dir, i=True)
        check_mat_duplicates()

        

def check_mat_duplicates():
    # Cleanup any repeated mats, 2dplacements, textures, and shading groups
        repeated_mat_indicator = "MayaLDToolsMaterials"
        
        post_import_mats = cmds.ls(materials=True)
        for mat in post_import_mats:
            if repeated_mat_indicator in mat:
                cmds.delete(mat)
        all_2d_textures = cmds.ls(type='place2dTexture')
        for tex2d in all_2d_textures:
            if repeated_mat_indicator in tex2d:
                cmds.delete(tex2d)
        all_textures = cmds.ls(type='file')
        for tex in all_textures:
            if repeated_mat_indicator in tex:
                cmds.delete(tex)
        all_sgs = cmds.ls(type='shadingEngine')
        for sg in all_sgs:
            if repeated_mat_indicator in sg:
                cmds.delete(sg)

callbacks = []
def create_callbacks():
    namespace_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, merge_namespaces_on_import)
    mixamo_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, reopen_mixamo_editor)
    mats_new_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterNew, import_LD_mats)
    mats_open_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterOpen, import_LD_mats)
    callbacks.append(namespace_callback)
    callbacks.append(mixamo_callback)
    callbacks.append(mats_new_callback)
    callbacks.append(mats_open_callback)

def deferred_functions():
    create_script_jobs()
    create_callbacks()
    import_workspaces()

# Use executeDeferred to ensure Maya is fully loaded
utils.executeDeferred(deferred_functions())