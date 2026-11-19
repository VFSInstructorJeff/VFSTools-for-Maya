"""VFS Tools - Environments.

Baking tools, UV tools and the layer editors (VFS_Environments shelf).

Load / unload from  Windows > Settings/Preferences > Plug-in Manager
All of the real work lives in environments.setup (install / uninstall).
"""
# Import Maya Python API
import maya.api.OpenMaya as om

PLUGIN_VERSION = "2.0.0"

# This is here just so Maya knows to use the new Python API (maya.api.OpenMaya instead of old maya.OpenMaya)
def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    # Create an MFnPlugin obj (registers this plug-in with Maya; its details show up in the Plug-in Manager)
    # Args in order: plugin, vendor, version, required Maya API version ("Any" = no restriction)
    om.MFnPlugin(plugin, "VFS", PLUGIN_VERSION, "Any")
    
    # Set actual functionality through setup file in separate location
    from environments import setup
    setup.install()


def uninitializePlugin(plugin):
    from core import lifecycle
    from environments import setup
    setup.uninstall()
    
    # Forget the cached modules so loading the plug-in again (or after editing code) picks up the changes.
    lifecycle.purge_modules("environments")
