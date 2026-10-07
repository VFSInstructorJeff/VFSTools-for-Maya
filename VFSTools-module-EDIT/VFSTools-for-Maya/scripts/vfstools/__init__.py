"""VFS Tools for Maya.

Layout
------
vfstools.core          shared helpers (paths, shelf/workspace/favorites helpers, lifecycle)
vfstools.general       baking, UV and layer-editor tools        -> plug-in  vfs_general.py
vfstools.rigging       rigging / animation tools                -> plug-in  vfs_rigging.py
vfstools.leveldesign   level-design tools, materials, hotkeys   -> plug-in  vfs_leveldesign.py

Each category exposes setup.install() / setup.uninstall(); the plug-ins in plug-ins/ call them,
which is what makes the categories loadable/unloadable from the Plug-in Manager.
"""
