'''
### SUMMARY ###
This script is made for cleaning up the older version of the VFS-Maya-Tools.
This way, users won't risk having multiple versions of the tools in their files.
It wouldn't be accessible through Maya itself, but this way the Maya files and folders are cleaner.

### HOW IT WORKS ###
1. Goes through the Maya folders, removes any VFS Tools that aren't in the VFSTools designated folder
2. Checks the if the Maya.env file can be appended to, ovewritten, or entirely added.
    2.1 This is done so if the user has any scripts/plugins/modules that alter the Maya.env file, we won't
    overwrite it and/or possibly break it.
3. The same goes for userSetup.py
'''

# ---------- IMPORTS/LIBRARIES/MODULES ----------
from pathlib import Path
import shutil
import os

# ---------- CONSTANTS ----------
# Create constants that we'll use for searching
PYTHONPATH = "PYTHONPATH"
PYTHONPATH_STRING = r"%userprofile%\Documents\maya\VFSTools"
XBMLANGPATH = "XBMLANGPATH"
XBMLANGPATH_STRING = r"%userprofile%\Documents\maya\VFSTools\icons"
# Create constants for directories
SOURCE_DIR = Path.cwd() # Get the directory where this script is (...\VFSTools-For-Maya\)
MAYA_ENV_PATH = os.path.expanduser('~') + r"\Documents\maya\VFSTools\Maya.env"
MAYA_SCRIPTS_DIR = os.path.expanduser('~') + r"\Documents\maya\scripts"
VFS_TOOLS_DIR =  os.path.expanduser('~') + r"\Documents\maya\VFSTools"
SCRIPT_DIRS = ["layer_editor_tools", "baking_tools", "uv_tools"]

# ---------- METHODS/FUNCTIONS ----------
# Create a method to check the contents of userSetup.py (!)
def userSetup(userSetupPath):
    with open(userSetupPath, 'a'):
        
        pass

# Create a method to go through the Maya directory and delete any old versions of the VFS-Maya-Tools
def purgeOldVFSTools():
    # List all files in the directory
    for filename in os.listdir(MAYA_SCRIPTS_DIR):
        file_path = os.path.join(MAYA_SCRIPTS_DIR, filename)
    
    # Check if it is a file (not a subdirectory)
    if os.path.isfile(file_path):
        if filename == "userSetup.py":
            userSetup(file_path)
            os.remove(file_path)  # Remove the file
            print(f"Deleted file: {filename}")
    for dir in SCRIPT_DIRS:
        if os.path.isfile(file_path):
            os.remove(file_path)  # Remove the file
        else:
            path = os.path.join(MAYA_SCRIPTS_DIR, dir)
            shutil.rmtree(path)
    pass

# Create a method to go through the lines in a file and look for our PYTHONPATH or XBMLANGPATH constants 
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
        
# ---------- FUNCTIONALITY/EXECUTION ----------
# Run the script and change all Maya.env files

with open(MAYA_ENV_PATH, 'r') as envfile:               # Open the Maya.env file
    if FileNotFoundError:                               # If the file doesn't exist
        print(f"File at {MAYA_ENV_PATH} doesn't exist!")
        shutil.copytree(SOURCE_DIR, VFS_TOOLS_DIR)
        # COPY FILE FROM CURRENT FOLDER TO DESTINATION FOLDER (!)
    else:
        lines = envfile.readlines()                     # If the file exists, put all lines in a list
        if not lines:                                   # If there aren't any lines (if the file is empty)
            print(f"File exists in {MAYA_ENV_PATH}, but it's empty!")
            # COPY FILE FROM CURRENT FOLDER TO DESTINATION FOLDER (!)
        else:
            isVFSToolsThere(lines, PYTHONPATH, PYTHONPATH_STRING)   # If the file isn't empty, check for VFSTools
            isVFSToolsThere(lines, XBMLANGPATH, XBMLANGPATH_STRING)


# check other folders for old stuff
    # if there's old stuff, delete it
    # if there isn't continue

# if the file is empty, just xcopy
# if the file has the same value as the xcopy, xcopy
# if the file is different, do stuff