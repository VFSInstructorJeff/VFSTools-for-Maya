"""Import workspace layouts shipped with the module."""
import json
import shutil
import tempfile
from pathlib import Path

import maya.cmds as cmds

from vfstools.core import paths


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
