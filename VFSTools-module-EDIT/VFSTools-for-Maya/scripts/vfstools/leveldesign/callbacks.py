"""Scene callbacks owned by the Level Design tools (registered on load, removed on unload)."""
import maya.api.OpenMaya as om
import maya.cmds as cmds

from vfstools.leveldesign import materials

_callback_ids = []


def merge_namespaces_on_import(*args):
    print("Merging namespaces...")
    cmds.namespace(setNamespace=':')
    namespaces = [namespace for namespace in cmds.namespaceInfo(listOnlyNamespaces=True)
                  if namespace != "UI" and namespace != "shared"]
    for namespace in namespaces:
        try:
            cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=True)
        except Exception as e:
            print(f"Could not merge namespace '{namespace}': {e}")


def install():
    remove()   # never register twice
    _callback_ids.append(om.MSceneMessage.addCallback(om.MSceneMessage.kAfterImport, merge_namespaces_on_import))
    _callback_ids.append(om.MSceneMessage.addCallback(om.MSceneMessage.kAfterNew, materials.import_ld_mats))
    _callback_ids.append(om.MSceneMessage.addCallback(om.MSceneMessage.kAfterOpen, materials.import_ld_mats))


def remove():
    for callback_id in _callback_ids:
        om.MMessage.removeCallback(callback_id)
    del _callback_ids[:]
