"""VFS Tools - Level Design.

VFS_LD shelf, grid materials, scene callbacks, VFS hotkey set and the modular kit workspace.

Load / unload from  Windows > Settings/Preferences > Plug-in Manager
All of the real work lives in vfstools.leveldesign.setup (install / uninstall).
"""
import maya.api.OpenMaya as om

PLUGIN_VERSION = "1.3.0"


def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    om.MFnPlugin(plugin, "VFS", PLUGIN_VERSION, "Any")
    
    from vfstools.leveldesign import setup
    setup.install()


def uninitializePlugin(plugin):
    from vfstools.core import lifecycle
    from vfstools.leveldesign import setup
    setup.uninstall()
    
    # Forget the cached modules so loading again (or after editing code) picks up the changes.
    lifecycle.purge_modules("vfstools.leveldesign")
