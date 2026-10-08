"""Locations inside the VFS Tools module.

Everything is derived from this file's position, so the module works from wherever it is
installed (a git clone, a network share, ...) - nothing is hardcoded to one user's machine.
"""
from pathlib import Path

# <root>/scripts/core/paths.py  ->  parents[2] is <root>
MODULE_ROOT = Path(__file__).resolve().parents[2]

ICON_DIR = MODULE_ROOT / "icons"
SHELF_DIR = MODULE_ROOT / "shelves"
HOTKEY_DIR = MODULE_ROOT / "hotkeys"
WORKSPACE_DIR = MODULE_ROOT / "workspaces"
ASSETS_DIR = MODULE_ROOT / "assets"


def posix(path):
    """Maya (and MEL string escaping) is happier with forward slashes, also on Windows."""
    return str(path).replace("\\", "/")
