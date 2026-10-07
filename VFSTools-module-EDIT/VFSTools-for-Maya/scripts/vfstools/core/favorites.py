"""Add a folder to the Content Browser favorites (prefs/favs.json) without touching other entries."""
import json
from pathlib import Path

import maya.cmds as cmds

from vfstools.core import paths
from vfstools.core.lifecycle import log


def add_favorite(folder):
    """Return True if the folder was added, False if it was already listed or the file is unreadable."""
    fav_file = Path(cmds.internalVar(userPrefDir=True)) / "favs.json"
    entry = paths.posix(folder)

    data = {}
    if fav_file.exists():
        try:
            data = json.loads(fav_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            cmds.warning("[VFS Tools] Could not read {} - leaving it untouched.".format(fav_file))
            return False

    favorites = data.setdefault("favorites", [])
    if entry.lower() in (str(f).replace("\\", "/").lower() for f in favorites):
        return False

    favorites.append(entry)
    fav_file.parent.mkdir(parents=True, exist_ok=True)
    fav_file.write_text(json.dumps(data, indent=4), encoding="utf-8")
    log("Added Content Browser favorite: {}".format(entry))
    return True
