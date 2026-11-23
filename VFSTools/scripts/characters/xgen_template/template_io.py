"""Saving and loading the template .json files."""

import json
import os
import tempfile

import maya.cmds as cmds
import xgenm as xg
import xgenm.xgGlobal as xgg

from characters.xgen_template.constants import DEFAULT_XGEN_OUTPUT_RENDERER
from characters.xgen_template.dialogs import confirm_template_overwrite
from characters.xgen_template.paths import resolve_template_path, templates_folder


def choose_template_save_path():
    template_directory = templates_folder()
    if not os.path.isdir(template_directory):
        os.makedirs(template_directory)

    selected = cmds.fileDialog2(
        fileMode=0,
        dialogStyle=2,
        caption="Save XGen Template",
        okCaption="Save",
        fileFilter="JSON Files (*.json)",
        startingDirectory=template_directory,
    )
    if not selected:
        return ""
    return resolve_template_path(selected[0])


def current_description():
    editor = xgg.DescriptionEditor
    if editor:
        palette = editor.currentPalette()
        description = editor.currentDescription()
        if palette and description:
            return palette, description

    raise RuntimeError(
        "Open the XGen Description Editor and select a description to save."
    )


def current_palette():
    editor = xgg.DescriptionEditor
    palette = editor.currentPalette() if editor else ""
    if not palette:
        raise RuntimeError(
            "Open the XGen Description Editor and select a collection to apply to."
        )
    return palette


def _description_output_renderer(palette, description):
    renderer_object = xg.getActive(palette, description, "Renderer")
    if not renderer_object or not xg.attrExists(
        "renderer", palette, description, renderer_object
    ):
        return ""
    return xg.getAttr("renderer", palette, description, renderer_object)


def save_template(path, allow_overwrite=True, confirm_overwrite=False):
    """Export the active description preset and store it inside a JSON file."""
    if not cmds.pluginInfo("xgenToolkit", query=True, loaded=True):
        cmds.loadPlugin("xgenToolkit.mll")

    palette, description = current_description()
    output_path = resolve_template_path(path)
    if os.path.isdir(output_path):
        raise ValueError("The selected template path is a folder, not a file.")

    if os.path.exists(output_path):
        if not allow_overwrite:
            raise FileExistsError(
                "A template already exists at '{}'. Choose a new filename or "
                "allow overwrite.".format(output_path)
            )
        if confirm_overwrite and not confirm_template_overwrite(output_path):
            return None

    template_directory = os.path.dirname(output_path)
    if template_directory and not os.path.isdir(template_directory):
        os.makedirs(template_directory)

    primitive = xg.getActive(palette, description, "Primitive")
    include_guides = primitive == "SplinePrimitive"
    output_renderer = (
        _description_output_renderer(palette, description)
        or DEFAULT_XGEN_OUTPUT_RENDERER
    )
    modifiers = []
    for modifier in xg.fxModules(palette, description) or []:
        modifiers.append(
            {
                "name": modifier,
                "type": xg.fxModuleType(palette, description, modifier),
            }
        )

    with tempfile.TemporaryDirectory(prefix="xgen_template_") as temporary_dir:
        preset_path = os.path.join(temporary_dir, "description.xgp")
        exported = xg.exportDescriptionAsPreset(
            palette,
            description,
            preset_path,
            activeModuleOnly=False,
            guides=include_guides,
        )
        if not exported or not os.path.isfile(preset_path):
            raise RuntimeError("Maya could not export the XGen description preset.")

        with open(preset_path, "r", encoding="utf-8") as preset_file:
            preset_data = preset_file.read()

    template_data = {
        "format": "x-gen-tools-template",
        "version": 1,
        "source": {
            "collection": palette,
            "description": description,
        },
        "includes_guides": include_guides,
        "output_renderer": output_renderer,
        "modifiers": modifiers,
        "xgen_preset": preset_data,
    }

    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=template_directory,
            prefix=".xgen_template_",
            suffix=".tmp",
            delete=False,
        ) as template_file:
            temporary_path = template_file.name
            json.dump(template_data, template_file, indent=2, ensure_ascii=False)
            template_file.write("\n")
        os.replace(temporary_path, output_path)
    except Exception:
        if temporary_path and os.path.exists(temporary_path):
            os.remove(temporary_path)
        raise

    return output_path


def load_template(path):
    template_path = resolve_template_path(path)
    if not os.path.isfile(template_path):
        raise ValueError("Choose an existing XGen JSON template file.")

    with open(template_path, "r", encoding="utf-8") as template_file:
        template_data = json.load(template_file)

    if not isinstance(template_data, dict):
        raise ValueError("The X-GenTools template must be a JSON object.")
    if template_data.get("format") != "x-gen-tools-template":
        raise ValueError("This JSON file is not an X-GenTools template.")
    if template_data.get("version") != 1:
        raise ValueError("This X-GenTools template version is not supported.")
    if (
        not isinstance(template_data.get("xgen_preset"), str)
        or not template_data["xgen_preset"].strip()
    ):
        raise ValueError("The template does not contain an XGen description preset.")
    if not isinstance(template_data.get("includes_guides"), bool):
        raise ValueError("The template has an invalid guide-data setting.")
    output_renderer = template_data.setdefault(
        "output_renderer", DEFAULT_XGEN_OUTPUT_RENDERER
    )
    if not isinstance(output_renderer, str):
        raise ValueError("The template has an invalid output renderer setting.")

    return template_path, template_data
