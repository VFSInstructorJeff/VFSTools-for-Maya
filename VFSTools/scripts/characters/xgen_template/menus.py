"""Dropdown population and remembering the user's choices (saved as optionVars)."""

import os

import maya.cmds as cmds

from characters.xgen_template.constants import (
    GENERATION_GROUP_NAME,
    GUIDE_GROUP_NAME,
    MENU_FROM_PREFIX,
    MENU_GENERATION_GROUP,
    MENU_GUIDE_GROUP,
    MENU_MATERIAL,
    MENU_TEMPLATE,
    MENU_TO_PREFIX,
    NO_CHANGE_MATERIAL,
    OPTION_VAR_FROM_PREFIX,
    OPTION_VAR_GENERATION_GROUP,
    OPTION_VAR_GUIDE_GROUP,
    OPTION_VAR_MATERIAL,
    OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
    OPTION_VAR_SAVE_TEMPLATE_PATH,
    OPTION_VAR_TO_PREFIX,
    SELECT_GROUP_LABEL,
    SELECT_MATERIAL_LABEL,
    SELECT_PREFIX_LABEL,
    SELECTED_TEMPLATE_LABEL,
)
from characters.xgen_template.paths import resolve_template_path, template_json_files
from characters.xgen_template.prefs import (
    read_option_var_string,
    write_option_var_string,
)
from characters.xgen_template.scene import (
    prefixes_for_generation_group,
    scene_group_names,
    scene_materials,
)
from characters.xgen_template.style import set_dropdown_placeholder_color


def _clear_menu(menu_name):
    for item in cmds.optionMenu(menu_name, query=True, itemListLong=True) or []:
        cmds.deleteUI(item)


def _persist_menu_selection(menu_name, placeholder_label, option_var_name):
    """Remember the dropdown's value unless it is still showing its placeholder."""
    value = cmds.optionMenu(menu_name, query=True, value=True)
    set_dropdown_placeholder_color(menu_name, placeholder_label)
    if value != placeholder_label:
        write_option_var_string(option_var_name, value)


def _persist_template_selection(menu_name, display_option_var, path_option_var):
    value = cmds.optionMenu(menu_name, query=True, value=True)
    fallback_label = SELECTED_TEMPLATE_LABEL
    set_dropdown_placeholder_color(menu_name, fallback_label)
    if value == fallback_label:
        write_option_var_string(display_option_var, fallback_label)
        write_option_var_string(path_option_var, "")
        return

    previous_value = read_option_var_string(display_option_var)
    if value != previous_value:
        write_option_var_string(path_option_var, "")
    write_option_var_string(display_option_var, value)


def persist_save_template_selection(*_):
    _persist_template_selection(
        MENU_TEMPLATE,
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )


def persist_material_selection(*_):
    _persist_menu_selection(MENU_MATERIAL, SELECT_MATERIAL_LABEL, OPTION_VAR_MATERIAL)


def persist_generation_group_selection(*_):
    _persist_menu_selection(
        MENU_GENERATION_GROUP, SELECT_GROUP_LABEL, OPTION_VAR_GENERATION_GROUP
    )
    refresh_prefix_menus()


def persist_guide_group_selection(*_):
    _persist_menu_selection(
        MENU_GUIDE_GROUP, SELECT_GROUP_LABEL, OPTION_VAR_GUIDE_GROUP
    )


def persist_from_prefix_selection(*_):
    _persist_menu_selection(
        MENU_FROM_PREFIX, SELECT_PREFIX_LABEL, OPTION_VAR_FROM_PREFIX
    )


def persist_to_prefix_selection(*_):
    _persist_menu_selection(MENU_TO_PREFIX, SELECT_PREFIX_LABEL, OPTION_VAR_TO_PREFIX)


def resolve_template_menu_path(menu_name, display_option_var, path_option_var):
    display_name = cmds.optionMenu(menu_name, query=True, value=True).strip()
    if not display_name or display_name == SELECTED_TEMPLATE_LABEL:
        return ""
    saved_path = read_option_var_string(path_option_var)
    saved_display = read_option_var_string(display_option_var)
    if saved_path and display_name == saved_display:
        return os.path.normpath(saved_path)
    return resolve_template_path(display_name)


def _populate_menu_or_fallback(menu_name, values, fallback_label):
    if values:
        for value in values:
            cmds.menuItem(label=value, parent=menu_name)
        return values

    cmds.menuItem(label=fallback_label, parent=menu_name, enable=False)
    return [fallback_label]


def _refresh_template_menu(menu_name, display_option_var, path_option_var):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    existing_items = cmds.optionMenu(menu_name, query=True, itemListLong=True) or []
    current_display = (
        cmds.optionMenu(menu_name, query=True, value=True) if existing_items else ""
    )
    saved_display = read_option_var_string(display_option_var)
    saved_path = read_option_var_string(path_option_var)
    file_names = template_json_files()
    if (
        saved_display
        and saved_display not in file_names
        and saved_path
        and os.path.basename(saved_path) == saved_display
        and os.path.isfile(saved_path)
    ):
        file_names.append(saved_display)
        file_names.sort(key=str.lower)

    for item in existing_items:
        cmds.deleteUI(item)
    fallback_label = SELECTED_TEMPLATE_LABEL
    menu_values = _populate_menu_or_fallback(menu_name, file_names, fallback_label)

    selected_value = (
        current_display
        if current_display in menu_values
        else (saved_display if saved_display in menu_values else menu_values[0])
    )
    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(file_names),
    )
    set_dropdown_placeholder_color(menu_name, fallback_label)


def refresh_save_template_menu(*_):
    _refresh_template_menu(
        MENU_TEMPLATE,
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )


def refresh_generation_group_menu(*_, group_names=None):
    menu_name = MENU_GENERATION_GROUP
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = read_option_var_string(
        OPTION_VAR_GENERATION_GROUP, GENERATION_GROUP_NAME
    )
    _clear_menu(menu_name)

    if group_names is None:
        group_names = scene_group_names()
    menu_values = _populate_menu_or_fallback(menu_name, group_names, SELECT_GROUP_LABEL)

    prefix_cache = {}

    def prefixes_for(group_name):
        if group_name not in prefix_cache:
            prefix_cache[group_name] = prefixes_for_generation_group(group_name)
        return prefix_cache[group_name]

    selected_value = saved_value if saved_value in group_names else menu_values[0]
    selected_prefixes = prefixes_for(saved_value) if saved_value in group_names else []
    if not selected_prefixes:
        for group_name in group_names:
            group_prefixes = prefixes_for(group_name)
            if group_prefixes:
                selected_value = group_name
                selected_prefixes = group_prefixes
                break
    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(group_names),
    )
    set_dropdown_placeholder_color(menu_name, SELECT_GROUP_LABEL)
    refresh_prefix_menus(prefixes=selected_prefixes)


def refresh_guide_group_menu(*_, group_names=None):
    menu_name = MENU_GUIDE_GROUP
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = read_option_var_string(OPTION_VAR_GUIDE_GROUP, GUIDE_GROUP_NAME)
    _clear_menu(menu_name)

    if group_names is None:
        group_names = scene_group_names()
    menu_values = _populate_menu_or_fallback(menu_name, group_names, SELECT_GROUP_LABEL)

    selected_value = saved_value if saved_value in group_names else menu_values[0]
    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(group_names),
    )
    set_dropdown_placeholder_color(menu_name, SELECT_GROUP_LABEL)


def refresh_material_menu(*_):
    menu_name = MENU_MATERIAL
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = read_option_var_string(OPTION_VAR_MATERIAL, SELECT_MATERIAL_LABEL)
    _clear_menu(menu_name)

    scene_material_names = scene_materials()
    if scene_material_names:
        material_names = [NO_CHANGE_MATERIAL] + scene_material_names
        _populate_menu_or_fallback(menu_name, material_names, SELECT_MATERIAL_LABEL)
    else:
        material_names = [NO_CHANGE_MATERIAL]
        cmds.menuItem(label=NO_CHANGE_MATERIAL, parent=menu_name)
        _populate_menu_or_fallback(menu_name, [], SELECT_MATERIAL_LABEL)

    selected_value = (
        saved_value
        if saved_value in material_names
        else (material_names[0] if scene_material_names else SELECT_MATERIAL_LABEL)
    )
    cmds.optionMenu(menu_name, edit=True, value=selected_value)
    set_dropdown_placeholder_color(menu_name, SELECT_MATERIAL_LABEL)


def refresh_scene_dropdowns(*_):
    refresh_save_template_menu()
    group_names = scene_group_names()
    refresh_generation_group_menu(group_names=group_names)
    refresh_guide_group_menu(group_names=group_names)
    refresh_material_menu()


def _scene_generation_prefixes():
    menu_name = MENU_GENERATION_GROUP
    if not cmds.optionMenu(menu_name, exists=True):
        return []

    generation_group = cmds.optionMenu(menu_name, query=True, value=True)
    if not generation_group or generation_group == SELECT_GROUP_LABEL:
        return []

    return prefixes_for_generation_group(generation_group)


def _refresh_prefix_menu(menu_name, option_var_name, prefixes, default_index):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    _clear_menu(menu_name)
    _populate_menu_or_fallback(menu_name, prefixes, SELECT_PREFIX_LABEL)

    if prefixes:
        default_value = prefixes[default_index]
        saved_value = read_option_var_string(option_var_name, default_value)
        selected_value = saved_value if saved_value in prefixes else default_value
    else:
        selected_value = SELECT_PREFIX_LABEL

    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(prefixes),
    )
    set_dropdown_placeholder_color(menu_name, SELECT_PREFIX_LABEL)


def refresh_from_prefix_menu(*_):
    _refresh_prefix_menu(
        MENU_FROM_PREFIX,
        OPTION_VAR_FROM_PREFIX,
        _scene_generation_prefixes(),
        0,
    )


def refresh_to_prefix_menu(*_):
    _refresh_prefix_menu(
        MENU_TO_PREFIX,
        OPTION_VAR_TO_PREFIX,
        _scene_generation_prefixes(),
        -1,
    )


def refresh_prefix_menus(*_, prefixes=None):
    if not cmds.optionMenu(MENU_FROM_PREFIX, exists=True) or not cmds.optionMenu(
        MENU_TO_PREFIX, exists=True
    ):
        return

    if prefixes is None:
        prefixes = _scene_generation_prefixes()
    _refresh_prefix_menu(
        MENU_FROM_PREFIX,
        OPTION_VAR_FROM_PREFIX,
        prefixes,
        0,
    )
    _refresh_prefix_menu(
        MENU_TO_PREFIX,
        OPTION_VAR_TO_PREFIX,
        prefixes,
        -1,
    )
