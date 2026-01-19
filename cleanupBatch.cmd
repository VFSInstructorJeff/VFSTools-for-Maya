:: ---------- CONSTANTS ----------
setlocal EnableDelayedExpansion
:: Create constants for directories
set "SOURCE_DIR= %~dp0" & :: ...\VFS-Maya-Tools\
set "MAYA_SCRIPTS_DIR=%userprofile%\Documents\maya\scripts\"
set "VFS_TOOLS_DIR=%userprofile%\Documents\maya\VFSTools\"
set "SCRIPT_DIRS=layer_editor_tools baking_tools uv_tools"

:: ---------- FUNCTIONS ----------
:: Purge old VFS tools
FOR %%D in (%SCRIPT_DIRS%) do (
    set "TARGET_DIR=!MAYA_SCRIPTS_DIR!%%D"
    if exist "!TARGET_DIR!" (
        echo Deleting %%D folder
        rmdir /s /q "!TARGET_DIR!"
    ) else (
        echo !TARGET_DIR! does not exist
    )
)

::replaceUserSetup
set "USER_SETUP_DIR=%MAYA_SCRIPTS_DIR%\userSetup.py"
if not exist "%USER_SETUP_DIR%" (
    echo userProfile.py does not exist.
)
if exist "%USER_SETUP_DIR%" (
    echo Deleting userSetup.py
    del /q "%USER_SETUP_DIR%"
)

::purgeOldShelf
set "2026_SHELF_DIR=!%userprofile%!\Documents\maya\2026\prefs\shelves\shelf_VFS_Tools.mel"
set "2025_SHELF_DIR=!%userprofile%!\Documents\maya\2025\prefs\shelves\shelf_VFS_Tools.mel"

if exist ("!2026_SHELF_DIR!") (
    echo Deleting shelf_VFS_Tools.mel from .../2026/prefs/shelves/ folder
    del /q "!2026_SHELF_DIR!"
) else (
    echo VFS Tools Shelf does not exist in !2026_SHELF_DIR!.
)

if exist ("!2025_SHELF_DIR!") (
    echo Deleting shelf_VFS_Tools.mel from .../2025/prefs/shelves/ folder
    del /q "!2025_SHELF_DIR!"
) else (
    echo VFS Tools Shelf does not exist in !2025_SHELF_DIR!.
)



:: We ignore Maya.env because we're setting MAYA_ENV_DIR
:: So Maya will ignore all Maya.env files existing outside of the VFSTools folder