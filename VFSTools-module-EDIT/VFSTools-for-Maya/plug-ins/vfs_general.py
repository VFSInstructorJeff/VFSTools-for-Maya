"""VFS Tools - General.

Baking tools, UV tools and the layer editors (VFS_Tools shelf, Coding workspace).

Load / unload from  Windows > Settings/Preferences > Plug-in Manager
All of the real work lives in vfstools.general.setup (install / uninstall).
"""
# Import Maya Python API
import maya.api.OpenMaya as om

PLUGIN_VERSION = "1.3.0"

# This is here just so Maya knows to use the new Python API (maya.api.OpenMaya instead of old maya.OpenMaya)
def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    # Create an MFnPlugin obj (Maya plug-in manager)
    # Args in order: plugin, author, version, compatibility/platform info
    om.MFnPlugin(plugin, "VFS", PLUGIN_VERSION, "Any")
    
    # Set actual functionality through setup file in separate location
    from vfstools.general import setup
    setup.install()


def uninitializePlugin(plugin):
    from vfstools.core import lifecycle
    from vfstools.general import setup
    setup.uninstall()
    
    # Forget the cached modules so loading the plug-in again (or after editing code) picks up the changes.
    lifecycle.purge_modules("vfstools.general")
