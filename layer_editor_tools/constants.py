# ------------ IMPORT MODULES/LIBRARIES ------------
from pathlib import Path

# ------------ SETUP CONSTANTS ------------

# Directories
ICON_DIR = Path(__file__).parent.parent / "icons"

# Icons
LAYER_UP = str(ICON_DIR / "moveLayerUp.png")
LAYER_DOWN = str(ICON_DIR / "moveLayerDown.png")
LAYER_NEW = str(ICON_DIR / "newLayerEmpty.png")
LAYER_ADD = str(ICON_DIR / "newLayerSelected.png")
LAYER_DELETE = str(ICON_DIR / "delete.png")
LAYER_VISIBLE = str(ICON_DIR / "visible.png")
GONK = str(ICON_DIR / "gonk.png")