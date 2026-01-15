:: BATCH VERSION OF CLEANUP.PY
:: ---------- CONSTANTS ----------
:: Create constants that we'll use for searching
SET PYTHONPATH= PYTHONPATH
SET PYTHONPATH_STRING= %userprofile%\Documents\maya\VFSTools\
SET XBMLANGPATH= XBMLANGPATH
SET XBMLANGPATH_STRING= %userprofile%\Documents\maya\VFSTools\icons\
SET OLD_USER_SETUP_FILTER= layer_editor_tools
:: Create constants for directories
SET SOURCE_DIR= %~dp0 & :: ...\VFS-Maya-Tools\
SET MAYA_ENV_PATH= %userprofile%\Documents\maya\VFSTools\Maya.env
SET MAYA_SCRIPTS_DIR= %userprofile%\Documents\maya\scripts\
SET VFS_TOOLS_DIR=  %userprofile%\Documents\maya\VFSTools\
SET SCRIPT_DIRS= layer_editor_tools baking_tools uv_tools

:: ---------- FUNCTIONALITY/EXECUTION ----------
:: Purge old VFS tool folders in .../maya/scripts/
:: Purge userSetup.py located in .../maya/scripts/ IF it contains old VFS Tools
CALL :purgeOldVFSTools 

:: Check if Maya.env exists, if it's empty, and if it has extra content
with open(MAYA_ENV_PATH, 'r') as envfile:               # Open the Maya.env file
    if FileNotFoundError:                               # If the file doesn't exist
        print(f"File at {MAYA_ENV_PATH} doesn't exist!")
        shutil.copy(SOURCE_DIR + r"\Maya.env", MAYA_ENV_PATH)
    else:
        lines = envfile.readlines()                     # If the file exists, put all lines in a list
        if not lines:                                   # If there aren't any lines (if the file is empty)
            print(f"File exists in {MAYA_ENV_PATH}, but it's empty!")
            shutil.copy(SOURCE_DIR + r"\Maya.env", MAYA_ENV_PATH)
        else:
            isVFSToolsThere(lines, PYTHONPATH, PYTHONPATH_STRING)   # If the file isn't empty, check for VFSTools
            isVFSToolsThere(lines, XBMLANGPATH, XBMLANGPATH_STRING)

:: ---------- METHODS/FUNCTIONS ----------
:: Create a method to go through userSetup.py file in .../maya/scripts/ and look for old VFSTools remains
:userSetup
SETLOCAL
SET userSetupFile= %MAYA_SCRIPTS_DIR%userSetup.py
FIND %OLD_USER_SETUP_FILTER% %userSetupFile%
if ErrorLevel 1
:: read lines from file
:: parse through lines, if match found
:: remove file

def userSetup(userSetupPath):
    with open(userSetupPath, 'r') as file:
        userSetupLines = file.readlines()                       # get all userSetup.py lines
        if OLD_USER_SETUP_FILTER in userSetupLines:             # if userSetup.py contains "layer_editor_tools"
            os.remove(userSetupPath)                            # Remove the file
            print(f"Deleted file: {file}")
        else:
            return

:: Create a method to go through the Maya directory and delete any old versions of the VFS-Maya-Tools
:purgeOldVFSTools
def purgeOldVFSTools():
    for filename in os.listdir(MAYA_SCRIPTS_DIR):               # List all files in .../maya/scripts/ directory
        file_path = os.path.join(MAYA_SCRIPTS_DIR, filename)
    if os.path.isfile(file_path):                               # Check if it is a file (not a subdirectory)
        if filename == "userSetup.py":                          # If file is called userSetup.py
            userSetup()                                         # Call our userSetup method to check if it has old VFS Tools remains
    for dir in SCRIPT_DIRS:
        path = os.path.join(MAYA_SCRIPTS_DIR, dir)
        shutil.rmtree(path)

:: Create a method to go through the lines in a file and look for our PYTHONPATH or XBMLANGPATH constants
:isVFSToolsThere
def isVFSToolsThere(filelines, envVar, envVarStr):
    envpath_check = False
    for line in filelines:                      # Iterate through each line of the file
        if envVar in line:                      # Check if PYTHONPATH or XBMLANGPATH variable is there
            envpath_check = True        
            if envVarStr in line:               # Check if our VFS PYTHONPATH or XBMLANGPATH variable is there
                print(f"{envVarStr} is already here, nothing added!")
                return                          # If it is, don't do anything
            else:
                line + ";"  + envVarStr         # If it isn't, add OUR variable
                print(f"{envVarStr} was added!")
                return
    if envpath_check == False:                          # If PYTHONPATH or XBMLANGPATH variable isn't there
        filelines.append(envVar + " = " + envVarStr)    # Add it and add the path to VFSTools
        print(f"{envVar} was added!")
        return