@echo off
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\2023\"
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\2024\"
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\2025\"
xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\2026\"

xcopy /s/y "%cd%\layer_editor_tools" "%userprofile%\Documents\maya\VFSTools\layer_editor_tools\"
xcopy /s/y "%cd%\baking_tools" "%userprofile%\Documents\maya\VFSTools\baking_tools\"
xcopy /s/y "%cd%\uv_tools" "%userprofile%\Documents\maya\VFSTools\uv_tools\"
xcopy /s/y "%cd%\animation_tools" "%userprofile%\Documents\maya\VFSTools\animation_tools\"
xcopy /s/y "%cd%\leveldesign_tools" "%userprofile%\Documents\maya\VFSTools\leveldesign_tools\"

xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\2023\prefs\shelves\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\2024\prefs\shelves\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\2025\prefs\shelves\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\2026\prefs\shelves\"

