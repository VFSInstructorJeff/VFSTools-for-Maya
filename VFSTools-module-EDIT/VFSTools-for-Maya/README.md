# VFS-Tools-for-Maya V 1.3.0

---
Contribution Members
1. GD67JoseMunguia
2. GD68IvyMedina
3. GD76RomanKaroly
4. GD71LauraRenis
---

This shelf of tools will help you to quickly iterate in you high to low resolution baking and UV editing processes in Maya.

VFS Tools is a Maya **module** with three plug-ins, one per category, that can be loaded and unloaded while Maya is running:

| Plug-in | What it provides |
| --- | --- |
| `vfs_general.py` | Baking tools, UV tools, layer editors - `VFS_Tools` shelf, `Coding` workspace |
| `vfs_rigging.py` | FK/IK switch + mirror tools, Mixamo tools, Karoly Controlly editor - `VFS_Rigging` shelf |
| `vfs_leveldesign.py` | `VFS_LD` shelf, grid materials, VFS hotkeys (Ctrl+[ / Ctrl+]), modular kit, `VFS_LD` workspace |

## How to install

1. Download ZIP and extract the content **somewhere permanent** (Maya loads the tools from there; nothing is copied). A git clone works well: `git pull` updates everyone.
2. Double-click `installer.cmd`. It registers the folder as a Maya module (writes `Documents/maya/modules/VFSTools.mod`).
3. Open Maya (if Maya is already open, close it and open it again). All three plug-ins load automatically the first time.

If the installer doesn't work, create the file `Documents/maya/modules/VFSTools.mod` yourself containing one line, with the real path to this folder:

```
+ VFSTools 1.3.0 C:/path/to/VFSTools-for-Maya
```

(or add this folder's parent to the `MAYA_MODULE_PATH` environment variable - the `VFSTools.mod` inside this folder uses `.` as the path).

## Loading / unloading categories

- **Windows > Settings/Preferences > Plug-in Manager**: tick *Loaded* to load or untick to unload a category; tick *Auto load* to have it start with Maya. Your choice is remembered.
- Or from the Script Editor: `cmds.loadPlugin("vfs_rigging")` / `cmds.unloadPlugin("vfs_rigging")`.

Unloading removes that category's shelf, scene callbacks, script jobs and open tool windows (and, for Level Design, switches your hotkey set back).

## How to use the custom layer editor

1. Creating a layer with a mesh selected will create a copy of the mesh to be used as collision.
2. Control the visibility of the entire layer, static meshes only or collision meshes only to help yourself on your work flow.
3. Keep the naming convention SM\_**, UCX\_SM\_** and **\_grp naming convention in the outliner
4. Use the custom layer editor not the outliner to rename the layer as desired
5. Be carefull to have all meshes with unique names

## For developers

```
VFSTools.mod                  module definition (adds scripts/, plug-ins/, icons/ to Maya's paths)
installer.cmd                 registers this folder as a module
plug-ins/vfs_*.py             thin Maya plug-ins: initializePlugin -> setup.install(), uninitializePlugin -> setup.uninstall()
scripts/userSetup.py          first-run defaults only (loads + auto-loads the 3 plug-ins once)
scripts/vfstools/
    core/                     shared helpers: paths, shelf, workspace, favorites, lifecycle
    general/                  setup.py + baking/, uv/, layer_editor/
    rigging/                  setup.py + the FK/IK/Mixamo/Controlly tools
    leveldesign/              setup.py + ld_tools, materials, callbacks, hotkeys
shelves/  hotkeys/  workspaces/  icons/    loaded explicitly by each category's setup.py
assets/leveldesign/           LD_MATS textures, MayaLDToolsMaterials.ma, SM_Manny, modular_kit
legacy/                       the old installer, userSetup.py, Maya.env and workspace-patching exe (reference only)
```

Rules of thumb:
- Anything a category registers at load time (shelf, callback, scriptJob, hotkey, workspace) belongs in that category's `setup.py`, with the matching undo in `uninstall()`.
- Don't import one category from another at module level; shared code goes in `vfstools/core`.
- Shelf buttons and runtime commands must `import` what they use. They can no longer rely on names leaked into Maya's global namespace by `userSetup.py`.
- Never use absolute paths. Use `vfstools.core.paths` (`MODULE_ROOT`, `ICON_DIR`, `LD_ASSETS_DIR`, ...).
- To pick up code edits without restarting Maya: unload then load the plug-in (its modules are purged on unload).
