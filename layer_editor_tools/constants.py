# ------------ IMPORT MODULES/LIBRARIES ------------
from pathlib import Path

# ------------ SETUP CONSTANTS ------------

# ---- LINKS ----
BUG_REPORT_URL = "https://forms.gle/2jvAfG3b7qkrEswr9"
HELP_URL = ""

# ---- DIRECTORIES ----
ICON_DIR = Path(__file__).parent.parent / "icons"

# ---- COLORS ----
DARK_GRAY = "#292929"

LAYER_PALETTE = [
    # Red
    ["#7B0000", "#9B0000", "#B71C1C", "#E53935", "#EF9A9A", "#FFCDD2"],
    # Orange
    ["#7B3A00", "#E65100", "#F57C00", "#FB8C00", "#FFCC80", "#FFE0B2"],
    # Yellow
    ["#7B6500", "#F57F17", "#F9A825", "#FBC02D", "#FFF176", "#FFF9C4"],
    # Green
    ["#1B5E20", "#2E7D32", "#388E3C", "#43A047", "#A5D6A7", "#C8E6C9"],
    # Light Blue
    ["#0D47A1", "#1565C0", "#1976D2", "#1E88E5", "#90CAF9", "#BBDEFB"],
    # Dark Blue
    ["#1A237E", "#283593", "#303F9F", "#3949AB", "#9FA8DA", "#C5CAE9"],
    # Purple
    ["#4A148C", "#6A1B9A", "#7B1FA2", "#8E24AA", "#CE93D8", "#E1BEE7"],
    # Gray
    ["#212121", "#424242", "#616161", "#757575", "#BDBDBD", "#E0E0E0"],
]


# ---- ICONS ----
# Layer Related
LAYER_UP = str(ICON_DIR / "moveLayerUp.png")
LAYER_DOWN = str(ICON_DIR / "moveLayerDown.png")
LAYER_NEW = str(ICON_DIR / "newLayerEmpty.png")
LAYER_ADD = str(ICON_DIR / "newLayerSelected.png")
LAYER_DELETE = str(ICON_DIR / "delete.png")
LAYER_VISIBLE = str(ICON_DIR / "visible.png")
HIDDEN = str(ICON_DIR / "hidden.png")
VISIBLE = str(ICON_DIR / "visible.png")
CONFIG_DROPDOWN = str(ICON_DIR / "hotkeySetSettings.png")
FOLDER_OPEN = str(ICON_DIR / "folder-open.png")
HELP = str(ICON_DIR / "help_line.png")
BUG_REPORT = str(ICON_DIR / "aic_warning.png")
DRAG_HANDLE = str(ICON_DIR / "draggable.png")
UNDO = str(ICON_DIR/ "undo_s.png")

# Others
ARROW_RIGHT = str(ICON_DIR / "teRightArrow.png")
ARROW_DOWN = str(ICON_DIR / "teDownArrow.png")
GONK = str(ICON_DIR / "gonk.png")




