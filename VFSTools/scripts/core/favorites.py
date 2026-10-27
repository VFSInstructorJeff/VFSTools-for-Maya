"""Add a folder to the Content Browser favorites (prefs/favs.json) without touching other entries."""
import json
from pathlib import Path

import maya.cmds as cmds

from core import paths
from core.lifecycle import log


def add_favorite(folder):
    """Return True if the folder was added, False if it was already listed or the file is unreadable."""
    fav_file = Path(cmds.internalVar(userPrefDir=True)) / "favs.json"   # Find favs.json full path
    entry = paths.posix(folder)     # Get folder to add to favs and format the path correctly

    data = {}
    if fav_file.exists():
        try:
            data = json.loads(fav_file.read_text(encoding="utf-8"))     # Read favs.json if it exists
        except (OSError, ValueError):
            cmds.warning("[VFS Tools] Could not read {} - leaving it untouched.".format(fav_file))
            return False

    favorites = data.setdefault("favorites", [])
    if entry.lower() in (str(f).replace("\\", "/").lower() for f in favorites):     # If chosen folder is already in favs, don't add it again
        return False

    favorites.append(entry)
    fav_file.parent.mkdir(parents=True, exist_ok=True)
    fav_file.write_text(json.dumps(data, indent=4), encoding="utf-8")   # Add chosen folder to favs.json
    log("Added Content Browser favorite: {}".format(entry))
    return True
