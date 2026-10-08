:: Don't print out commands, including the echo off one
@echo off
:: Make all environment variable changes local to this file
setlocal

:: The module is the VFSTools folder that sits next to this file (the folder this file is in already ends in a backslash)
set "MODULE_DIR=%~dp0VFSTools"
:: Make sure that folder is really there before registering it. It won't be if installer.cmd was moved out of VFSTools-for-Maya
if not exist "%MODULE_DIR%\plug-ins" (
    echo Could not find the VFSTools folder next to installer.cmd. Keep installer.cmd inside VFSTools-for-Maya, next to the VFSTools folder.
    pause
    exit /b 1
)

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
:: In the Windows registry, in the section that belongs to the current Windows user, look for MAYA_ENV_DIR
:: >nul means no regular output, 2>&1 means send error output to the same place as regular output (nothing/null/don't show)
reg query "HKCU\Environment" /v MAYA_ENV_DIR >nul 2>&1
:: 0 = success, !0 means error
:: if not !0 (so if 0/success), force delete the variable we found
if not errorlevel 1 (
    reg delete "HKCU\Environment" /v MAYA_ENV_DIR /f >nul
    echo Removed the old MAYA_ENV_DIR setting. If Maya still loads the old tools, sign out and back in.
)

echo.
echo Module creation DONE.
pause
