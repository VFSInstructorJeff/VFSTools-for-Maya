@echo off

setx MAYA_ENV_DIR "%userprofile%"\Documents\maya\VFSTools\

call cleanupBatch.cmd

xcopy /s/y "%cd%\Maya.env" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\userSetup.py" "%userprofile%\Documents\maya\VFSTools\"
xcopy /s/y "%cd%\shelf_VFS_Tools.mel" "%userprofile%\Documents\maya\VFSTools\"

xcopy /s/y "%cd%\layer_editor_tools" "%userprofile%\Documents\maya\VFSTools\layer_editor_tools\"
xcopy /s/y "%cd%\baking_tools" "%userprofile%\Documents\maya\VFSTools\baking_tools\"
xcopy /s/y "%cd%\uv_tools" "%userprofile%\Documents\maya\VFSTools\uv_tools\"
xcopy /s/y "%cd%\animation_tools" "%userprofile%\Documents\maya\VFSTools\animation_tools\"
xcopy /s/y "%cd%\leveldesign_tools" "%userprofile%\Documents\maya\VFSTools\leveldesign_tools\"
xcopy /s/y "%cd%\icons" "%userprofile%\Documents\maya\VFSTools\icons\"