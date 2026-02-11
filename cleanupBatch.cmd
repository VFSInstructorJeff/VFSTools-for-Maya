setlocal EnableDelayedExpansion
:: ---------- CONSTANTS ----------
:: Create constants for directories
set "MAYA_SCRIPTS_DIR=%userprofile%\Documents\maya\scripts\"
set "SCRIPT_DIRS=layer_editor_tools baking_tools uv_tools"

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

:: Replace userSetup.py
set "USER_SETUP_DIR=%MAYA_SCRIPTS_DIR%\userSetup.py"
if not exist "%USER_SETUP_DIR%" (
    echo userProfile.py does not exist in %MAYA_SCRIPTS_DIR% folder.
)
if exist "%USER_SETUP_DIR%" (
    echo Deleting userSetup.py...
    del /q "%USER_SETUP_DIR%"
)

:: Purge old shelf and favs
set "SHELF_DIR_2026=%userprofile%\Documents\maya\2026\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2025=%userprofile%\Documents\maya\2025\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2024=%userprofile%\Documents\maya\2024\prefs\shelves\shelf_VFS_Tools.mel"
set "SHELF_DIR_2023=%userprofile%\Documents\maya\2023\prefs\shelves\shelf_VFS_Tools.mel"

set "FAVS_DIR_2023=%userprofile%\Documents\maya\2023\prefs\favs.json"
set "FAVS_DIR_2024=%userprofile%\Documents\maya\2024\prefs\favs.json"
set "FAVS_DIR_2025=%userprofile%\Documents\maya\2025\prefs\favs.json"
set "FAVS_DIR_2026=%userprofile%\Documents\maya\2026\prefs\favs.json"

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
    echo Deleting shelf_VFS_Tools.mel from .../2023/prefs/shelves/ folder
    del /q "%FAVS_DIR_2023%"
) else (
    echo VFS Tools Shelf does not exist in %FAVS_DIR_2023%.
)

if exist "%FAVS_DIR_2024%" (
    echo Deleting shelf_VFS_Tools.mel from .../2023/prefs/shelves/ folder
    del /q "%FAVS_DIR_2024%"
) else (
    echo VFS Tools Shelf does not exist in %FAVS_DIR_2024%.
)

if exist "%FAVS_DIR_2025%" (
    echo Deleting shelf_VFS_Tools.mel from .../2023/prefs/shelves/ folder
    del /q "%FAVS_DIR_2025%"
) else (
    echo VFS Tools Shelf does not exist in %FAVS_DIR_2025%.
)

if exist "%FAVS_DIR_2026%" (
    echo Deleting shelf_VFS_Tools.mel from .../2023/prefs/shelves/ folder
    del /q "%FAVS_DIR_2026%"
) else (
    echo VFS Tools Shelf does not exist in %FAVS_DIR_2026%.
)

:: We ignore Maya.env because we're setting MAYA_ENV_DIR
:: So Maya will ignore all Maya.env files existing outside of the VFSTools folder