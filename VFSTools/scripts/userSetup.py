"""VFS Tools - first-run defaults (module-level userSetup).

The first time the module is used, load all three VFS plug-ins and mark them Auto Load, which matches
how the old installer behaved (everything on at startup). After that this does nothing: whatever
the user chooses in the Plug-in Manager (loaded / auto load) is respected.

To go back to the "first run" behaviour, delete the optionVar:  cmds.optionVar(remove="VFSTools_defaultsApplied")
"""
import maya.cmds as cmds
import maya.utils

_PLUGINS = ("vfs_general.py", "vfs_rigging.py", "vfs_leveldesign.py")
_DEFAULTS_APPLIED = "VFSTools_defaultsApplied"


def _apply_first_run_defaults():
    if cmds.optionVar(exists=_DEFAULTS_APPLIED):
        return
    all_ok = True
    for plugin in _PLUGINS:
        try:
            cmds.loadPlugin(plugin, quiet=True)
            cmds.pluginInfo(plugin, edit=True, autoload=True)
        except Exception as exc:
            all_ok = False
            cmds.warning("[VFS Tools] Could not load {}: {}".format(plugin, exc))
    if all_ok:                       # otherwise try again next launch
        cmds.optionVar(intValue=(_DEFAULTS_APPLIED, 1))


maya.utils.executeDeferred(_apply_first_run_defaults)
