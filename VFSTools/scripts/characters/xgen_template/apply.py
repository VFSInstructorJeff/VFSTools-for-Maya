"""Applying a template to the scene (create or replace descriptions, convert guides, assign the material) and Clean Start."""

import os
import tempfile
import uuid

import maya.cmds as cmds
import maya.mel as mel
import xgenm as xg
import xgenm.xgGlobal as xgg
import xgenm.xmaya.xgmExternalAPI as xgen_api

from characters.xgen_shader_cleanup import (
    remove_new_unused_hair_physical_nodes,
    snapshot_hair_physical_nodes,
)
from characters.xgen_template.constants import NO_CHANGE_MATERIAL, SELECT_MATERIAL_LABEL
from characters.xgen_template.dialogs import (
    confirm_clean_start,
    confirm_description_replacement,
)
from characters.xgen_template.scene import collect_apply_targets, leaf_name
from characters.xgen_template.template_io import current_palette, load_template


class _TargetDescriptionValidator:
    def __init__(self, palette, description):
        self.action = xg.ADD_TO_EXISTING_PALETTE
        self.palette = palette
        self.description = description

    def __call__(self, _source_description, _source_palette, _index):
        return True, self.description, self.palette


def mel_string(value):
    return '"{}"'.format(value.replace("\\", "\\\\").replace('"', '\\"'))


def convert_curves_to_guides(curves, description):
    """Convert uniquely named curve copies to avoid ambiguous shape lookups."""
    temporary_curves = []
    curve_shapes = []
    name_prefix = "xGenToolsGuideSource_{}".format(uuid.uuid4().hex)
    try:
        for curve_index, curve in enumerate(curves):
            duplicate = cmds.duplicate(
                curve,
                returnRootsOnly=True,
                name="{}_{}".format(name_prefix, curve_index),
            )[0]
            duplicate_path = duplicate
            temporary_curves.append(duplicate_path)

            parented = cmds.parent(duplicate_path, world=True) or []
            if parented:
                duplicate_path = parented[0]
                temporary_curves[-1] = duplicate_path

        transform_indices = {
            leaf_name(transform): index
            for index, transform in enumerate(temporary_curves)
        }
        shape_indices = {}
        shapes = (
            cmds.listRelatives(
                *temporary_curves,
                shapes=True,
                noIntermediate=True,
                fullPath=True,
                type="nurbsCurve",
            )
            or []
            if temporary_curves
            else []
        )
        for shape in shapes:
            transform_name = leaf_name(shape.rsplit("|", 1)[0])
            curve_index = transform_indices[transform_name]
            shape_index = shape_indices.get(curve_index, 0)
            shape_indices[curve_index] = shape_index + 1
            shape_name = "{}_{}_shape{}".format(name_prefix, curve_index, shape_index)
            renamed_shape = cmds.rename(shape, shape_name)
            curve_shapes.append(renamed_shape)

        if not curve_shapes:
            raise RuntimeError(
                "No NURBS curve shapes were available for '{}'.".format(description)
            )

        cmds.select(curve_shapes, replace=True)
        mel.eval("xgmCurveToGuide -d {} -tsp 1 -tsa 0".format(mel_string(description)))
    finally:
        remaining_curves = cmds.ls(temporary_curves, long=True) or []
        if remaining_curves:
            cmds.delete(remaining_curves)


def _hide_description_guides(description):
    """Set all guides for one XGen description to hidden."""
    for guide in xg.descriptionGuides(description) or []:
        visibility_plug = guide + ".visibility"
        if cmds.objExists(visibility_plug):
            cmds.setAttr(visibility_plug, 0)


def _resolve_material_shading_engine(material_name):
    material_name = (material_name or "").strip()
    if material_name in ("", NO_CHANGE_MATERIAL, SELECT_MATERIAL_LABEL):
        return ""

    materials = cmds.ls(material_name, materials=True, long=True) or []
    if len(materials) != 1:
        raise ValueError(
            "Material '{}' is not available in the scene. Refresh the material "
            "list and choose an existing material.".format(material_name)
        )

    shading_engines = (
        cmds.listConnections(
            materials[0],
            source=False,
            destination=True,
            type="shadingEngine",
        )
        or []
    )
    if not shading_engines:
        raise ValueError(
            "Material '{}' has no connected shading group.".format(material_name)
        )
    return shading_engines[0]


def _apply_material_to_collection(palette, shading_engine, descriptions=None):
    """Assign one material to all non-archive descriptions in a single selection."""
    if descriptions is None:
        descriptions = xg.descriptions(palette) or []

    applied_descriptions = [
        description
        for description in descriptions
        if xg.getActive(palette, description, "Primitive") != "ArchivePrimitive"
    ]
    if applied_descriptions:
        cmds.select(applied_descriptions, replace=True)
        cmds.hyperShade(assign=shading_engine)
    return applied_descriptions


def _rebuild_modifier_maps(palette, description):
    """Regenerate the point and clump maps required by imported modifiers."""
    warnings = []
    for module in xg.fxModules(palette, description) or []:
        module_type = xg.fxModuleType(palette, description, module)
        if module_type not in ("ClumpingFXModule", "AnimWiresFXModule"):
            continue

        try:
            density = xg.getAttr("ptDensity", palette, description, module)
            mask = xg.getAttr("ptMask", palette, description, module)
            point_path = xg.getAttr("pointDir", palette, description, module)
            map_path = xg.getAttr("mapDir", palette, description, module)
            texels_per_unit = xg.getAttr("texelsPerUnit", palette, description, module)
            radius_variance = xg.getAttr("radiusVariance", palette, description, module)
            cmds.xgmPoints(
                generatePoints=[float(density), mask],
                module=module,
            )
            cmds.xgmPoints(savePoints=point_path, module=module)
            cmds.xgmClumpMap(
                progressBar=True,
                fxmodule=module,
                mapDir=map_path,
                pointDir=point_path,
                texelsPerUnit=float(texels_per_unit),
                radiusVariance=radius_variance,
                description=description,
            )
        except Exception as error:
            warning = "{} / {}: {}".format(description, module, error)
            warnings.append(warning)
            cmds.warning(
                "[X-GenTools] Could not regenerate modifier maps for {}".format(warning)
            )

    return warnings


def _set_output_renderer(palette, description, output_renderer):
    """Switch the description's output renderer to the one stored in the template (if it stores one)."""
    if not output_renderer:
        return
    renderer_object = xg.getActive(palette, description, "Renderer")
    if not renderer_object or not xg.attrExists(
        "renderer", palette, description, renderer_object
    ):
        raise RuntimeError(
            "Could not find the output renderer setting for '{}'.".format(description)
        )
    if not xg.setAttr(
        "renderer",
        output_renderer,
        palette,
        description,
        renderer_object,
    ):
        raise RuntimeError(
            "Could not set '{}' to '{}' for '{}'.".format(
                renderer_object,
                output_renderer,
                description,
            )
        )


def _refresh_editor_and_preview(palette, created_descriptions):
    """Refresh the XGen editor, rebuild modifier maps and preview. Returns (map_warnings, preview_warning)."""
    map_warnings = []
    preview_warning = ""
    editor = xgg.DescriptionEditor
    try:
        editor.refresh("Full")
        editor.setCurrentPalette(palette)
    except Exception as error:
        warning = "Could not refresh the XGen editor for modifier maps: {}".format(
            error
        )
        map_warnings.append(warning)
        cmds.warning("[X-GenTools] {}".format(warning))
    else:
        for description in created_descriptions:
            try:
                editor.setCurrentDescription(description)
                map_warnings.extend(_rebuild_modifier_maps(palette, description))
            except Exception as error:
                warning = "{}: could not regenerate modifier maps: {}".format(
                    description, error
                )
                map_warnings.append(warning)
                cmds.warning("[X-GenTools] {}".format(warning))

    try:
        editor.setCurrentPalette(palette)
        editor.setCurrentDescription(created_descriptions[-1])
        descriptions = ",".join(
            mel_string(description) for description in created_descriptions
        )
        mel.eval("xgmPreview {{{}}}".format(descriptions))
    except Exception as error:
        preview_warning = str(error)
        cmds.warning(
            "[X-GenTools] Descriptions were applied, but preview failed: {}".format(
                error
            )
        )

    return map_warnings, preview_warning


def apply_template(
    path,
    generation_group,
    guide_group,
    from_prefix,
    to_prefix,
    material="No change",
):
    """Create or replace descriptions from the selected template and scene guides."""
    if not cmds.pluginInfo("xgenToolkit", query=True, loaded=True):
        cmds.loadPlugin("xgenToolkit.mll")

    _, template_data = load_template(path)
    palette = current_palette()
    generation_root, _, targets = collect_apply_targets(
        generation_group,
        guide_group,
        from_prefix,
        to_prefix,
        template_data["includes_guides"],
    )

    existing_descriptions = set(xg.descriptions(palette) or [])
    loaded_descriptions = set(xg.descriptions() or [])
    other_collection_conflicts = [
        target["description"]
        for target in targets
        if target["description"] in loaded_descriptions
        and target["description"] not in existing_descriptions
    ]
    if other_collection_conflicts:
        raise ValueError(
            "These description names already exist in another XGen collection: "
            "{}.".format(", ".join(other_collection_conflicts))
        )

    shading_engine = _resolve_material_shading_engine(material)

    replacements = [
        target["description"]
        for target in targets
        if target["description"] in existing_descriptions
    ]
    if replacements:
        if not confirm_description_replacement(replacements):
            return None

    previous_selection = cmds.ls(selection=True, long=True) or []
    created_descriptions = []
    scene_changed = False
    with tempfile.TemporaryDirectory(prefix="xgen_apply_template_") as temporary_dir:
        preset_path = os.path.join(temporary_dir, "description.xgp")
        with open(preset_path, "w", encoding="utf-8", newline="\n") as preset_file:
            preset_file.write(template_data["xgen_preset"])
        xgen_preset_path = os.path.abspath(preset_path).replace("\\", "/")
        preset_descriptions = xgen_api.base.getAttrFromFile(
            "name", "Description", xgen_preset_path
        )
        if len(preset_descriptions) != 1:
            raise ValueError(
                "Maya could not read a valid description from the XGen preset. "
                "Re-save the template and try again."
            )

        cmds.undoInfo(openChunk=True, chunkName="Apply XGen Template")
        shader_snapshot = snapshot_hair_physical_nodes()
        shader_cleanup_done = False
        try:
            for target in targets:
                target_description = target["description"]
                if target_description in existing_descriptions:
                    scene_changed = True
                    xg.deleteDescription(palette, target_description)

                cmds.select(target["base"], replace=True)
                use_preset_guides = (
                    not target["curves"] and template_data["includes_guides"]
                )
                imported_description = xg.importDescriptionAsPreset(
                    palette,
                    xgen_preset_path,
                    _TargetDescriptionValidator(palette, target_description),
                    guides=use_preset_guides,
                )
                if not imported_description:
                    raise RuntimeError(
                        "Maya could not import the preset for '{}'.".format(
                            target["base_name"]
                        )
                    )
                scene_changed = True
                if imported_description != target_description:
                    raise RuntimeError(
                        "Maya created '{}' instead of the expected description "
                        "'{}'.".format(imported_description, target_description)
                    )

                _set_output_renderer(
                    palette, target_description, template_data["output_renderer"]
                )

                if target["curves"]:
                    convert_curves_to_guides(target["curves"], target_description)

                created_descriptions.append(target_description)

            shader_cleanup_done = True
            remove_new_unused_hair_physical_nodes(shader_snapshot)

            collection_descriptions = xg.descriptions(palette) or []
            for description in collection_descriptions:
                _hide_description_guides(description)
            applied_material_descriptions = (
                _apply_material_to_collection(
                    palette,
                    shading_engine,
                    descriptions=collection_descriptions,
                )
                if shading_engine
                else []
            )
            scene_changed = True
        except Exception as error:
            if not shader_cleanup_done:
                shader_cleanup_done = True
                try:
                    remove_new_unused_hair_physical_nodes(shader_snapshot)
                except Exception as cleanup_error:
                    cmds.warning(
                        "[X-GenTools] Shader cleanup failed during rollback: {}".format(
                            cleanup_error
                        )
                    )
            cmds.undoInfo(closeChunk=True)
            if scene_changed:
                try:
                    cmds.undo()
                except Exception as undo_error:
                    raise RuntimeError(
                        "Apply failed ({}), and Maya could not roll back the scene "
                        "changes ({}).".format(error, undo_error)
                    ) from error
            raise
        else:
            cmds.undoInfo(closeChunk=True)
        finally:
            if previous_selection:
                cmds.select(previous_selection, replace=True)
            else:
                cmds.select(clear=True)

    map_warnings, preview_warning = _refresh_editor_and_preview(
        palette, created_descriptions
    )

    return {
        "descriptions": created_descriptions,
        "replaced": replacements,
        "used_preset_guides": [
            target["description"]
            for target in targets
            if not target["curves"] and template_data["includes_guides"]
        ],
        "map_warnings": map_warnings,
        "preview_warning": preview_warning,
        "applied_material": material if shading_engine else "",
        "material_descriptions": applied_material_descriptions,
        "generation_group": generation_root,
    }


def clean_start():
    """Delete all descriptions in the active XGen collection after confirmation."""
    palette = current_palette()
    descriptions = list(xg.descriptions(palette) or [])
    if not descriptions:
        return []

    if not confirm_clean_start(palette, descriptions):
        return None

    previous_selection = cmds.ls(selection=True, long=True) or []
    deleted_descriptions = []
    cmds.undoInfo(openChunk=True, chunkName="X-GenTools Clean Start")
    try:
        for description in descriptions:
            if not xg.deleteDescription(palette, description):
                raise RuntimeError(
                    "Maya could not delete description '{}'.".format(description)
                )
            deleted_descriptions.append(description)
    except Exception as error:
        cmds.undoInfo(closeChunk=True)
        if deleted_descriptions:
            try:
                cmds.undo()
            except Exception as undo_error:
                raise RuntimeError(
                    "Clean Start failed ({}), and Maya could not restore the "
                    "deleted descriptions ({}).".format(error, undo_error)
                ) from error
        raise
    else:
        cmds.undoInfo(closeChunk=True)
    finally:
        remaining_selection = cmds.ls(previous_selection, long=True) or []
        if remaining_selection:
            cmds.select(remaining_selection, replace=True)
        else:
            cmds.select(clear=True)

    editor = xgg.DescriptionEditor
    if editor:
        try:
            editor.refresh("Full")
            editor.setCurrentPalette(palette)
        except Exception as error:
            raise RuntimeError(
                "Descriptions were deleted, but Maya could not refresh the XGen "
                "editor: {}".format(error)
            ) from error

    return deleted_descriptions
