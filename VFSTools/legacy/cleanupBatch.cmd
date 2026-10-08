setlocal EnableDelayedExpansion

:: ---------- CONSTANTS ----------
:: Create constants for directories
set "MAYA_SCRIPTS_DIR=%userprofile%\Documents\maya\scripts\"
set "SCRIPT_DIRS=layer_editor_tools baking_tools uv_tools"
set "VFS_SCRIPTS_DIR=%userprofile%\Documents\maya\VFSTools\"
set "VFS_SCRIPT_DIRS=animation_tools baking_tools icons layer_editor_tools LD_MATS leveldesign_tools modular_kit uv_tools workspaces"

:: ---------- FUNCTIONS ----------
:: Purge old VFS tools
FOR %%D in (%SCRIPT_DIRS%) do (
    set "TARGET_DIR=!MAYA_SCRIPTS_DIR!%%D"
    if exist "!TARGET_DIR!" (
        echo Deleting %%D folder...
        rmdir /s /q "!TARGET_DIR!"
    ) else (
        echo !TARGET_DIR! does not exist.
    )
)

:: Purge new VFS tools since we're replacing them anyway
FOR %%D in (%VFS_SCRIPT_DIRS%) do (
    set "TARGET_DIR=!VFS_SCRIPTS_DIR!%%D"
    if exist "!TARGET_DIR!" (
        echo Deleting %%D folder...
        rmdir /s /q "!TARGET_DIR!"
    ) else (
        echo !TARGET_DIR! does not exist.
    )
)

:: Replace userSetup.py
set "USER_SETUP_DIR=%MAYA_SCRIPTS_DIR%\userSetup.py"
if not exist "%USER_SETUP_DIR%" (
    echo userProfile.py does not exist in %MAYA_SCRIPTS_DIR% folder.
)
if exist "%USER_SETUP_DIR%" (
    echo Deleting userSetup.py...
    del /q "%USER_SETUP_DIR%"
)

:: Purge old shelf, favs, workspaces, and hotkeys
set "SHELF_DIR_2026=%userprofile%\Documents\maya\2026\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2025=%userprofile%\Documents\maya\2025\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2024=%userprofile%\Documents\maya\2024\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2023=%userprofile%\Documents\maya\2023\prefs\shelves\shelf_VFS_Tools.mel"

set "FAVS_DIR_2023=%userprofile%\Documents\maya\2023\prefs\favs.json"
set "FAVS_DIR_2024=%userprofile%\Documents\maya\2024\prefs\favs.json"
set "FAVS_DIR_2025=%userprofile%\Documents\maya\2025\prefs\favs.json"
set "FAVS_DIR_2026=%userprofile%\Documents\maya\2026\prefs\favs.json"

set "WORKSPACE_DIR_2023=%userprofile%\Documents\maya\2023\prefs\workspaces\*"
set "WORKSPACE_DIR_2024=%userprofile%\Documents\maya\2024\prefs\workspaces\*"
set "WORKSPACE_DIR_2025=%userprofile%\Documents\maya\2025\prefs\workspaces\*"
set "WORKSPACE_DIR_2026=%userprofile%\Documents\maya\2026\prefs\workspaces\*"

:: Delete all files in workspace directories
if exist %WORKSPACE_DIR_2023% (
    del /S /Q %WORKSPACE_DIR_2023%
    echo Deleting workspaces from .../2023/prefs/workspaces/ folder
) else (
    echo No workspaces in .../2023/prefs/workspaces/ folder
)
if exist %WORKSPACE_DIR_2024% (
    del /S /Q %WORKSPACE_DIR_2024%
    echo Deleting workspaces from .../2024/prefs/workspaces/ folder
) else (
    echo No workspaces in .../2024/prefs/workspaces/ folder
)
if exist %WORKSPACE_DIR_2025% (
    del /S /Q %WORKSPACE_DIR_2025%
    echo Deleting workspaces from .../2025/prefs/workspaces/ folder
) else (
    echo No workspaces in .../2025/prefs/workspaces/ folder
)
if exist %WORKSPACE_DIR_2026% (
    del /S /Q %WORKSPACE_DIR_2026%
    echo Deleting workspaces from .../2026/prefs/workspaces/ folder
) else (
    echo No workspaces in .../2026/prefs/workspaces/ folder
)

:: Delete shelf files
if exist "%SHELF_DIR_2026%" (
    echo Deleting shelf_VFS_Tools.mel from .../2026/prefs/shelves/ folder
    del /q %SHELF_DIR_2026%
) else (
    echo VFS Tools Shelf does not exist in %SHELF_DIR_2026%.
)

if exist "%SHELF_DIR_2025%" (
    echo Deleting shelf_VFS_Tools.mel from .../2025/prefs/shelves/ folder
    del /q "%SHELF_DIR_2025%"
) else (
    echo VFS Tools Shelf does not exist in %SHELF_DIR_2025%.
)

if exist "%SHELF_DIR_2024%" (
    echo Deleting shelf_VFS_Tools.mel from .../2024/prefs/shelves/ folder
    del /q "%SHELF_DIR_2024%"
) else (
    echo VFS Tools Shelf does not exist in %SHELF_DIR_2024%.
)

if exist "%SHELF_DIR_2023%" (
    echo Deleting shelf_VFS_Tools.mel from .../2023/prefs/shelves/ folder
    del /q "%SHELF_DIR_2023%"
) else (
    echo VFS Tools Shelf does not exist in %SHELF_DIR_2023%.
)

:: Purging all favs

if exist "%FAVS_DIR_2023%" (
    echo Deleting favs.json from .../2023/prefs/ folder
    del /q "%FAVS_DIR_2023%"
) else (
    echo favs.json does not exist in %FAVS_DIR_2023%.
)

if exist "%FAVS_DIR_2024%" (
    echo Deleting favs.json from .../2024/prefs/ folder
    del /q "%FAVS_DIR_2024%"
) else (
    echo favs.json does not exist in %FAVS_DIR_2024%.
)

if exist "%FAVS_DIR_2025%" (
    echo Deleting favs.json from .../2025/prefs/ folder
    del /q "%FAVS_DIR_2025%"
) else (
    echo favs.json does not exist in %FAVS_DIR_2025%.
)

if exist "%FAVS_DIR_2026%" (
    echo Deleting favs.json from .../2026/prefs/ folder
    del /q "%FAVS_DIR_2026%"
) else (
    echo favs.json does not exist in %FAVS_DIR_2026%.
)

:: Purging all hotkey folders

if exist "%HKEYS_DIR_2023%" (
    echo Deleting files from .../2023/prefs/hotkeys folder
    del /F /S /Q "%HKEYS_DIR_2023%"
) else (
    echo 2023 hotkeys folder is empty.
)

if exist "%HKEYS_DIR_2024%" (
    echo Deleting files from .../2024/prefs/hotkeys folder
    del /F /S /Q "%HKEYS_DIR_2024%"
) else (
    echo 2024 hotkeys folder is empty.
)

if exist "%HKEYS_DIR_2025%" (
    echo Deleting files from .../2025/prefs/hotkeys folder
    del /F /S /Q "%HKEYS_DIR_2025%"
) else (
    echo 2025 hotkeys folder is empty.
)

if exist "%HKEYS_DIR_2026%" (
    echo Deleting files from .../2026/prefs/hotkeys folder
    del /F /S /Q "%HKEYS_DIR_2026%"
) else (
    echo 2026 hotkeys folder is empty.
)
:: We ignore Maya.env because we're setting MAYA_ENV_DIR
:: So Maya will ignore all Maya.env files existing outside of the VFSTools folder