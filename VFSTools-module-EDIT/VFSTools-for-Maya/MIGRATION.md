# Migration notes: old layout -> module

## Where everything went

| Old | New | Plug-in |
| --- | --- | --- |
| `animation_tools/` | `scripts/vfstools/rigging/` | rigging |
| `shelf_VFS_Rigging.mel` | `shelves/` | rigging |
| `baking_tools/`, `uv_tools/` | `scripts/vfstools/general/baking`, `.../uv` | general |
| `layer_editor_tools/` (incl. `old/`) | `scripts/vfstools/general/layer_editor/` | general |
| `shelf_VFS_Tools.mel`, `workspaces/Coding.json` | `shelves/`, `workspaces/` | general |
| userSetup: display-layer scriptJobs (`on_scene_change`) | `general/setup.py` | general |
| userSetup: `UCX_name_fix` (was already disabled) | `general/ucx.py` | general |
| `leveldesign_tools/ld_tools.py` | `scripts/vfstools/leveldesign/ld_tools.py` | level design |
| `shelf_VFS_LD.mel`, `workspaces/VFS_LD.json` | `shelves/`, `workspaces/` | level design |
| `VFS_Hotkeys.mhk` + userSetup `load_hotkeys` | `hotkeys/`, `leveldesign/hotkeys.py` | level design |
| userSetup: `import_LD_mats`, `check_mat_duplicates` | `leveldesign/materials.py` | level design |
| userSetup: scene callbacks (namespace merge, material import) | `leveldesign/callbacks.py` | level design |
| `LD_MATS/`, `modular_kit/`, `MayaLDToolsMaterials.ma`, `SM_Manny.*` | `assets/leveldesign/` | level design |
| `icons/` | `icons/` (on `XBMLANGPATH` via the module) | - |
| `Maya.env`, `userSetup.py`, `installer.cmd`, `cleanupBatch.cmd`, `VFSLDWorkspaceEditor.*`, `favs.json` | `legacy/` (replaced) | - |

Python packages are now `vfstools.<category>...` (e.g. `from vfstools.general.uv import ui`).

## Behaviour that changed on purpose

- **Hidden dependencies removed.** 11 LD shelf buttons used `ld` and 3 used `cmds` without importing them, and the legacy display-layer editor's `uiScript` used `layer_editor_tools_ui`. They only worked because `userSetup.py` leaked those names into Maya's global namespace. They now import explicitly.
- **No more per-user absolute paths.** `VFSLDWorkspaceEditor.exe` patched the materials `.ma` and `VFS_LD.json` after copying. Now texture paths are repointed at runtime (`materials.repoint_textures`, which also repairs scenes saved on another machine) and the workspace's `REPLACETHISLINE` is filled in when it is imported. Shelf icons that pointed at `C:/Users/lrenis/...` use bare file names.
- **Content Browser favorite** for the modular kit is *added* to `prefs/favs.json` (the old installer overwrote the file).
- **Hotkeys are reversible.** Loading Level Design remembers your current hotkey set and unloading restores it. Runtime commands left over from an old install are rewritten to the new package path.
- **Failures are no longer silent.** Each setup step is wrapped; a failure prints a traceback and a warning but doesn't stop the other steps.
- **No `MAYA_ENV_DIR` redirect.** The installer removes it.

## Not changed (pre-existing, found while reorganizing)

- `animation_tools/mixamo_animation_editor.py:189` calls `set_controllers_to_default`, which isn't defined anywhere.
- `layer_editor/layer_editor.py` is not imported by anything and has a hardcoded `C:\Users\Public\Repos\...` icon path and an undefined `maya_layers`.
- `layer_editor/old/start.py` uses `cmds` without importing it. `old/addTab.py` runs code at import.
- `ld_tools.py` builds icon paths with `\` separators, so it is Windows-only.
- `ld_tools.py` contains placeholder UI code ("You like food").

## Please verify in Maya (could not be run here)

1. Plug-in Manager lists `vfs_general.py`, `vfs_rigging.py`, `vfs_leveldesign.py`; unticking *Loaded* removes the matching shelf; ticking it brings it back with no duplicate tab.
2. First launch after install loads all three (needs the module's `scripts/userSetup.py` to be executed by Maya).
3. Ctrl+] / Ctrl+[ change the grid step with Level Design loaded, and the previous hotkey set returns after unloading it.
4. New scene / open scene imports the grid materials with working textures.
5. After quitting Maya with a category loaded, check `Documents/maya/<ver>/prefs/shelves/` - Maya may save a copy of the shelf there. It is harmless (loading replaces any same-named tab) but you may want to delete it if you notice stale shelves when a plug-in is off.
6. The `VFS_LD` workspace opens the Content Browser on the modular kit.
