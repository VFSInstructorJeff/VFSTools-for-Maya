import maya.cmds as cmds

def delete_VFS_tab():
    tab_name = "VFSToolsTab"

    if cmds.control(tab_name, exists=True):
        cmds.deleteUI(tab_name)
        print("VFS tab deleted.")
    else:
        print("VFS tab not found.")

delete_VFS_tab()