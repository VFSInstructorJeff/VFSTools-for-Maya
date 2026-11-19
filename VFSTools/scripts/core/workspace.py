"""Import workspace layouts shipped with the module."""
import json
import shutil
import tempfile
from pathlib import Path

import maya.cmds as cmds

from core import paths


def delete_workspace(name, switch_to=None):
    """Delete a workspace by name (a no-op if it doesn't exist). Used to retire renamed workspaces.

    If it's the active workspace, switch to `switch_to` first (when that exists), since Maya won't
    reliably delete the layout it is currently showing.
    """
    if name not in (cmds.workspaceLayoutManager(query=True, listUserLayouts=True) or []):
        return False
    if cmds.workspaceLayoutManager(query=True, current=True) == name and switch_to:
        cmds.workspaceLayoutManager(setCurrent=switch_to)
    cmds.workspaceLayoutManager(delete=name)
    return True


def import_workspace(json_file, replacements=None):
    """Import a workspace .json. `replacements` maps placeholder text -> value, applied first.

    Maya names the imported workspace after the file name, so a patched copy is written to a temp
    folder under the *same* file name.
    """
    json_file = Path(json_file)
    if not replacements:
        cmds.workspaceLayoutManager(i=paths.posix(json_file))
        return

    text = json_file.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, json.dumps(str(value))[1:-1])   # JSON-escaped, no quotes

    tmp_dir = tempfile.mkdtemp(prefix="vfstools_ws_")
    try:
        patched = Path(tmp_dir) / json_file.name
        patched.write_text(text, encoding="utf-8")
        cmds.workspaceLayoutManager(i=paths.posix(patched))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
