"""Load / remove a shelf tab from a shelf_*.mel file kept inside the module."""
import maya.cmds as cmds
import maya.mel as mel

from core import paths


def load_shelf(name, mel_file):
    """Create the shelf tab `name` from `mel_file` (e.g. 'VFS_Tools' from shelf_VFS_Tools.mel).

    The tab name Maya creates is the file name without 'shelf_' and '.mel', so `name` must match it.
    A pre-existing tab of the same name (for instance one Maya restored from the user's prefs) is
    replaced, so loading twice never produces duplicates.
    """
    remove_shelf(name)
    mel.eval('loadNewShelf "{}"'.format(paths.posix(mel_file)))
    if not cmds.shelfLayout(name, exists=True):
        cmds.warning("[VFS Tools] Expected a shelf tab named '{}' after loading {}.".format(name, mel_file))
        return False
    return True


def remove_shelf(name):
    if cmds.shelfLayout(name, exists=True):
        cmds.deleteUI(name, layout=True)
