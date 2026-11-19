"""Safely remove unused hair-physical shader nodes created during XGen work.

``snapshot_hair_physical_nodes`` records the scene's shader, shading-engine, and
material-info nodes before an operation. ``remove_new_unused_hair_physical_nodes``
compares the scene with that snapshot and deletes only newly created shader
networks that have no connections to unrelated scene nodes and no assigned or
unexpectedly connected shading group. It also removes orphaned material-info
nodes and warns when a network is preserved for safety.
"""

import maya.cmds as cmds


def snapshot_hair_physical_nodes():
    return {
        "shaders": set(cmds.ls(type="hairPhysicalShader") or []),
        "shading_engines": set(cmds.ls(type="shadingEngine") or []),
        "material_infos": set(cmds.ls(type="materialInfo") or []),
    }


def remove_new_unused_hair_physical_nodes(snapshot):
    new_shaders = set(cmds.ls(type="hairPhysicalShader") or [])
    new_shaders.difference_update(snapshot["shaders"])
    new_shading_engines = set(cmds.ls(type="shadingEngine") or [])
    new_shading_engines.difference_update(snapshot["shading_engines"])
    new_material_infos = set(cmds.ls(type="materialInfo") or [])
    new_material_infos.difference_update(snapshot["material_infos"])

    removed = []
    for shader in sorted(new_shaders):
        connected_nodes = set(
            cmds.listConnections(
                shader, source=True, destination=True
            ) or []
        )
        shading_engines = set(
            cmds.listConnections(
                shader,
                source=False,
                destination=True,
                type="shadingEngine",
            ) or []
        ).intersection(new_shading_engines)
        material_infos = set(
            cmds.listConnections(
                shader,
                source=True,
                destination=True,
                type="materialInfo",
            ) or []
        ).intersection(new_material_infos)
        owned_nodes = shading_engines.union(material_infos)

        if connected_nodes.difference(owned_nodes):
            cmds.warning(
                "[XGen shader cleanup] Preserved '{}' because it connects to "
                "pre-existing or unrelated scene nodes.".format(shader)
            )
            continue

        safe_shading_engines = []
        for shading_engine in sorted(shading_engines):
            members = cmds.sets(shading_engine, query=True) or []
            surface_shaders = cmds.listConnections(
                shading_engine + ".surfaceShader",
                source=True,
                destination=False,
            ) or []
            if members or set(surface_shaders) != {shader}:
                cmds.warning(
                    "[XGen shader cleanup] Preserved '{}' because its shading "
                    "group '{}' is assigned or has an unexpected connection."
                    .format(shader, shading_engine)
                )
                safe_shading_engines = None
                break
            safe_shading_engines.append(shading_engine)

        if safe_shading_engines is None:
            continue

        cmds.delete([shader] + safe_shading_engines)
        for material_info in sorted(material_infos):
            if (
                cmds.objExists(material_info)
                and not (
                    cmds.listConnections(
                        material_info,
                        source=True,
                        destination=True,
                    )
                    or []
                )
            ):
                cmds.delete(material_info)
        removed.append(shader)

    return removed
