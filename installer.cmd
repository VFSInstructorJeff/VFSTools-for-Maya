@echo off

:: Setting Maya.env directory to load PYTHONPATH, XBMLANGPATH, and MAYA_SHELF_PATH
setx MAYA_ENV_DIR "%userprofile%"\Documents\maya\VFSTools\

:: Cleanup old tools
call cleanupBatch.cmd

:: Copy setup files
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\userSetup.py" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\VFSTools\"

:: Copy VFS Tools files
xcopy /s/y "%cd%\layer_editor_tools" "%userprofile%\Documents\maya\VFSTools\layer_editor_tools\"
xcopy /s/y "%cd%\baking_tools" "%userprofile%\Documents\maya\VFSTools\baking_tools\"
xcopy /s/y "%cd%\uv_tools" "%userprofile%\Documents\maya\VFSTools\uv_tools\"
xcopy /s/y "%cd%\animation_tools" "%userprofile%\Documents\maya\VFSTools\animation_tools\"
xcopy /s/y "%cd%\leveldesign_tools" "%userprofile%\Documents\maya\VFSTools\leveldesign_tools\"
xcopy /s/y "%cd%\modular_kit" "%userprofile%\Documents\maya\VFSTools\modular_kit\"

:: Copy icons and workspaces (organizational/aesthetic stuff mostly)
xcopy /s/y "%cd%\icons" "%userprofile%\Documents\maya\VFSTools\icons\"
xcopy /s/y "%cd%\workspaces" "%userprofile%\Documents\maya\VFSTools\workspaces\"

:: Create favs.json with the relative path
FILE="%userprofile%/Documents/maya/VFSTools/modular_kit""
FILEPATH="${FILE//\\//}"

echo {> favs.json
echo     "favorites": [>> favs.json
echo         "$FILEPATH">> favs.json
echo     ]>> favs.json
echo }>> favs.json

:: Copy favs.json to prefs folder
xcopy /s/y "%cd%\favs.json" "%userprofile%\Documents\maya\2026\prefs\"
xcopy /s/y "%cd%\favs.json" "%userprofile%\Documents\maya\2025\prefs\"