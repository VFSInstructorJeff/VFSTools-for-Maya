"""VFS Tools - first-run defaults (module-level userSetup).

The first time each VFS plug-in is seen, load it and mark it Auto Load, which matches how the old
installer behaved (everything on at startup). After that, whatever the user chooses in the Plug-in
Manager (loaded / auto load) is respected.

Because this is tracked per plug-in, a plug-in added in a later update (e.g. vfs_characters.py) is
switched on for everyone after a plain `git pull` + restarting Maya, while plug-ins the user already
has - and any choice they made about them - are left alone.

To go back to the "first run" behaviour, delete the optionVar:
    cmds.optionVar(remove="VFSTools_pluginsDefaultsApplied")
"""
import maya.cmds as cmds
import maya.utils

_PLUGINS = ("vfs_environments.py", "vfs_rigging.py", "vfs_leveldesign.py", "vfs_characters.py")
_APPLIED = "VFSTools_pluginsDefaultsApplied"        # string array: plug-ins that already got first-run defaults
_OLD_APPLIED = "VFSTools_defaultsApplied"           # pre-2.0.0 flag (covered rigging, leveldesign and vfs_general)
_RENAMED_AWAY = ("vfs_general.py",)                 # plug-ins that no longer exist (now vfs_environments.py)


def _already_applied():
    applied = set(cmds.optionVar(q=_APPLIED) or []) if cmds.optionVar(exists=_APPLIED) else set()
    # Migrate from 2.0.0's predecessor: those users already made their own choices for these two.
    if cmds.optionVar(exists=_OLD_APPLIED):
        applied.update(("vfs_rigging.py", "vfs_leveldesign.py"))
    return applied


def _forget_renamed_plugins():
    """Stop Maya trying to auto-load plug-ins that were renamed, so it doesn't warn on every start."""
    for plugin in _RENAMED_AWAY:
        try:
            cmds.pluginInfo(plugin, edit=True, autoload=False)
        except Exception:
            pass                                    # not in Maya's list: nothing to clean up


def _apply_first_run_defaults():
    _forget_renamed_plugins()
    applied = _already_applied()
    for plugin in _PLUGINS:
        if plugin in applied:
            continue
        try:
            cmds.loadPlugin(plugin, quiet=True)
            cmds.pluginInfo(plugin, edit=True, autoload=True)
        except Exception as exc:                    # not recorded, so we try again next launch
            cmds.warning("[VFS Tools] Could not load {}: {}".format(plugin, exc))
            continue
        applied.add(plugin)
    cmds.optionVar(clearArray=_APPLIED)
    for plugin in sorted(applied):
        cmds.optionVar(stringValueAppend=(_APPLIED, plugin))


maya.utils.executeDeferred(_apply_first_run_defaults)
