"""VFS Tools - Rigging.

FK/IK switch and mirror tools, Mixamo tools, Karoly Controlly editor (VFS_Rigging shelf).

Load / unload from  Windows > Settings/Preferences > Plug-in Manager
All of the real work lives in rigging.setup (install / uninstall).
"""
import maya.api.OpenMaya as om

PLUGIN_VERSION = "1.3.0"


def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    om.MFnPlugin(plugin, "VFS", PLUGIN_VERSION, "Any")
    
    from rigging import setup
    setup.install()


def uninitializePlugin(plugin):
    from core import lifecycle
    from rigging import setup
    setup.uninstall()
    
    # Forget the cached modules so loading again (or after editing code) picks up the changes.
    lifecycle.purge_modules("rigging")
