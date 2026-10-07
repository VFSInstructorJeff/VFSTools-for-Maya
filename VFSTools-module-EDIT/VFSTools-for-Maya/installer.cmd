:: Don't print out commands, including the echo off one
@echo off
:: Make all environment variable changes local to this file
setlocal

:: Get this file's full path to parent directory (doesn't include this file in the path)
set "MODULE_DIR=%~dp0"
:: If the last character of the path is \, remove it
if "%MODULE_DIR:~-1%"=="\" set "MODULE_DIR=%MODULE_DIR:~0,-1%"

:: Set the Maya modules directory
set "MODS_DIR=%userprofile%\Documents\maya\modules"
:: If that directory doesn't exist, create it
if not exist "%MODS_DIR%" mkdir "%MODS_DIR%"

:: > means we're creating/writing to a file (or overriding it) (if we didn't want to override, we should use >>, since >> only appends)
:: We're writing to the .mod file we made in the Maya modules dir
:: And we're registering this dir as the module dir
> "%MODS_DIR%\VFSTools.mod" echo + VFSTools 1.3.0 %MODULE_DIR%
echo Registered module: %MODULE_DIR%
echo Wrote: %MODS_DIR%\VFSTools.mod

:: The old installer redirected Maya.env through the MAYA_ENV_DIR variable. Remove it so the old
:: userSetup.py / Maya.env in Documents\maya\VFSTools stops loading alongside the new plug-ins.
:: Remove MAYA_ENV_DIR var since we don't need it anymore now that we're using the module/plug-in approach
:: In the windows directory, in the section that belongs to the current Windows user, look for MAYA_ENV_DIR
:: >nul means no regular output, 2>&1 means send error output to the same place as regular output (nothing/null/don't show)
reg query "HKCU\Environment" /v MAYA_ENV_DIR >nul 2>&1
:: 0 = sucess, !0 means error
:: if not !0 (so if 0/sucess), force delete the variable we found
if not errorlevel 1 (
    reg delete "HKCU\Environment" /v MAYA_ENV_DIR /f >nul
    echo Removed the old MAYA_ENV_DIR setting.
)

echo.
echo Module creation DONE.
pause
