"""VFS Tools - Characters.

XGen hair-card tools: the X-Gen Template Tool (VFS_Characters shelf).

Load / unload from  Windows > Settings/Preferences > Plug-in Manager
All of the real work lives in characters.setup (install / uninstall).
"""
import maya.api.OpenMaya as om

PLUGIN_VERSION = "2.0.0"


def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    om.MFnPlugin(plugin, "VFS", PLUGIN_VERSION, "Any")

    from characters import setup
    setup.install()


def uninitializePlugin(plugin):
    from core import lifecycle
    from characters import setup
    setup.uninstall()

    # Forget the cached modules so loading again (or after editing code) picks up the changes.
    lifecycle.purge_modules("characters")
