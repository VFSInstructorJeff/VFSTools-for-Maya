"""Level-design grid materials: import them into new/opened scenes and keep texture paths valid."""
import os

import maya.cmds as cmds
import maya.mel as mel

from vfstools.core import paths

MATERIALS_FILE = paths.LD_ASSETS_DIR / "MayaLDToolsMaterials.ma"
TEXTURE_DIR = paths.LD_ASSETS_DIR / "LD_MATS"

ALL_MATS = ["Floor_grid", "Misc01_grid", "Misc02_grid", "Misc03_grid", "Misc04_grid", "Misc05_grid",
            "Misc06_grid", "Misc07_grid", "Misc08_grid", "Misc09_grid", "Wall01_grid", "Wall02_grid",
            "Wall03_grid", "Wall04_grid"]

# Prefix Maya gives duplicates created when the materials file is imported over existing ones
REPEATED_MAT_INDICATOR = "MayaLDToolsMaterials"


def import_ld_mats(*args):
    # Set import settings
    mel.eval('optionVar -cat "Files/Projects" -iv "removeDuplicateShadingNetworksOnImport" 1')

    mat_count = 0
    for material in ALL_MATS:
        if cmds.objExists(material):
            print(f"{material} already exists.")
            mat_count = mat_count + 1

    if mat_count == len(ALL_MATS):
        print("VFS Materials already exist. Skipping import.")
    elif not MATERIALS_FILE.exists():
        cmds.warning("[VFS Tools] Materials file not found: {}".format(MATERIALS_FILE))
        return
    else:
        cmds.file(paths.posix(MATERIALS_FILE), i=True)

    check_mat_duplicates()
    repoint_textures()


def check_mat_duplicates():
    # Cleanup any repeated mats, 2dplacements, textures, and shading groups
    post_import_mats = cmds.ls(materials=True)
    for mat in post_import_mats:
        if REPEATED_MAT_INDICATOR in mat:
            cmds.delete(mat)
    all_2d_textures = cmds.ls(type='place2dTexture')
    for tex2d in all_2d_textures:
        if REPEATED_MAT_INDICATOR in tex2d:
            cmds.delete(tex2d)
    all_textures = cmds.ls(type='file')
    for tex in all_textures:
        if REPEATED_MAT_INDICATOR in tex:
            cmds.delete(tex)
    all_sgs = cmds.ls(type='shadingEngine')
    for sg in all_sgs:
        if REPEATED_MAT_INDICATOR in sg:
            cmds.delete(sg)


def repoint_textures():
    """Point the grid textures at this install's LD_MATS folder.

    MayaLDToolsMaterials.ma (and scenes saved from it) store absolute texture paths from whoever
    exported them. The old installer patched the .ma with VFSLDWorkspaceEditor.exe; doing it here
    means it works from any install location and also repairs scenes saved on another machine.
    """
    for node in cmds.ls(type="file") or []:
        try:
            current = cmds.getAttr(node + ".fileTextureName").replace("\\", "/")
        except Exception:
            continue
        if "/LD_MATS/" not in current:
            continue
        target = TEXTURE_DIR / os.path.basename(current)
        if not target.exists():
            continue                      # not one of ours
        target = paths.posix(target)
        if current != target:
            try:
                cmds.setAttr(node + ".fileTextureName", target, type="string")
            except Exception:
                pass                      # e.g. referenced node - leave it alone
