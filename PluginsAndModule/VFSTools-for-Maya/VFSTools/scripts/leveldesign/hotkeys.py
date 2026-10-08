"""VFS hotkey set (Ctrl+] / Ctrl+[ to change the grid step). Activated on load, reverted on unload."""
import maya.cmds as cmds

from core import paths

SET_NAME = "VFS_Hotkeys"
HOTKEY_FILE = paths.HOTKEY_DIR / "VFS_Hotkeys.mhk"
_PREVIOUS_SET_OPTVAR = "VFSTools_previousHotkeySet"

# Kept in sync with hotkeys/VFS_Hotkeys.mhk. Re-applied on every load so a set imported by an older
# install (whose commands still import the old 'leveldesign_tools' package) keeps working.
RUNTIME_COMMANDS = {
    "DecreaseStepSnap": "from leveldesign import ld_tools as ld\nstep = ld.current_step_index - 1\nld.scale_step_snap(step)",
    "IncreaseStepSnap": "from leveldesign import ld_tools as ld\nstep = ld.current_step_index + 1\nld.scale_step_snap(step)",
}


def install():
    for name, command in RUNTIME_COMMANDS.items():
        if cmds.runTimeCommand(name, exists=True):
            cmds.runTimeCommand(name, edit=True, command=command, commandLanguage="python")

    current = cmds.hotkeySet(query=True, current=True)

    if not cmds.hotkeySet(SET_NAME, query=True, exists=True):
        print("Importing VFS_Hotkeys...")
        cmds.hotkeySet(edit=True, ip=paths.posix(HOTKEY_FILE))

    if current == SET_NAME:
        print("VFS Hotkeys are already setup!")
        return

    cmds.optionVar(stringValue=(_PREVIOUS_SET_OPTVAR, current))   # remember it so unload can restore it
    cmds.hotkeySet(SET_NAME, edit=True, current=True)


def uninstall():
    if cmds.hotkeySet(query=True, current=True) != SET_NAME:
        return
    previous = "Maya_Default"
    if cmds.optionVar(exists=_PREVIOUS_SET_OPTVAR):
        candidate = cmds.optionVar(query=_PREVIOUS_SET_OPTVAR)
        if candidate != SET_NAME and cmds.hotkeySet(candidate, query=True, exists=True):
            previous = candidate
    cmds.hotkeySet(previous, edit=True, current=True)
