'''
### SUMMARY ###
This script is made for cleaning up the older version of the VFS-Maya-Tools.
This way, users won't risk having multiple versions of the tools in their files.
It wouldn't be accessible through Maya itself, but this way the Maya files and folders are cleaner.

### HOW IT WORKS ###
1. Goes through the Maya folders, removes any VFS Tools that aren't in the VFSTools designated folder
2. For each version of Maya (2025, 2026, etc.), checks the if the Maya.env file can be appended to,
ovewritten, or entirely added.
    2.5 This is done so if the user has any scripts/plugins/modules that alter the Maya.env file, we won't
    overwrite it and/or possibly break it.
'''

# ---------- IMPORTS/LIBRARIES/MODULES ----------
from pathlib import Path
import shutil
import os

# ---------- VARIABLES ----------
# Create a list with all the paths the Maya.env file can be
env_path_2023 = r"%userProfile%\Documents\maya\2023\Maya.env"
env_path_2024 = r"%userProfile%\Documents\maya\2024\Maya.env"
env_path_2025 = r"%userProfile%\Documents\maya\2025\Maya.env"
env_path_2026 = r"%userProfile%\Documents\maya\2026\Maya.env"
env_path_list = [env_path_2023, env_path_2024, env_path_2025, env_path_2026]

# ---------- CONSTANTS ----------
# Create constants that we'll use for searching
PYTHONPATH = "PYTHONPATH"
PYTHONPATH_STRING = r"%userprofile%\Documents\maya\VFSTools"
XBMLANGPATH = "XBMLANGPATH"
XBMLANGPATH_STRING = r"%userprofile%\Documents\maya\VFSTools\icons"
# Create constants for directories
SOURCE_DIR = Path.cwd() # Get the directory where this script is (...\VFSTools-For-Maya\)

# ---------- METHODS/FUNCTIONS ----------
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
for path in env_path_list:                      # For each version of Maya
    with open(path, 'r') as envfile:            # Open the Maya.env file
        if FileNotFoundError:                   # If the file doesn't exist
            print(f"File at {path} doesn't exist!")
            # COPY FILE FROM CURRENT FOLDER TO DESTINATION FOLDER (!)
            break
        else:
            lines = envfile.readlines()         # If the file exists, put all lines in a list
            if not lines:                       # If there aren't any lines (if the file is empty)
                print(f"File exists in {path}, but it's empty!")
                # COPY FILE FROM CURRENT FOLDER TO DESTINATION FOLDER (!)
                break
            else:
                isVFSToolsThere(lines, PYTHONPATH, PYTHONPATH_STRING)   # If the file isn't empty, check for VFSTools
                isVFSToolsThere(lines, XBMLANGPATH, XBMLANGPATH_STRING)


# check other folders for old stuff
    # if there's old stuff, delete it
    # if there isn't continue

# if the file is empty, just xcopy
# if the file has the same value as the xcopy, xcopy
# if the file is different, do stuff