import maya.cmds as cmds 

def VFSToolsUI():
    tab_layout = "ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout"

    if not cmds.tabLayout(tab_layout, exists=True):
        cmds.warning("Channel Box tabLayout not found.")
        return

    if cmds.control("VFSToolsTab", exists=True):
        cmds.deleteUI("VFSToolsTab")

    vfs_tab = cmds.columnLayout(
        "VFSToolsTab",
        adjustableColumn=True,
        parent=tab_layout
    )

    cmds.button(label="VFS Tool A")
    cmds.button(label="VFS Tool B")
    cmds.button(label="VFS Tool C")

    cmds.tabLayout(
        tab_layout,
        edit=True,
        tabLabel=(vfs_tab, "VFS")
    )

VFSToolsUI()