"""Where the template .json files live."""

import os

import maya.cmds as cmds

from characters.xgen_template.constants import TEMPLATE_SUBDIR


def project_root():
    root = cmds.workspace(query=True, rootDirectory=True)
    if not root:
        # No Maya project: fall back to the characters package folder
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.normpath(root)


def templates_folder():
    return os.path.join(project_root(), TEMPLATE_SUBDIR)


def resolve_template_path(path):
    path = (path or "").strip()
    if not path:
        raise ValueError("Choose a template filename.")

    if path.startswith("./") or path.startswith(".\\"):
        path = path[2:]
    if not os.path.isabs(path):
        path = os.path.join(templates_folder(), path)

    if not path.lower().endswith(".json"):
        path += ".json"
    return os.path.normpath(path)


def template_json_files():
    template_directory = templates_folder()
    if not os.path.isdir(template_directory):
        return []
    with os.scandir(template_directory) as entries:
        return sorted(
            (
                entry.name
                for entry in entries
                if entry.name.lower().endswith(".json") and entry.is_file()
            ),
            key=str.lower,
        )
