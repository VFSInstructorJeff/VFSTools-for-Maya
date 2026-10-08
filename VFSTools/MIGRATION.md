# Migration notes: old layout -> module

## Where everything went

Paths are relative to the `VFSTools` folder (the module root, inside `VFSTools-for-Maya`).

| Old | New | Plug-in |
| --- | --- | --- |
| `animation_tools/` | `scripts/rigging/` | rigging |
| `shelf_VFS_Rigging.mel` | `shelves/` | rigging |
| `baking_tools/`, `uv_tools/` | `scripts/general/baking`, `.../uv` | general |
| `layer_editor_tools/` (except `old/`) | `scripts/general/layer_editor/` | general |
| `layer_editor_tools/old/` (legacy Display Layer Editor) | **removed** | - |
| `shelf_VFS_Tools.mel`, `workspaces/Coding.json` | `shelves/`, `workspaces/` | general |
| userSetup: display-layer scriptJobs (`on_scene_change`) | **removed** (they only refreshed the legacy editor; the current layer editor registers its own scene callbacks) | - |
| userSetup: `UCX_name_fix` (was already disabled) | `general/ucx.py` | general |
| `leveldesign_tools/ld_tools.py` | `scripts/leveldesign/ld_tools.py` | level design |
| `shelf_VFS_LD.mel`, `workspaces/VFS_LD.json` | `shelves/`, `workspaces/` | level design |
| `VFS_Hotkeys.mhk` + userSetup `load_hotkeys` | `hotkeys/`, `leveldesign/hotkeys.py` | level design |
| userSetup: `import_LD_mats`, `check_mat_duplicates` | `leveldesign/materials.py` | level design |
| userSetup: scene callbacks (namespace merge, material import) | `leveldesign/callbacks.py` | level design |
| `LD_MATS/`, `modular_kit/`, `MayaLDToolsMaterials.ma`, `SM_Manny.*` | `assets/` | level design |
| `icons/` | `icons/` (on `XBMLANGPATH` via the module) | - |
| `Maya.env`, `userSetup.py`, `installer.cmd`, `cleanupBatch.cmd`, `VFSLDWorkspaceEditor.*`, `favs.json` | `legacy/` (replaced) | - |

Python packages are now the top-level packages `core`, `general`, `leveldesign` and `rigging` (e.g. `from general.uv import ui`).

## Behaviour that changed on purpose

- **Hidden dependencies removed.** 11 LD shelf buttons used `ld` and 3 used `cmds` without importing them. They only worked because `userSetup.py` leaked those names into Maya's global namespace. They now import explicitly.
- **No more per-user absolute paths.** `VFSLDWorkspaceEditor.exe` patched the materials `.ma` and `VFS_LD.json` after copying. Now texture paths are repointed at runtime (`materials.repoint_textures`, which also repairs scenes saved on another machine) and the workspace's `REPLACETHISLINE` is filled in when it is imported. Shelf icons that pointed at `C:/Users/lrenis/...` use bare file names.
- **Content Browser favorite** for the modular kit is *added* to `prefs/favs.json` (the old installer overwrote the file).
- **Hotkeys are reversible.** Loading Level Design remembers your current hotkey set and unloading restores it. Runtime commands left over from an old install are rewritten to the new package path.
- **Failures are no longer silent.** Each setup step is wrapped; a failure prints a traceback and a warning but doesn't stop the other steps.
- **No `MAYA_ENV_DIR` redirect.** The installer removes it. If Maya still loads the old tools afterwards, sign out and back in.
- **Legacy Display Layer Editor removed.** `layer_editor/old/` and the scriptJobs that refreshed it are gone. Nothing in the shelves opened it; the current layer editor (`layer_editor/main.py`) is unaffected. `VFS_LD.json` still lists `displayLayerWorkspaceControl` under `closedControls`, which only remembers where a closed window used to sit and is harmless.

## Not changed (pre-existing, found while reorganizing)

- `animation_tools/mixamo_animation_editor.py:189` calls `set_controllers_to_default`, which isn't defined anywhere.
- `layer_editor/layer_editor.py` is not imported by anything and has a hardcoded `C:\Users\Public\Repos\...` icon path and an undefined `maya_layers`.
- `ld_tools.py` builds icon paths with `\` separators, so it is Windows-only.
- `ld_tools.py` contains placeholder UI code ("You like food").

## Naming heads-up

- `core`, `general`, `leveldesign` and `rigging` are top-level package names, so they share Python's namespace with every other tool in Maya. If another tool in your pipeline also has a top-level `core` (or similar), whichever is found first wins and the other breaks. No conflict was found in the standard library, but Maya's own Python and your other tools could not be checked here.
- `legacy/` contains runnable files from the old installer (`installer.cmd`, `cleanupBatch.cmd`, `VFSLDWorkspaceEditor.exe`). Running them would redo the old install and delete files in `Documents/maya`. They are only kept for reference.

## Please verify in Maya (could not be run here)

1. Plug-in Manager lists `vfs_general.py`, `vfs_rigging.py`, `vfs_leveldesign.py`; unticking *Loaded* removes the matching shelf; ticking it brings it back with no duplicate tab.
2. First launch after install loads all three (needs the module's `scripts/userSetup.py` to be executed by Maya).
3. Ctrl+] / Ctrl+[ change the grid step with Level Design loaded, and the previous hotkey set returns after unloading it.
4. New scene / open scene imports the grid materials with working textures.
5. After quitting Maya with a category loaded, check `Documents/maya/<ver>/prefs/shelves/` - Maya may save a copy of the shelf there. It is harmless (loading replaces any same-named tab) but you may want to delete it if you notice stale shelves when a plug-in is off.
6. The `VFS_LD` workspace opens the Content Browser on the modular kit.
7. With the General plug-in loaded, the layer editor still refreshes after *New Scene* and *Open Scene* (it now relies only on its own callbacks).
8. In the Script Editor, `import core, general, leveldesign, rigging` and print each module's `__file__`: all four should point inside `VFSTools/scripts`.
