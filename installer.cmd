@echo off

:: Setting Maya.env directory to load PYTHONPATH (scripts), XBMLANGPATH (icons), and MAYA_SHELF_PATH (shelves)
setx MAYA_ENV_DIR "%userprofile%"\Documents\maya\VFSTools\

:: Cleanup old tools (Deletes everything we've added and files we've modified. We're completely wiping it, so if any other installed tools also modified the file, they'll have to be reinstalled.)
call cleanupBatch.cmd

:: Copy setup files
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\userSetup.py" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\VFSTools\"

:: Copy VFS Tools folders
xcopy /s/y "%cd%\layer_editor_tools" "%userprofile%\Documents\maya\VFSTools\layer_editor_tools\"
xcopy /s/y "%cd%\baking_tools" "%userprofile%\Documents\maya\VFSTools\baking_tools\"
xcopy /s/y "%cd%\uv_tools" "%userprofile%\Documents\maya\VFSTools\uv_tools\"
xcopy /s/y "%cd%\animation_tools" "%userprofile%\Documents\maya\VFSTools\animation_tools\"
xcopy /s/y "%cd%\leveldesign_tools" "%userprofile%\Documents\maya\VFSTools\leveldesign_tools\"
xcopy /s/y "%cd%\modular_kit" "%userprofile%\Documents\maya\VFSTools\modular_kit\"

:: Fix workspaces absolute paths
call VFSLDWorkspaceEditor.exe

:: Copy icons and workspaces (organizational/aesthetic stuff mostly)
xcopy /s/y "%cd%\icons" "%userprofile%\Documents\maya\VFSTools\icons\"
xcopy /s/y "%cd%\workspaces" "%userprofile%\Documents\maya\VFSTools\workspaces\"

:: Create favs.json with the relative path to add our Modular kit to the favorites tab in the Content Browser
SET "FILEPATH=%userprofile%/Documents/maya/VFSTools/modular_kit"
echo {> favs.json
echo     "favorites": [>> favs.json
echo         "%FILEPATH:\=/%">> favs.json
echo     ]>> favs.json
echo }>> favs.json

:: Copy our favs.json to prefs folder (I haven't been able to redirect this one because it would mean changing the entire Maya application folder location, but it could be done by setting MAYA_APP_DIR)
xcopy /s/y "%cd%\favs.json" "%userprofile%\Documents\maya\2026\prefs\"
xcopy /s/y "%cd%\favs.json" "%userprofile%\Documents\maya\2025\prefs\"

pause