"""The dockable X-Gen Template Tool panel: building it and the callbacks behind its buttons."""

import os

import maya.cmds as cmds

from characters.xgen_template.apply import apply_template, clean_start
from characters.xgen_template.constants import (
    APPLY_ROW_COLOR,
    BUTTON_CLEAN_START,
    BUTTON_LOAD_TEMPLATE,
    BUTTON_SAVE_TEMPLATE,
    CLEAN_START_BODY_BACKGROUND,
    CLEAN_START_HEADER_BACKGROUND,
    FIELD_COLOR,
    FIELD_HEIGHT,
    FIELD_ROW_HEIGHT,
    FOOTER_AUTHOR,
    FOOTER_HELP,
    FOOTER_ROW_HEIGHT,
    FOOTER_SIDE_PADDING,
    FOOTER_TEXT_HEIGHT,
    FOOTER_VERSION,
    LEGACY_WINDOW_NAME,
    MENU_FROM_PREFIX,
    MENU_GENERATION_GROUP,
    MENU_GUIDE_GROUP,
    MENU_MATERIAL,
    MENU_TEMPLATE,
    MENU_TO_PREFIX,
    OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
    OPTION_VAR_SAVE_TEMPLATE_PATH,
    ROW_NUMBER_WIDTH,
    SCROLL_LAYOUT_NAME,
    SELECTED_TEMPLATE_LABEL,
    SECTION_HEADER_HEIGHT,
    STEP_1,
    STEP_2,
    STEP_3,
    STEP_4,
    STEP_5,
    STEP_NUMBER_COLOR,
    WINDOW_CONTENT_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WORKSPACE_CONTROL_NAME,
)
from characters.xgen_template.dialogs import show_completion_message, show_message
from characters.xgen_template.menus import (
    persist_from_prefix_selection,
    persist_generation_group_selection,
    persist_guide_group_selection,
    persist_material_selection,
    persist_save_template_selection,
    persist_to_prefix_selection,
    refresh_from_prefix_menu,
    refresh_generation_group_menu,
    refresh_guide_group_menu,
    refresh_material_menu,
    refresh_prefix_menus,
    refresh_save_template_menu,
    refresh_scene_dropdowns,
    refresh_to_prefix_menu,
    resolve_template_menu_path,
)
from characters.xgen_template.paths import resolve_template_path
from characters.xgen_template.prefs import write_option_var_string
from characters.xgen_template.style import (
    install_dropdown_hover_effects,
    install_fast_tooltips,
    install_step_hover_effects,
    set_dropdown_placeholder_color,
    set_footer_text_color,
    set_workspace_control_fixed_width,
    style_action_button,
)
from characters.xgen_template.template_io import (
    choose_template_save_path,
    save_template,
)


def _save_template_from_window(*_):
    try:
        path = choose_template_save_path()
        if not path:
            return

        resolved_path = resolve_template_path(path)
        overwriting = os.path.isfile(resolved_path)
        output_path = save_template(path, allow_overwrite=True, confirm_overwrite=False)
        if output_path:
            saved_display = os.path.basename(output_path)
            write_option_var_string(OPTION_VAR_SAVE_TEMPLATE_DISPLAY, saved_display)
            write_option_var_string(OPTION_VAR_SAVE_TEMPLATE_PATH, output_path)
            refresh_save_template_menu()
            cmds.optionMenu(MENU_TEMPLATE, edit=True, value=saved_display)
            set_dropdown_placeholder_color(MENU_TEMPLATE, SELECTED_TEMPLATE_LABEL)
            action = "Overwrote" if overwriting else "Saved"
            show_completion_message("{} Template: {}.".format(action, saved_display))
    except Exception as error:
        cmds.warning("[X-Gen Template Tool] Save Template failed: {}".format(error))
        show_message("Save Template Error", str(error), icon="critical")


def _resolve_apply_template_path():
    return resolve_template_menu_path(
        MENU_TEMPLATE,
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )


def _apply_from_window(*_):
    try:
        path = _resolve_apply_template_path()

        generation_group = cmds.optionMenu(
            MENU_GENERATION_GROUP, query=True, value=True
        )
        guide_group = cmds.optionMenu(MENU_GUIDE_GROUP, query=True, value=True)
        from_prefix = cmds.optionMenu(MENU_FROM_PREFIX, query=True, value=True)
        to_prefix = cmds.optionMenu(MENU_TO_PREFIX, query=True, value=True)
        material = cmds.optionMenu(MENU_MATERIAL, query=True, value=True)
        result = apply_template(
            path,
            generation_group,
            guide_group,
            from_prefix,
            to_prefix,
            material,
        )
        if result is None:
            return

        warnings = list(result["map_warnings"])
        if result["preview_warning"]:
            warnings.append("Preview failed: {}".format(result["preview_warning"]))
        completion_verb = "Replaced" if result["replaced"] else "Loaded"
        completion = "{} {} Description(s)".format(
            completion_verb, len(result["descriptions"])
        )
        show_completion_message("{}.".format(completion))
        if warnings:
            show_message(
                "X-GenTools Apply Warning",
                "\n".join(warnings),
                icon="warning",
            )
    except Exception as error:
        cmds.warning("[X-GenTools] Load Template failed: {}".format(error))
        show_message("Load Template Error", str(error), icon="critical")


def _clean_start_from_window(*_):
    try:
        deleted_descriptions = clean_start()
        if deleted_descriptions is None:
            return
        if deleted_descriptions:
            show_completion_message(
                "Deleted {} Description(s).".format(len(deleted_descriptions))
            )
        else:
            show_completion_message("No descriptions to delete.")
    except Exception as error:
        cmds.warning("[X-GenTools] Clean Start failed: {}".format(error))
        show_message("Clean Start Error", str(error), icon="critical")


def workspace_ui_script():
    return (
        "from characters import xgen_template_tool; " "xgen_template_tool._build_ui()"
    )


def show():
    """Open or restore the dockable X-Gen Template Tool panel."""
    if cmds.window(LEGACY_WINDOW_NAME, exists=True):
        cmds.deleteUI(LEGACY_WINDOW_NAME)

    shared_options = dict(
        label=WINDOW_TITLE,
        initialWidth=WINDOW_WIDTH,
        minimumWidth=WINDOW_WIDTH,
        widthProperty="fixed",
        loadImmediately=True,
        checksPlugins=True,
        requiredPlugin="xgenToolkit",
        uiScript=workspace_ui_script(),
    )
    if cmds.workspaceControl(WORKSPACE_CONTROL_NAME, query=True, exists=True):
        cmds.workspaceControl(
            WORKSPACE_CONTROL_NAME, edit=True, restore=True, **shared_options
        )
        build_ui()
        return

    cmds.workspaceControl(
        WORKSPACE_CONTROL_NAME,
        retain=True,
        initialHeight=WINDOW_HEIGHT,
        dockToMainWindow=("right", False),
        **shared_options
    )
    build_ui()


# ---------------------------------------------------------------------------
# Building the panel
# ---------------------------------------------------------------------------


def _bullet(text):
    return "<tr><td width='8' valign='top'>\u2022</td><td>{}</td></tr>".format(text)


def _tooltip(width, *bullets):
    """HTML help text: a dark table with one bulleted row per item."""
    return (
        "<span style='color: #ffffff;'>"
        "<table cellspacing='0' cellpadding='3' border='0' width='{}' "
        "bgcolor='#3b3b3b'>{}</table></span>"
    ).format(width, "".join(_bullet(text) for text in bullets))


_PREFIX_RANGE_TOOLTIP = _tooltip(
    270,
    "<b><i>Select</i></b> the <b><i>Prefix Range</i></b> to "
    "<b><i>Apply</i></b> across the<br>"
    "<b><i>Generation Bases</i></b> &amp; the matching "
    "<b><i>Guide Curves</i></b>.",
)

_WORKFLOW_TOOLTIP = (
    "<span style='color: #ffffff;'>"
    "<table cellspacing='0' cellpadding='3' border='0' width='304' "
    "bgcolor='#3b3b3b'>"
    "<tr><td align='left'>"
    "<b><i>[[ WORKFLOW ]]</i></b></td></tr>"
    "<tr><td>"
    "<table cellspacing='0' cellpadding='3' border='0' width='298'>"
    + "".join(
        _bullet(text)
        for text in (
            "Prepare your " "<b><i>Generation Bases &amp; Guide Curves</i></b>.",
            "Finalize a "
            "<b><i>Description</i></b> under an existing "
            "<b><i>Collection</i></b>.",
            "<b><i>Save Template</i></b> "
            "saves <b><i>All Settings</i></b> on <b><i>All Tabs</i></b>, "
            "<b><i>Set Stray Percentages</i></b> "
            "&amp; <b><i>Modifiers</i></b> to a "
            "<b><i>.json File</i></b>.",
            "<b><i>Select</i></b> your "
            "<b><i>Template</i></b>, <b><i>Generation Base</i></b> | "
            "<b><i>Guide Curve</i></b><br>"
            "outliner groups, <b><i>Prefix Range</i></b> &amp; the display "
            "<b><i>Material</i></b>.",
            "<b><i>Load Template</i></b> "
            "applies the template to all<br>"
            "the <b><i>Generation Bases</i></b> in the "
            "<b><i>Range Specified</i></b>.",
            "<b><i>Clean Start</i></b> will "
            "remove <b><i>All Descriptions</i></b>. Tweak the<br>"
            "curves &amp; reload the template. "
            "<b><i>Iterate until happy. :-D</i></b>",
        )
    )
    + "</table></td></tr>"
    "</table></span>"
)


def _action_button(
    name, label, background_color, tooltip, command, pressed_color, hover_color
):
    cmds.button(
        name,
        label=label,
        height=SECTION_HEADER_HEIGHT,
        backgroundColor=background_color,
        annotation=tooltip,
        command=command,
    )
    style_action_button(
        name,
        pressed_color=pressed_color,
        hover_color=hover_color,
        pressed_text_color="white",
    )


def _begin_step_row(step_control, number):
    """Separator + a two-column row holding the numbered label; the caller adds the dropdown and closes the row."""
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(ROW_NUMBER_WIDTH, WINDOW_CONTENT_WIDTH - ROW_NUMBER_WIDTH),
        columnAttach2=("both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=APPLY_ROW_COLOR,
    )
    _step_number(step_control, number)


def _step_number(step_control, number):
    cmds.text(
        step_control,
        label=str(number),
        align="center",
        height=24,
        backgroundColor=STEP_NUMBER_COLOR,
    )


def _dropdown(menu_name, change_command, popup_command, tooltip):
    cmds.optionMenu(
        menu_name,
        height=FIELD_HEIGHT,
        backgroundColor=FIELD_COLOR,
        changeCommand=change_command,
        beforeShowPopup=popup_command,
        annotation=tooltip,
    )


def build_ui():
    if cmds.scrollLayout(SCROLL_LAYOUT_NAME, exists=True):
        cmds.deleteUI(SCROLL_LAYOUT_NAME)
    # Maya may rebuild retained workspace controls and run the shelf command too.
    for child in cmds.layout(WORKSPACE_CONTROL_NAME, query=True, childArray=True) or []:
        cmds.deleteUI(child)
    cmds.setParent(WORKSPACE_CONTROL_NAME)
    cmds.columnLayout(
        adjustableColumn=True,
        rowSpacing=0,
        columnAttach=("both", 4),
    )

    _action_button(
        BUTTON_SAVE_TEMPLATE,
        "SAVE TEMPLATE",
        (0.52, 0.72, 0.53),
        _tooltip(
            225,
            "<b><i>Saves</i></b> or "
            "<b><i>Overwrites</i></b> a <b><i>.json File</i></b> "
            "<b><i>Template</i></b><br>"
            "of the current <b><i>Selected Description</i></b>.",
            "Saved into " "<b><i>/xgen/template</i></b> folder.",
        ),
        _save_template_from_window,
        pressed_color=(46, 75, 48),
        hover_color=(99, 184, 102),
    )

    # Row 1: Selected Template Dropdown
    _begin_step_row(STEP_1, 1)
    _dropdown(
        MENU_TEMPLATE,
        persist_save_template_selection,
        refresh_save_template_menu,
        _tooltip(
            210,
            "<b><i>Select</i></b> the <b><i>Saved Template</i></b> you want<br>"
            "to apply to your <b><i>Generation Bases</i></b>.",
        ),
    )
    cmds.setParent("..")
    refresh_save_template_menu()

    # Row 2: Generation Bases Group
    _begin_step_row(STEP_2, 2)
    _dropdown(
        MENU_GENERATION_GROUP,
        persist_generation_group_selection,
        refresh_generation_group_menu,
        _tooltip(
            235,
            "<b><i>Select</i></b> the <b><i>Top-Level Group</i></b> in the "
            "<b><i>Outliner</i></b> "
            "containing the <b><i>Generation Bases</i></b>.",
        ),
    )
    cmds.setParent("..")
    refresh_generation_group_menu()

    # Row 3: Guide Curves Group
    _begin_step_row(STEP_3, 3)
    _dropdown(
        MENU_GUIDE_GROUP,
        persist_guide_group_selection,
        refresh_guide_group_menu,
        _tooltip(
            235,
            "<b><i>Select</i></b> the <i>Top-Level Group</i> in the "
            "<b><i>Outliner</i></b><br>"
            "containing the <b><i>Guide Curves</i></b>.",
        ),
    )
    cmds.setParent("..")
    refresh_guide_group_menu()

    # Row 4: Prefix Range (From / To)
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=5,
        adjustableColumn=3,
        columnWidth5=(ROW_NUMBER_WIDTH, 30, 44, 16, 48),
        columnAttach5=("both", "both", "both", "both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=APPLY_ROW_COLOR,
    )
    _step_number(STEP_4, 4)
    cmds.text(label="From", align="center", height=24)
    _dropdown(
        MENU_FROM_PREFIX,
        persist_from_prefix_selection,
        refresh_from_prefix_menu,
        _PREFIX_RANGE_TOOLTIP,
    )
    cmds.text(label="To", align="center", height=24)
    _dropdown(
        MENU_TO_PREFIX,
        persist_to_prefix_selection,
        refresh_to_prefix_menu,
        _PREFIX_RANGE_TOOLTIP,
    )
    cmds.setParent("..")
    refresh_prefix_menus()

    # Row 5: Material Selection
    _begin_step_row(STEP_5, 5)
    _dropdown(
        MENU_MATERIAL,
        persist_material_selection,
        refresh_material_menu,
        _tooltip(
            250,
            "<b><i>Choose</i></b> the <b><i>Material</i></b> for all the "
            "<b><i>Descriptions</i></b><br>"
            "within the <b><i>Specified</i></b> <b><i>Range</i></b>.",
        ),
    )
    cmds.setParent("..")
    refresh_material_menu()
    install_dropdown_hover_effects()
    install_step_hover_effects()
    cmds.scriptJob(
        event=("SceneOpened", refresh_scene_dropdowns),
        parent=WORKSPACE_CONTROL_NAME,
        replacePrevious=True,
    )

    # LOAD TEMPLATE Button
    cmds.separator(height=3, style="none")
    _action_button(
        BUTTON_LOAD_TEMPLATE,
        "LOAD TEMPLATE",
        (0.53, 0.52, 0.78),
        _tooltip(
            350,
            "<b><i>Creates "
            "Descriptions</i></b> under the <b><i>Selected Collection</i></b> "
            "by pairing<br>"
            "<b><i>Generation Bases</i></b> to <b><i>Guide Curves</i></b> by "
            "naming convention<br>"
            "<b><i>Across The Range</i></b>.",
            "<b><i>Copies All "
            "Settings</i></b> from the <b><i>Template</i></b> including "
            "<b><i>Modifiers</i></b>.",
            "Applies the selected "
            "<b><i>Material</i></b> to the <b><i>Collection</i></b>.",
            "<b><i>Hides</i></b> the "
            "<b><i>XGen Description Guides</i></b> &amp; "
            "<b><i>Previews All Descriptions</i></b>.",
        ),
        _apply_from_window,
        pressed_color=(51, 49, 77),
        hover_color=(105, 102, 199),
    )

    # CLEAN START Button
    cmds.separator(height=3, style="none")
    _action_button(
        BUTTON_CLEAN_START,
        "CLEAN START",
        CLEAN_START_HEADER_BACKGROUND,
        _tooltip(
            255,
            "<b><i>Deletes All Descriptions</i></b> from the "
            "<b><i>Collection</i></b>.<br>"
            "<b><i>Tweak The Curves</i></b> then "
            "<b><i>Reload The Template</i></b>.",
        ),
        _clean_start_from_window,
        pressed_color=(83, 66, 2),
        hover_color=(214, 183, 57),
    )

    # Footer
    cmds.separator(height=2, style="none")
    cmds.rowLayout(
        numberOfColumns=5,
        adjustableColumn=3,
        columnWidth5=(
            FOOTER_SIDE_PADDING,
            18,
            WINDOW_CONTENT_WIDTH - 55 - 18 - FOOTER_SIDE_PADDING * 2,
            55,
            FOOTER_SIDE_PADDING,
        ),
        columnAttach5=("both", "both", "both", "both", "both"),
        height=FOOTER_ROW_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    _footer_spacer()
    cmds.iconTextButton(
        FOOTER_HELP,
        style="iconOnly",
        image="help.png",
        width=18,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
        annotation=_WORKFLOW_TOOLTIP,
    )
    cmds.text(
        FOOTER_AUTHOR,
        label="InstructorJeff",
        align="left",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    cmds.text(
        FOOTER_VERSION,
        label="V1.00",
        align="right",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    _footer_spacer()
    install_fast_tooltips()
    set_footer_text_color()
    cmds.setParent("..")

    cmds.setParent("..")
    set_workspace_control_fixed_width()


def _footer_spacer():
    cmds.text(
        label="",
        width=FOOTER_SIDE_PADDING,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
