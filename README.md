# VFS-Tools-for-Maya V 1.3.0

---
Contribution Members
1. GD67 Jose Munguia
2. GD68 Ivy Medina
3. GD76 Roman Karoly
4. GD71 Laura Renis
---

VFS Tools is a Maya **module** with three plug-ins, one per category, that can be loaded and unloaded through the Plug-In Manager while Maya is running.

vfs_general.py - Contains Baking tools, UV tools, and the Layer editor. Loads the VFS_Tools shelf, and the Coding workspace.
vfs_rigging.py - FK/IK switch + mirror tools, Mixamo tools, Karoly Controlly editor. Loads the VFS_Rigging shelf.
vfs_leveldesign.py - Loads VFS_LD shelf, grid materials, VFS hotkeys, modular kit, and VFS_LD workspace.


## How to install

0. Close Maya.
1. [DOWNLOAD] Download ZIP and extract the content **somewhere permanent** (Maya loads the tools from there) OR
   [CLONE REPO] Clone the VFSTools-for-Maya repo to your REPOS folder (at C:/Users/Public/Repos). Pull from main to get updates.
2. Double-click installer.cmd (the only file you need to run). It registers the VFSTools folder next to it as a Maya module (writes `Documents/maya/modules/VFSTools.mod`). Everything else lives inside `VFSTools`; you don't need to open it.
3. Open Maya (if Maya is already open, close it and open it again). All three plug-ins load automatically the first time.

If the installer doesn't work, create the file `Documents/maya/modules/VFSTools.mod` yourself containing one line, with the real path to the `VFSTools` folder (the one *inside* `VFSTools-for-Maya`):

```
+ VFSTools 1.3.0 C:/path/to/VFSTools-for-Maya/VFSTools
```

## Loading / unloading categories

- **Windows > Settings/Preferences > Plug-in Manager**: tick *Loaded* to load or untick to unload a category; tick *Auto load* to have it start with Maya. Your choice is remembered.

Unloading removes that category's shelf, scene callbacks and open tool windows (and, for Level Design, switches your hotkey set back).



## For developers

```
VFSTools-for-Maya/
    installer.cmd             registers the VFSTools folder as a Maya module (the only thing users run)
    README.md
    VFSTools/                 <- the Maya module
        VFSTools.mod              module definition (adds scripts/, plug-ins/, icons/ to Maya's paths)
        MIGRATION.md              old layout -> module notes, things to verify in Maya
        plug-ins/vfs_*.py         thin Maya plug-ins: initializePlugin -> setup.install(), uninitializePlugin -> setup.uninstall()
        scripts/
            userSetup.py          first-run defaults only (loads + auto-loads the 3 plug-ins once)
            core/                 shared helpers: paths, shelf, workspace, favorites, lifecycle
            general/              setup.py + baking/, uv/, layer_editor/
            rigging/              setup.py + the FK/IK/Mixamo/Controlly tools
            leveldesign/          setup.py + ld_tools, materials, callbacks, hotkeys
        shelves/  hotkeys/  workspaces/  icons/    loaded explicitly by each category's setup.py
        assets/                   LD_MATS textures, modular_kit, MayaLDToolsMaterials.ma, SM_Manny
        legacy/                   the old installer, userSetup.py, Maya.env and workspace-patching exe (reference only - do not run)
```

The packages in `scripts/` are top-level Python packages (`import core`, `from general import setup`, ...), so keep their names distinctive: another tool on the same Python path with a top-level `core` would clash with ours.

Rules of thumb:
- Anything a category registers at load time (shelf, callback, hotkey, workspace) belongs in that category's `setup.py`, with the matching undo in `uninstall()`.
- Don't import one category from another at module level; shared code goes in `core`.
- Shelf buttons and runtime commands must `import` what they use. They can no longer rely on names leaked into Maya's global namespace by `userSetup.py`.
- Never use absolute paths. Use `core.paths` (`MODULE_ROOT`, `ICON_DIR`, `ASSETS_DIR`, ...).
- To pick up code edits without restarting Maya: unload then load the plug-in (its modules are purged on unload).
