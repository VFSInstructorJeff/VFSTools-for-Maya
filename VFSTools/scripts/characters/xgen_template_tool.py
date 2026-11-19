"""Provide a dockable Maya interface for saving and applying XGen templates.

The tool saves the selected XGen description's settings, palette data, and
modifier information as JSON under the project's ``xgen/templates`` folder.
It can apply a saved template across selected generation bases, matching guide
curves and prefix ranges, optionally convert curves to guides, and apply a display
material. Clean Start removes descriptions from the active collection so the user
can revise curves and rebuild. The module also provides the UI callbacks and menu
refresh helpers, validates apply targets, and uses shader-cleanup helpers to avoid
leaving unused hair-physical shader nodes behind.
"""

import json
import html
import os
import re
import sys
import tempfile
import uuid

import maya.cmds as cmds
import maya.mel as mel
import xgenm as xg
import xgenm.xgGlobal as xgg
import xgenm.xmaya.xgmExternalAPI as xgen_api

_SCRIPT_PATH = globals().get("__file__")
_SCRIPT_ARGS = globals().get("__args__")
if not _SCRIPT_PATH and isinstance(_SCRIPT_ARGS, dict):
    _SCRIPT_PATH = _SCRIPT_ARGS.get("script_path")
if not _SCRIPT_PATH:
    _SCRIPT_PATH = next(
        (
            candidate
            for directory in sys.path
            for candidate in [os.path.join(directory or os.getcwd(), "xgen_template_tool.py")]
            if os.path.isfile(candidate)
        ),
        "",
    )
if not _SCRIPT_PATH:
    raise RuntimeError("X-Gen Template Tool needs its script path to be available.")
_SCRIPT_PATH = os.path.abspath(_SCRIPT_PATH)
_PROJECT_DIRECTORY = os.path.dirname(_SCRIPT_PATH)
from characters.xgen_shader_cleanup import (
    remove_new_unused_hair_physical_nodes,
    snapshot_hair_physical_nodes,
)


WORKSPACE_CONTROL_NAME = "xGenToolsWorkspaceControl"
SCROLL_LAYOUT_NAME = "xGenToolsScrollLayout"
LEGACY_WINDOW_NAME = "xGenToolsWindow"
WINDOW_TITLE = "X-Gen Template Tool"
WINDOW_WIDTH = 180
WINDOW_CONTENT_WIDTH = WINDOW_WIDTH - 10
WINDOW_HEIGHT = 700
SECTION_HEADER_HEIGHT = 25
FIELD_HEIGHT = 20
FIELD_ROW_HEIGHT = 28
ROW_NUMBER_WIDTH = 24
FOOTER_ROW_HEIGHT = 19
FOOTER_TEXT_HEIGHT = 16
FOOTER_SIDE_PADDING = 2
CLEAN_START_HEADER_BACKGROUND = (0.82, 0.71, 0.334)
CLEAN_START_BODY_BACKGROUND = (0.30, 0.30, 0.30)
TEMPLATE_SUBDIR = os.path.join("xgen", "templates")
GEO_PATTERN = re.compile(r"^([A-Za-z])_(.+)_GEO$")
OPTION_VAR_SAVE_TEMPLATE_PATH = "xGenTools_SaveTemplatePath"
OPTION_VAR_SAVE_TEMPLATE_DISPLAY = "xGenTools_SaveTemplateDisplay"
OPTION_VAR_GENERATION_GROUP = "xGenTools_GenerationGroup"
OPTION_VAR_GUIDE_GROUP = "xGenTools_GuideGroup"
OPTION_VAR_FROM_PREFIX = "xGenTools_FromPrefix"
OPTION_VAR_TO_PREFIX = "xGenTools_ToPrefix"
OPTION_VAR_MATERIAL = "xGenTools_Material"
NO_CHANGE_MATERIAL = "No change"
SELECT_MATERIAL_LABEL = "Select material"
SELECT_GROUP_LABEL = "Select group"
SELECTED_TEMPLATE_LABEL = "selected template"
SELECT_PREFIX_LABEL = "Select prefix"
DEFAULT_XGEN_OUTPUT_RENDERER = "Arnold Renderer"


def _project_root():
    root = cmds.workspace(query=True, rootDirectory=True)
    if not root:
        root = os.path.dirname(_SCRIPT_PATH)
    return os.path.normpath(root)


def _template_directory():
    return os.path.join(_project_root(), TEMPLATE_SUBDIR)


def _show_message(title, message, icon="information"):
    cmds.confirmDialog(
        title=title,
        message=message,
        button=["OK"],
        defaultButton="OK",
        icon=icon,
    )


def _confirm_clean_start(palette, descriptions):
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    parent_pointer = omui.MQtUtil.mainWindow()
    parent = (
        wrap_instance(int(parent_pointer), QtWidgets.QWidget)
        if parent_pointer
        else None
    )
    dialog = QtWidgets.QMessageBox(parent)
    dialog.setWindowTitle("Clean Start?")

    warning_icon = getattr(QtWidgets.QMessageBox, "Warning", None)
    if warning_icon is None:
        warning_icon = QtWidgets.QMessageBox.Icon.Warning
    dialog.setIcon(warning_icon)

    rich_text = getattr(QtCore.Qt, "RichText", None)
    if rich_text is None:
        rich_text = QtCore.Qt.TextFormat.RichText
    dialog.setTextFormat(rich_text)
    escaped_palette = html.escape(palette, quote=False)
    escaped_descriptions = "<br>".join(
        html.escape(description, quote=False) for description in descriptions
    )
    dialog.setText(
        "<b><i>Delete All {} Description(s)</i></b><br>"
        "from the "
        "<b><i>'{}'?</i></b><br><br>"
        "<b><i>Generation Bases</i></b> &amp; <b><i>Guide Curves</i></b><br>"
        "will <b><i>NOT</i></b> be <b><i>Deleted.</i></b><br><br>"
        "{}<br><br><b><i>Continue?</i></b>".format(
            len(descriptions), escaped_palette, escaped_descriptions
        )
    )

    accept_role = getattr(QtWidgets.QMessageBox, "AcceptRole", None)
    reject_role = getattr(QtWidgets.QMessageBox, "RejectRole", None)
    if accept_role is None:
        accept_role = QtWidgets.QMessageBox.ButtonRole.AcceptRole
    if reject_role is None:
        reject_role = QtWidgets.QMessageBox.ButtonRole.RejectRole
    yes_button = dialog.addButton("Yes", accept_role)
    no_button = dialog.addButton("No", reject_role)
    dialog.setDefaultButton(no_button)
    dialog.setEscapeButton(no_button)

    execute = getattr(dialog, "exec", None)
    if execute is None:
        execute = dialog.exec_
    execute()
    return dialog.clickedButton() is yes_button


def _confirm_description_replacement(descriptions):
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    parent_pointer = omui.MQtUtil.mainWindow()
    parent = (
        wrap_instance(int(parent_pointer), QtWidgets.QWidget)
        if parent_pointer
        else None
    )
    dialog = QtWidgets.QMessageBox(parent)
    dialog.setWindowTitle("Replace Existing XGen Descriptions?")

    warning_icon = getattr(QtWidgets.QMessageBox, "Warning", None)
    if warning_icon is None:
        warning_icon = QtWidgets.QMessageBox.Icon.Warning
    dialog.setIcon(warning_icon)

    rich_text = getattr(QtCore.Qt, "RichText", None)
    if rich_text is None:
        rich_text = QtCore.Qt.TextFormat.RichText
    dialog.setTextFormat(rich_text)
    escaped_descriptions = "<br>".join(
        html.escape(description, quote=False) for description in descriptions
    )
    dialog.setText(
        "This will <b><i>Replace {} Existing Description(s)</i>"
        "</b>,<br>including their <b><i>Settings &amp; Bindings</i></b>:<br><br>"
        "{}<br><br><b><i>Continue?</i></b>".format(
            len(descriptions), escaped_descriptions
        )
    )

    accept_role = getattr(QtWidgets.QMessageBox, "AcceptRole", None)
    reject_role = getattr(QtWidgets.QMessageBox, "RejectRole", None)
    if accept_role is None:
        accept_role = QtWidgets.QMessageBox.ButtonRole.AcceptRole
    if reject_role is None:
        reject_role = QtWidgets.QMessageBox.ButtonRole.RejectRole
    replace_button = dialog.addButton("Replace", accept_role)
    cancel_button = dialog.addButton("Cancel", reject_role)
    dialog.setDefaultButton(cancel_button)
    dialog.setEscapeButton(cancel_button)

    execute = getattr(dialog, "exec", None)
    if execute is None:
        execute = dialog.exec_
    execute()
    return dialog.clickedButton() is replace_button


def _confirm_template_overwrite(output_path):
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    parent_pointer = omui.MQtUtil.mainWindow()
    parent = (
        wrap_instance(int(parent_pointer), QtWidgets.QWidget)
        if parent_pointer
        else None
    )
    dialog = QtWidgets.QMessageBox(parent)
    dialog.setWindowTitle("Overwrite Template?")

    warning_icon = getattr(QtWidgets.QMessageBox, "Warning", None)
    if warning_icon is None:
        warning_icon = QtWidgets.QMessageBox.Icon.Warning
    dialog.setIcon(warning_icon)

    rich_text = getattr(QtCore.Qt, "RichText", None)
    if rich_text is None:
        rich_text = QtCore.Qt.TextFormat.RichText
    dialog.setTextFormat(rich_text)
    dialog.setText(_template_overwrite_confirmation_text(output_path))

    accept_role = getattr(QtWidgets.QMessageBox, "AcceptRole", None)
    reject_role = getattr(QtWidgets.QMessageBox, "RejectRole", None)
    if accept_role is None:
        accept_role = QtWidgets.QMessageBox.ButtonRole.AcceptRole
    if reject_role is None:
        reject_role = QtWidgets.QMessageBox.ButtonRole.RejectRole
    overwrite_button = dialog.addButton("Overwrite", accept_role)
    cancel_button = dialog.addButton("Cancel", reject_role)
    dialog.setDefaultButton(cancel_button)
    dialog.setEscapeButton(cancel_button)

    execute = getattr(dialog, "exec", None)
    if execute is None:
        execute = dialog.exec_
    execute()
    return dialog.clickedButton() is overwrite_button


def _template_overwrite_confirmation_text(output_path):
    relative_path = os.path.relpath(output_path, _project_root()).replace(
        "\\", "/"
    )
    return (
        "<div style='text-align: left;'>"
        "A file already exists at:<br>{}"
        "</div>"
        "<div style='text-align: center; margin-top: 8px;'>"
        "Overwrite it with selected description?"
        "</div>"
    ).format(html.escape(relative_path, quote=True))


def _read_option_var_string(name, default=""):
    if not cmds.optionVar(exists=name):
        return default
    value = cmds.optionVar(query=name)
    return default if value is None else value


def _write_option_var_string(name, value):
    cmds.optionVar(stringValue=(name, value))


def _persist_text_field(field_name, option_var_name, *_):
    value = cmds.textField(field_name, query=True, text=True)
    _write_option_var_string(option_var_name, value)


def _persist_template_selection(menu_name, display_option_var, path_option_var):
    value = cmds.optionMenu(menu_name, query=True, value=True)
    fallback_label = _template_fallback_label()
    _set_dropdown_placeholder_color(menu_name, fallback_label)
    if value == fallback_label:
        _write_option_var_string(display_option_var, fallback_label)
        _write_option_var_string(path_option_var, "")
        return

    previous_value = _read_option_var_string(display_option_var)
    if value != previous_value:
        _write_option_var_string(path_option_var, "")
    _write_option_var_string(display_option_var, value)


def _persist_save_template_selection(*_):
    _persist_template_selection(
        "xGenToolsTemplatePath",
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )





def _persist_material_selection(*_):
    value = cmds.optionMenu(
        "xGenToolsApplyMaterial", query=True, value=True
    )
    _set_dropdown_placeholder_color(
        "xGenToolsApplyMaterial", SELECT_MATERIAL_LABEL
    )
    if value != SELECT_MATERIAL_LABEL:
        _write_option_var_string(OPTION_VAR_MATERIAL, value)


def _persist_generation_group_selection(*_):
    value = cmds.optionMenu(
        "xGenToolsGenerationGroup", query=True, value=True
    )
    _set_dropdown_placeholder_color(
        "xGenToolsGenerationGroup", SELECT_GROUP_LABEL
    )
    if value != SELECT_GROUP_LABEL:
        _write_option_var_string(OPTION_VAR_GENERATION_GROUP, value)
    _refresh_prefix_menus()


def _persist_guide_group_selection(*_):
    value = cmds.optionMenu(
        "xGenToolsGuideGroup", query=True, value=True
    )
    _set_dropdown_placeholder_color(
        "xGenToolsGuideGroup", SELECT_GROUP_LABEL
    )
    if value != SELECT_GROUP_LABEL:
        _write_option_var_string(OPTION_VAR_GUIDE_GROUP, value)


def _persist_prefix_selection(menu_name, option_var_name):
    value = cmds.optionMenu(menu_name, query=True, value=True)
    _set_dropdown_placeholder_color(menu_name, SELECT_PREFIX_LABEL)
    if value != SELECT_PREFIX_LABEL:
        _write_option_var_string(option_var_name, value)


def _persist_from_prefix_selection(*_):
    _persist_prefix_selection("xGenToolsFromPrefix", OPTION_VAR_FROM_PREFIX)


def _persist_to_prefix_selection(*_):
    _persist_prefix_selection("xGenToolsToPrefix", OPTION_VAR_TO_PREFIX)


def _set_footer_text_color():
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    for control_name in ("xGenToolsFooterAuthor", "xGenToolsFooterVersion"):
        pointer = omui.MQtUtil.findControl(control_name)
        if not pointer:
            raise RuntimeError(
                "Maya could not find the X-GenTools footer label '{}'.".format(
                    control_name
                )
            )
        label = wrap_instance(int(pointer), QtWidgets.QWidget)
        label.setStyleSheet("color: rgb(153, 153, 153);")


def _set_dropdown_placeholder_color(menu_name, placeholder_label):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    items = cmds.optionMenu(menu_name, query=True, itemListLong=True) or []
    value = (
        cmds.optionMenu(menu_name, query=True, value=True) if items else ""
    )
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtGui
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtGui
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    pointer = omui.MQtUtil.findControl(menu_name)
    if not pointer:
        raise RuntimeError(
            "Maya could not find the X-GenTools dropdown '{}'.".format(
                menu_name
            )
        )
    menu = wrap_instance(int(pointer), QtWidgets.QComboBox)
    if menu_name == "xGenToolsTemplatePath":
        for index in range(menu.count()):
            item_color = (
                QtGui.QColor(220, 220, 220)
                if menu.itemText(index) == placeholder_label
                else QtGui.QColor(255, 255, 255)
            )
            menu.setItemData(
                index,
                QtGui.QBrush(item_color),
                QtCore.Qt.ForegroundRole,
            )
    if value == placeholder_label:
        menu.setStyleSheet(
            "QComboBox { background-color: rgb(66, 66, 66); "
            "color: rgb(220, 220, 220); }"
        )
    else:
        menu.setStyleSheet("")


_DROPDOWN_HOVER_FILTERS = []


def _install_dropdown_hover_effects():
    """Lighten dropdown backgrounds by about 25% while hovered."""
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    class DropdownHoverFilter(QtCore.QObject):
        def __init__(self, widget, parent=None):
            super(DropdownHoverFilter, self).__init__(parent)
            self.widget = widget
            self.normal_style = ""

        def eventFilter(self, watched, event):
            if event.type() == QtCore.QEvent.Enter:
                self.normal_style = self.widget.styleSheet()
                self.widget.setStyleSheet(
                    self.normal_style
                    + " QComboBox { background-color: rgb(66, 66, 66); }"
                )
                self.widget.update()
            elif event.type() == QtCore.QEvent.Leave:
                self.widget.setStyleSheet(self.normal_style)
                self.widget.update()
            return False

    _DROPDOWN_HOVER_FILTERS[:] = []
    for control_name in (
        "xGenToolsTemplatePath",
        "xGenToolsGenerationGroup",
        "xGenToolsGuideGroup",
        "xGenToolsFromPrefix",
        "xGenToolsToPrefix",
        "xGenToolsApplyMaterial",
    ):
        pointer = omui.MQtUtil.findControl(control_name)
        if not pointer:
            continue
        widget = wrap_instance(int(pointer), QtWidgets.QComboBox)
        hover_filter = DropdownHoverFilter(widget, widget)
        widget.setMouseTracking(True)
        widget.installEventFilter(hover_filter)
        _DROPDOWN_HOVER_FILTERS.append(hover_filter)


def _style_action_button(
    control_name,
    pressed_color,
    hover_color,
    text_color="rgb(0, 0, 0)",
    pressed_text_color="white",
    font_weight="bold",
):
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    pointer = omui.MQtUtil.findControl(control_name)
    if not pointer:
        return
    button = wrap_instance(int(pointer), QtWidgets.QWidget)
    normal_style = "QPushButton { color: %s; font-weight: %s; }" % (
        text_color,
        font_weight,
    )
    button.setStyleSheet(normal_style)
    effect = ActionButtonPressEffect(
        button,
        pressed_color,
        hover_color,
        pressed_text_color,
        text_color,
        font_weight,
    )
    button.installEventFilter(effect)
    _ACTION_BUTTON_FILTERS.append(effect)


_ACTION_BUTTON_FILTERS = []


class ActionButtonPressEffect:
    """Apply explicit colors during mouse and keyboard press/release."""

    def __new__(cls, *args, **kwargs):
        try:
            from PySide6 import QtCore
        except ImportError:
            from PySide2 import QtCore

        normal_style = "QPushButton { color: %s; font-weight: %s; }" % (
            args[4], args[5]
        )

        class _Filter(QtCore.QObject):
            def __init__(self, widget, pressed_color, hover_color, pressed_text, text_color, weight, normal_style):
                super(_Filter, self).__init__(widget)
                self.widget = widget
                self.normal_style = normal_style
                self.hover_style = self._color_style(hover_color, text_color, weight)
                self.pressed_style = (
                    "QPushButton {{ background-color: rgb({}, {}, {}); "
                    "border: 1px solid rgb({}, {}, {}); "
                    "color: {}; font-weight: {}; }}".format(
                        pressed_color[0],
                        pressed_color[1],
                        pressed_color[2],
                        max(0, pressed_color[0] - 18),
                        max(0, pressed_color[1] - 18),
                        max(0, pressed_color[2] - 18),
                        pressed_text,
                        weight,
                    )
                )

            def _color_style(self, color, text, weight):
                return (
                    "QPushButton {{ background-color: rgb({}, {}, {}); "
                    "border: 1px solid rgb({}, {}, {}); color: {}; "
                    "font-weight: {}; }}".format(
                        color[0], color[1], color[2],
                        max(0, color[0] - 18),
                        max(0, color[1] - 18),
                        max(0, color[2] - 18),
                        text, weight,
                    )
                )

            def eventFilter(self, watched, event):
                event_type = event.type()
                if event_type in (QtCore.QEvent.MouseButtonPress, QtCore.QEvent.KeyPress):
                    self.widget.setStyleSheet(self.pressed_style)
                    self.widget.update()
                elif event_type in (QtCore.QEvent.Enter,):
                    self.widget.setStyleSheet(self.hover_style)
                    self.widget.update()
                elif event_type == QtCore.QEvent.Leave:
                    self.widget.setStyleSheet(self.normal_style)
                    self.widget.update()
                elif event_type in (QtCore.QEvent.MouseButtonRelease, QtCore.QEvent.KeyRelease):
                    self.widget.setStyleSheet(
                        self.hover_style if self.widget.underMouse() else self.normal_style
                    )
                    self.widget.update()
                return False

        return _Filter(*args, normal_style=normal_style, **kwargs)


_STEP_HOVER_FILTERS = []


def _install_step_hover_effects():
    """Lighten numbered labels and turn their digit white on hover."""
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    class StepHoverFilter(QtCore.QObject):
        def __init__(self, widget, original_text, parent=None):
            super(StepHoverFilter, self).__init__(parent)
            self.widget = widget
            self.original_text = original_text
            self.normal_style = "font-weight: bold;"
            self.hover_style = (
                "background-color: rgb(51, 49, 77); "
                "border: 1px solid rgb(33, 31, 59); "
                "color: white; font-weight: bold;"
            )
            self.widget.setStyleSheet(self.normal_style)

        def eventFilter(self, watched, event):
            if event.type() == QtCore.QEvent.Enter:
                self.widget.setStyleSheet(self.hover_style)
            elif event.type() == QtCore.QEvent.Leave:
                self.widget.setStyleSheet(self.normal_style)
            return False

    _STEP_HOVER_FILTERS[:] = []
    for control_name, digit in (
        ("xGenToolsStep1", "1"),
        ("xGenToolsStep2", "2"),
        ("xGenToolsStep3", "3"),
        ("xGenToolsStep4", "4"),
        ("xGenToolsStep5", "5"),
    ):
        pointer = omui.MQtUtil.findControl(control_name)
        if not pointer:
            continue
        widget = wrap_instance(int(pointer), QtWidgets.QLabel)
        hover_filter = StepHoverFilter(widget, digit, widget)
        widget.setMouseTracking(True)
        widget.installEventFilter(hover_filter)
        _STEP_HOVER_FILTERS.append(hover_filter)


_FAST_TOOLTIP_FILTERS = []


def _install_fast_tooltips():
    """Show selected controls' existing section help with a short delay."""
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore, QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
    except ImportError:
        from PySide2 import QtCore, QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance

    class FastTooltipFilter(QtCore.QObject):
        def __init__(
            self,
            widget,
            tooltip_html,
            delay_ms=120,
            icon_control=None,
            parent=None,
        ):
            super(FastTooltipFilter, self).__init__(parent)
            self.widget = widget
            self.tooltip_html = tooltip_html
            self.icon_control = icon_control
            self.timer = QtCore.QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.setInterval(delay_ms)
            self.timer.timeout.connect(self._show_tooltip)

        def _show_tooltip(self):
            if self.widget.underMouse():
                position = self.widget.mapToGlobal(
                    QtCore.QPoint(0, self.widget.height())
                )
                QtWidgets.QToolTip.showText(
                    position,
                    self.tooltip_html,
                    self.widget,
                    QtCore.QRect(),
                    2147483647,
                )

        def eventFilter(self, watched, event):
            if event.type() == QtCore.QEvent.Enter:
                if self.icon_control:
                    cmds.iconTextButton(
                        self.icon_control, edit=True, image="help_line.png"
                    )
                self.timer.start()
            elif event.type() in (
                QtCore.QEvent.MouseButtonPress,
                QtCore.QEvent.MouseButtonRelease,
            ):
                self.timer.start()
            elif event.type() == QtCore.QEvent.Leave:
                self.timer.stop()
                QtWidgets.QToolTip.hideText()
                if self.icon_control:
                    cmds.iconTextButton(
                        self.icon_control, edit=True, image="help.png"
                    )
            elif event.type() == QtCore.QEvent.ToolTip:
                return True
            return False

    _FAST_TOOLTIP_FILTERS[:] = []
    sections = (
        ("xGenToolsStep1", "xGenToolsTemplatePath", cmds.optionMenu),
        ("xGenToolsStep2", "xGenToolsGenerationGroup", cmds.optionMenu),
        ("xGenToolsStep3", "xGenToolsGuideGroup", cmds.optionMenu),
        ("xGenToolsStep4", "xGenToolsFromPrefix", cmds.optionMenu),
        ("xGenToolsStep5", "xGenToolsApplyMaterial", cmds.optionMenu),
    )
    control_help = [
        ("xGenToolsFooterHelp", cmds.iconTextButton(
            "xGenToolsFooterHelp", query=True, annotation=True
        )),
    ]
    for control_name in (
        "xGenToolsSaveTemplateButton",
        "xGenToolsLoadButton",
        "xGenToolsResetButton",
    ):
        control_help.append(
            (
                control_name,
                cmds.button(control_name, query=True, annotation=True),
            )
        )
    for label_name, source_name, source_command in sections:
        section_tooltip = source_command(
            source_name, query=True, annotation=True
        )
        control_help.append(
            (label_name, section_tooltip)
        )
        # Keep the section help on its numbered label, not on the dropdown.
        source_command(source_name, edit=True, annotation="")
    cmds.optionMenu("xGenToolsToPrefix", edit=True, annotation="")

    for control_name, tooltip_html in control_help:
        if not tooltip_html:
            continue
        pointer = omui.MQtUtil.findControl(control_name)
        if not pointer:
            continue
        widget = wrap_instance(int(pointer), QtWidgets.QWidget)
        widget.setToolTip(tooltip_html)
        delay_ms = 0 if control_name in {
            "xGenToolsStep1",
            "xGenToolsStep2",
            "xGenToolsStep3",
            "xGenToolsStep4",
            "xGenToolsStep5",
        } else 120
        tooltip_filter = FastTooltipFilter(
            widget,
            tooltip_html,
            delay_ms=delay_ms,
            icon_control=(
                "xGenToolsFooterHelp"
                if control_name == "xGenToolsFooterHelp"
                else None
            ),
            parent=widget,
        )
        widget.installEventFilter(tooltip_filter)
        _FAST_TOOLTIP_FILTERS.append(tooltip_filter)


def _resolve_template_menu_path(menu_name, display_option_var, path_option_var):
    display_name = cmds.optionMenu(menu_name, query=True, value=True).strip()
    if not display_name or display_name == _template_fallback_label():
        return ""
    saved_path = _read_option_var_string(path_option_var)
    saved_display = _read_option_var_string(display_option_var)
    if saved_path and display_name == saved_display:
        return os.path.normpath(saved_path)
    return _resolve_template_path(display_name)


def _resolve_template_path(path):
    path = (path or "").strip()
    if not path:
        raise ValueError("Choose a template filename.")

    if path.startswith("./") or path.startswith(".\\"):
        path = path[2:]
    if not os.path.isabs(path):
        path = os.path.join(_template_directory(), path)

    if not path.lower().endswith(".json"):
        path += ".json"
    return os.path.normpath(path)


def _scene_materials():
    return sorted(set(cmds.ls(materials=True) or []), key=str.lower)


def _template_json_files():
    template_directory = _template_directory()
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


def _populate_menu_or_fallback(menu_name, values, fallback_label):
    if values:
        for value in values:
            cmds.menuItem(label=value, parent=menu_name)
        return values

    cmds.menuItem(
        label=fallback_label, parent=menu_name, enable=False
    )
    return [fallback_label]


def _template_fallback_label():
    return SELECTED_TEMPLATE_LABEL


def _refresh_template_menu(menu_name, display_option_var, path_option_var):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    existing_items = cmds.optionMenu(
        menu_name, query=True, itemListLong=True
    ) or []
    current_display = (
        cmds.optionMenu(menu_name, query=True, value=True)
        if existing_items
        else ""
    )
    saved_display = _read_option_var_string(display_option_var)
    saved_path = _read_option_var_string(path_option_var)
    file_names = _template_json_files()
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
    fallback_label = _template_fallback_label()
    menu_values = _populate_menu_or_fallback(
        menu_name, file_names, fallback_label
    )

    selected_value = (
        current_display
        if current_display in menu_values
        else (
            saved_display
            if saved_display in menu_values
            else menu_values[0]
        )
    )
    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(file_names),
    )
    _set_dropdown_placeholder_color(menu_name, fallback_label)


def refresh_save_template_menu(*_):
    _refresh_template_menu(
        "xGenToolsTemplatePath",
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )


def _scene_group_names():
    groups = []
    # Assemblies are the only DAG nodes that can qualify as top-level groups.
    # Avoid querying children and parents for every transform in a large scene.
    for node in cmds.ls(assemblies=True, type="transform", long=True) or []:
        children = cmds.listRelatives(
            node, children=True, type="transform", fullPath=True
        ) or []
        if children:
            groups.append(_leaf_name(node))
    return sorted(groups, key=str.lower)


def refresh_generation_group_menu(*_, group_names=None):
    menu_name = "xGenToolsGenerationGroup"
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = _read_option_var_string(
        OPTION_VAR_GENERATION_GROUP, "GENERATION_BASES"
    )
    for item in cmds.optionMenu(menu_name, query=True, itemListLong=True) or []:
        cmds.deleteUI(item)

    if group_names is None:
        group_names = _scene_group_names()
    menu_values = _populate_menu_or_fallback(
        menu_name, group_names, SELECT_GROUP_LABEL
    )

    prefix_cache = {}

    def prefixes_for(group_name):
        if group_name not in prefix_cache:
            prefix_cache[group_name] = _prefixes_for_generation_group(
                group_name
            )
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
    _set_dropdown_placeholder_color(menu_name, SELECT_GROUP_LABEL)
    _refresh_prefix_menus(prefixes=selected_prefixes)


def refresh_guide_group_menu(*_, group_names=None):
    menu_name = "xGenToolsGuideGroup"
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = _read_option_var_string(
        OPTION_VAR_GUIDE_GROUP, "GUIDE_CURVES"
    )
    for item in cmds.optionMenu(menu_name, query=True, itemListLong=True) or []:
        cmds.deleteUI(item)

    if group_names is None:
        group_names = _scene_group_names()
    menu_values = _populate_menu_or_fallback(
        menu_name, group_names, SELECT_GROUP_LABEL
    )

    selected_value = (
        saved_value if saved_value in group_names else menu_values[0]
    )
    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(group_names),
    )
    _set_dropdown_placeholder_color(menu_name, SELECT_GROUP_LABEL)


def refresh_material_menu(*_):
    menu_name = "xGenToolsApplyMaterial"
    if not cmds.optionMenu(menu_name, exists=True):
        return

    saved_value = _read_option_var_string(
        OPTION_VAR_MATERIAL, SELECT_MATERIAL_LABEL
    )
    for item in cmds.optionMenu(menu_name, query=True, itemListLong=True) or []:
        cmds.deleteUI(item)

    scene_material_names = _scene_materials()
    if scene_material_names:
        material_names = [NO_CHANGE_MATERIAL] + scene_material_names
        _populate_menu_or_fallback(
            menu_name, material_names, SELECT_MATERIAL_LABEL
        )
    else:
        material_names = [NO_CHANGE_MATERIAL]
        cmds.menuItem(label=NO_CHANGE_MATERIAL, parent=menu_name)
        _populate_menu_or_fallback(
            menu_name, [], SELECT_MATERIAL_LABEL
        )

    selected_value = (
        saved_value
        if saved_value in material_names
        else (
            material_names[0]
            if scene_material_names
            else SELECT_MATERIAL_LABEL
        )
    )
    cmds.optionMenu(menu_name, edit=True, value=selected_value)
    _set_dropdown_placeholder_color(menu_name, SELECT_MATERIAL_LABEL)


def _refresh_scene_dropdowns(*_):
    refresh_save_template_menu()
    group_names = _scene_group_names()
    refresh_generation_group_menu(group_names=group_names)
    refresh_guide_group_menu(group_names=group_names)
    refresh_material_menu()


def _choose_template_save_path():
    template_directory = _template_directory()
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
    return _resolve_template_path(selected[0])


def _current_description():
    editor = xgg.DescriptionEditor
    if editor:
        palette = editor.currentPalette()
        description = editor.currentDescription()
        if palette and description:
            return palette, description

    raise RuntimeError(
        "Open the XGen Description Editor and select a description to save."
    )


def _current_palette():
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

    palette, description = _current_description()
    output_path = _resolve_template_path(path)
    if os.path.isdir(output_path):
        raise ValueError("The selected template path is a folder, not a file.")

    if os.path.exists(output_path):
        if not allow_overwrite:
            raise FileExistsError(
                "A template already exists at '{}'. Choose a new filename or "
                "allow overwrite.".format(output_path)
            )
        if confirm_overwrite and not _confirm_template_overwrite(output_path):
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


def _save_template_from_window(*_):
    try:
        path = _choose_template_save_path()
        if not path:
            return

        resolved_path = _resolve_template_path(path)
        overwriting = os.path.isfile(resolved_path)
        output_path = save_template(path, allow_overwrite=True, confirm_overwrite=False)
        if output_path:
            saved_display = os.path.basename(output_path)
            _write_option_var_string(OPTION_VAR_SAVE_TEMPLATE_DISPLAY, saved_display)
            _write_option_var_string(OPTION_VAR_SAVE_TEMPLATE_PATH, output_path)
            refresh_save_template_menu()
            cmds.optionMenu(
                "xGenToolsTemplatePath", edit=True, value=saved_display
            )
            _set_dropdown_placeholder_color(
                "xGenToolsTemplatePath", _template_fallback_label()
            )
            action = "Overwrote" if overwriting else "Saved"
            _show_completion_message(
                "{} Template: {}.".format(action, saved_display)
            )
    except Exception as error:
        cmds.warning("[X-Gen Template Tool] Save Template failed: {}".format(error))
        _show_message("Save Template Error", str(error), icon="critical")


def _resolve_apply_template_path():
    return _resolve_template_menu_path(
        "xGenToolsTemplatePath",
        OPTION_VAR_SAVE_TEMPLATE_DISPLAY,
        OPTION_VAR_SAVE_TEMPLATE_PATH,
    )


def _prefix_index(value, field_name):
    prefix = (value or "").strip().upper()
    if prefix.endswith("_"):
        prefix = prefix[:-1]
    if len(prefix) != 1 or prefix < "A" or prefix > "Z":
        raise ValueError(
            "{} must be one letter, optionally followed by an underscore.".format(
                field_name
            )
        )
    return ord(prefix) - ord("A")


def _resolve_scene_group(value, field_name):
    matches = cmds.ls(
        (value or "").strip(), long=True, type="transform"
    ) or []
    if len(matches) != 1:
        raise ValueError(
            "The {} group must resolve to exactly one Outliner transform.".format(
                field_name
            )
        )
    return matches[0]


def _scene_generation_prefixes():
    menu_name = "xGenToolsGenerationGroup"
    if not cmds.optionMenu(menu_name, exists=True):
        return []

    generation_group = cmds.optionMenu(menu_name, query=True, value=True)
    if not generation_group or generation_group == SELECT_GROUP_LABEL:
        return []

    return _prefixes_for_generation_group(generation_group)


def _prefixes_for_generation_group(generation_group):
    if (
        not generation_group
        or generation_group == SELECT_GROUP_LABEL
        or not cmds.objExists(generation_group)
    ):
        return []

    try:
        generation_root = _resolve_scene_group(
            generation_group, "Generation Bases"
        )
    except ValueError:
        return []
    prefixes = set()
    mesh_shapes = cmds.ls(
        generation_root,
        dag=True,
        type="mesh",
        noIntermediate=True,
        long=True,
    ) or []
    for shape in mesh_shapes:
        node = shape.rsplit("|", 1)[0]
        match = GEO_PATTERN.match(_leaf_name(node))
        if not match:
            continue
        prefixes.add(match.group(1).upper() + "_")
    return sorted(prefixes)


def _refresh_prefix_menu(menu_name, option_var_name, prefixes, default_index):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    for item in cmds.optionMenu(menu_name, query=True, itemListLong=True) or []:
        cmds.deleteUI(item)
    menu_values = _populate_menu_or_fallback(
        menu_name, prefixes, SELECT_PREFIX_LABEL
    )

    if prefixes:
        default_value = prefixes[default_index]
        saved_value = _read_option_var_string(option_var_name, default_value)
        selected_value = (
            saved_value if saved_value in prefixes else default_value
        )
    else:
        selected_value = SELECT_PREFIX_LABEL

    cmds.optionMenu(
        menu_name,
        edit=True,
        value=selected_value,
        enable=bool(prefixes),
    )
    _set_dropdown_placeholder_color(menu_name, SELECT_PREFIX_LABEL)


def refresh_from_prefix_menu(*_):
    _refresh_prefix_menu(
        "xGenToolsFromPrefix",
        OPTION_VAR_FROM_PREFIX,
        _scene_generation_prefixes(),
        0,
    )


def refresh_to_prefix_menu(*_):
    _refresh_prefix_menu(
        "xGenToolsToPrefix",
        OPTION_VAR_TO_PREFIX,
        _scene_generation_prefixes(),
        -1,
    )


def _refresh_prefix_menus(*_, prefixes=None):
    if not cmds.optionMenu("xGenToolsFromPrefix", exists=True) or not cmds.optionMenu(
        "xGenToolsToPrefix", exists=True
    ):
        return

    if prefixes is None:
        prefixes = _scene_generation_prefixes()
    _refresh_prefix_menu(
        "xGenToolsFromPrefix",
        OPTION_VAR_FROM_PREFIX,
        prefixes,
        0,
    )
    _refresh_prefix_menu(
        "xGenToolsToPrefix",
        OPTION_VAR_TO_PREFIX,
        prefixes,
        -1,
    )


def _leaf_name(node):
    return node.rsplit("|", 1)[-1]


def _curve_transforms(group):
    shapes = cmds.ls(
        group,
        dag=True,
        type="nurbsCurve",
        noIntermediate=True,
        long=True,
    ) or []
    return sorted({shape.rsplit("|", 1)[0] for shape in shapes})


def _collect_apply_targets(
    generation_group,
    guide_group,
    from_prefix,
    to_prefix,
    includes_preset_guides,
):
    start_index = _prefix_index(from_prefix, "From")
    end_index = _prefix_index(to_prefix, "To")
    if start_index > end_index:
        raise ValueError("The From prefix must come before the To prefix.")

    generation_root = _resolve_scene_group(generation_group, "Generation Bases")
    guide_root = _resolve_scene_group(guide_group, "Guide Curves")
    generation_shapes = cmds.ls(
        generation_root,
        dag=True,
        type="mesh",
        noIntermediate=True,
        long=True,
    ) or []
    generation_nodes = {
        shape.rsplit("|", 1)[0] for shape in generation_shapes
    }
    matching_generation_nodes = []
    for node in sorted(generation_nodes):
        base_name = _leaf_name(node)
        match = GEO_PATTERN.match(base_name)
        if not match:
            continue
        letter = match.group(1).upper()
        letter_index = ord(letter) - ord("A")
        if start_index <= letter_index <= end_index:
            matching_generation_nodes.append((node, base_name, letter))

    if not matching_generation_nodes:
        raise ValueError(
            "No *_GEO meshes in '{}' matched the selected prefix range.".format(
                generation_root
            )
        )

    guide_nodes = [
        guide_root
    ] + (
        cmds.listRelatives(
            guide_root,
            allDescendents=True,
            type="transform",
            fullPath=True,
        )
        or []
    )

    guide_groups = {}
    for node in guide_nodes:
        name = _leaf_name(node)
        if name.endswith("_CURVES"):
            guide_groups.setdefault(name, []).append(node)

    expected_guide_names = {
        base_name[:-4] + "_CURVES"
        for _node, base_name, _letter in matching_generation_nodes
    }
    matching_guide_paths = [
        group_path
        for group_name in expected_guide_names
        for group_path in guide_groups.get(group_name, [])
    ]
    guide_group_paths = set(matching_guide_paths)
    curves_by_guide_group = {}
    guide_shapes = (
        cmds.ls(
            matching_guide_paths,
            dag=True,
            type="nurbsCurve",
            noIntermediate=True,
            long=True,
        )
        or []
        if matching_guide_paths
        else []
    )
    for shape in guide_shapes:
        curve_transform = shape.rsplit("|", 1)[0]
        node = curve_transform
        while node:
            if node in guide_group_paths:
                curves_by_guide_group.setdefault(node, set()).add(
                    curve_transform
                )
                break
            if "|" not in node:
                break
            node = node.rsplit("|", 1)[0]
    curves_by_guide_group = {
        group_path: sorted(curve_transforms)
        for group_path, curve_transforms in curves_by_guide_group.items()
    }

    targets = []
    for node, base_name, letter in matching_generation_nodes:
        expected_guide_group = base_name[:-4] + "_CURVES"
        matching_groups = guide_groups.get(expected_guide_group, [])
        if len(matching_groups) != 1:
            raise ValueError(
                "Expected one guide group named '{}' for '{}'.".format(
                    expected_guide_group, base_name
                )
            )

        curves = curves_by_guide_group.get(matching_groups[0], [])
        if not curves and not includes_preset_guides:
            raise ValueError(
                "No NURBS guide curves were found in '{}' and the template has no "
                "saved guides.".format(expected_guide_group)
            )

        targets.append(
            {
                "letter": letter,
                "base": node,
                "base_name": base_name,
                "description": base_name[:-4] + "_Description",
                "guide_group": matching_groups[0],
                "curves": curves,
            }
        )

    description_names = [target["description"] for target in targets]
    if len(description_names) != len(set(description_names)):
        raise ValueError("The selected generation bases produce duplicate descriptions.")

    return generation_root, guide_root, targets


def _load_template(path):
    template_path = _resolve_template_path(path)
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
    if not isinstance(template_data.get("xgen_preset"), str) or not template_data[
        "xgen_preset"
    ].strip():
        raise ValueError("The template does not contain an XGen description preset.")
    if not isinstance(template_data.get("includes_guides"), bool):
        raise ValueError("The template has an invalid guide-data setting.")
    output_renderer = template_data.setdefault(
        "output_renderer", DEFAULT_XGEN_OUTPUT_RENDERER
    )
    if not isinstance(output_renderer, str):
        raise ValueError("The template has an invalid output renderer setting.")

    return template_path, template_data


class _TargetDescriptionValidator:
    def __init__(self, palette, description):
        self.action = xg.ADD_TO_EXISTING_PALETTE
        self.palette = palette
        self.description = description

    def __call__(self, _source_description, _source_palette, _index):
        return True, self.description, self.palette


def _mel_string(value):
    return '"{}"'.format(value.replace("\\", "\\\\").replace('"', '\\"'))


def _show_completion_message(message):
    """Show a short, fading completion notice in Maya's active viewport."""
    cmds.inViewMessage(
        message=html.escape(message),
        position="topCenter",
        fade=True,
        fadeInTime=250,
        fadeStayTime=2200,
        fadeOutTime=500,
        alpha=0.9,
        textAlpha=1.0,
        backColor=0xCC303030,
    )


def _convert_curves_to_guides(curves, description):
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
            _leaf_name(transform): index
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
            transform_name = _leaf_name(shape.rsplit("|", 1)[0])
            curve_index = transform_indices[transform_name]
            shape_index = shape_indices.get(curve_index, 0)
            shape_indices[curve_index] = shape_index + 1
            shape_name = "{}_{}_shape{}".format(
                name_prefix, curve_index, shape_index
            )
            renamed_shape = cmds.rename(shape, shape_name)
            curve_shapes.append(renamed_shape)

        if not curve_shapes:
            raise RuntimeError(
                "No NURBS curve shapes were available for '{}'.".format(description)
            )

        cmds.select(curve_shapes, replace=True)
        mel.eval(
            "xgmCurveToGuide -d {} -tsp 1 -tsa 0".format(
                _mel_string(description)
            )
        )
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

    shading_engines = cmds.listConnections(
        materials[0],
        source=False,
        destination=True,
        type="shadingEngine",
    ) or []
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
            texels_per_unit = xg.getAttr(
                "texelsPerUnit", palette, description, module
            )
            radius_variance = xg.getAttr(
                "radiusVariance", palette, description, module
            )
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
                "[X-GenTools] Could not regenerate modifier maps for {}".format(
                    warning
                )
            )

    return warnings


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

    _, template_data = _load_template(path)
    palette = _current_palette()
    generation_root, _, targets = _collect_apply_targets(
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
        if not _confirm_description_replacement(replacements):
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
                    _TargetDescriptionValidator(
                        palette, target_description
                    ),
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

                output_renderer = template_data["output_renderer"]
                if output_renderer:
                    renderer_object = xg.getActive(
                        palette, target_description, "Renderer"
                    )
                    if not renderer_object or not xg.attrExists(
                        "renderer", palette, target_description, renderer_object
                    ):
                        raise RuntimeError(
                            "Could not find the output renderer setting for '{}'."
                            .format(target_description)
                        )
                    if not xg.setAttr(
                        "renderer",
                        output_renderer,
                        palette,
                        target_description,
                        renderer_object,
                    ):
                        raise RuntimeError(
                            "Could not set '{}' to '{}' for '{}'.".format(
                                renderer_object,
                                output_renderer,
                                target_description,
                            )
                        )

                if target["curves"]:
                        _convert_curves_to_guides(
                            target["curves"], target_description
                        )

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
                        "[X-GenTools] Shader cleanup failed during rollback: {}"
                        .format(cleanup_error)
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
            _mel_string(description) for description in created_descriptions
        )
        mel.eval("xgmPreview {{{}}}".format(descriptions))
    except Exception as error:
        preview_warning = str(error)
        cmds.warning(
            "[X-GenTools] Descriptions were applied, but preview failed: {}".format(
                error
            )
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


def _apply_from_window(*_):
    try:
        path = _resolve_apply_template_path()

        generation_group = cmds.optionMenu(
            "xGenToolsGenerationGroup", query=True, value=True
        )
        guide_group = cmds.optionMenu(
            "xGenToolsGuideGroup", query=True, value=True
        )
        from_prefix = cmds.optionMenu(
            "xGenToolsFromPrefix", query=True, value=True
        )
        to_prefix = cmds.optionMenu(
            "xGenToolsToPrefix", query=True, value=True
        )
        material = cmds.optionMenu(
            "xGenToolsApplyMaterial", query=True, value=True
        )
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
        _show_completion_message("{}.".format(completion))
        if warnings:
            _show_message(
                "X-GenTools Apply Warning",
                "\n".join(warnings),
                icon="warning",
            )
    except Exception as error:
        cmds.warning("[X-GenTools] Load Template failed: {}".format(error))
        _show_message("Load Template Error", str(error), icon="critical")


def clean_start():
    """Delete all descriptions in the active XGen collection after confirmation."""
    palette = _current_palette()
    descriptions = list(xg.descriptions(palette) or [])
    if not descriptions:
        return []

    if not _confirm_clean_start(palette, descriptions):
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


def _clean_start_from_window(*_):
    try:
        deleted_descriptions = clean_start()
        if deleted_descriptions is None:
            return
        if deleted_descriptions:
            _show_completion_message(
                "Deleted {} Description(s).".format(
                    len(deleted_descriptions)
                )
            )
        else:
            _show_completion_message("No descriptions to delete.")
    except Exception as error:
        cmds.warning("[X-GenTools] Clean Start failed: {}".format(error))
        _show_message("Clean Start Error", str(error), icon="critical")


def _workspace_ui_script():
    return (
        "from characters import xgen_template_tool; "
        "xgen_template_tool._build_ui()"
    )


def _set_workspace_control_fixed_width():
    import maya.OpenMayaUI as omui

    try:
        from PySide6 import QtCore
        from PySide6 import QtWidgets
        import shiboken6

        wrap_instance = shiboken6.wrapInstance
        is_valid = shiboken6.isValid
    except ImportError:
        from PySide2 import QtCore
        from PySide2 import QtWidgets
        import shiboken2

        wrap_instance = shiboken2.wrapInstance
        is_valid = shiboken2.isValid

    pointer = omui.MQtUtil.findControl(WORKSPACE_CONTROL_NAME)
    if not pointer:
        raise RuntimeError(
            "Maya could not find the X-GenTools workspace control."
        )
    control = wrap_instance(int(pointer), QtWidgets.QWidget)

    def fit_floating_window():
        if not is_valid(control):
            return
        if not cmds.workspaceControl(
            WORKSPACE_CONTROL_NAME, query=True, exists=True
        ):
            return
        if not cmds.workspaceControl(
            WORKSPACE_CONTROL_NAME, query=True, floating=True
        ):
            return

        control.adjustSize()
        floating_window = control.window()
        target_size = QtCore.QSize(control.width(), control.height())
        # Ignore Maya's wider dock-tab size hint and lock to the content size.
        floating_window.setFixedSize(target_size)

    legacy_filter = control.findChild(
        QtCore.QObject, "xGenToolsFloatingSizeFilter"
    )
    if legacy_filter is not None:
        legacy_filter.deleteLater()

    legacy_timer = control.findChild(
        QtCore.QTimer, "xGenToolsFloatingSizeTimer"
    )
    if legacy_timer is not None:
        legacy_timer.stop()
        legacy_timer.deleteLater()

    timer_name = "xGenToolsFloatingSizeTimerV2"
    timer = control.findChild(QtCore.QTimer, timer_name)
    if timer is None:
        # Maya does not reliably signal workspace dock/float transitions.
        floating_state = {
            "value": cmds.workspaceControl(
                WORKSPACE_CONTROL_NAME, query=True, floating=True
            )
        }
        timer = QtCore.QTimer(control)
        timer.setObjectName(timer_name)
        timer.setInterval(200)

        def watch_floating_state():
            if not is_valid(control):
                return
            if not cmds.workspaceControl(
                WORKSPACE_CONTROL_NAME, query=True, exists=True
            ):
                timer.stop()
                return

            is_floating = cmds.workspaceControl(
                WORKSPACE_CONTROL_NAME, query=True, floating=True
            )
            if is_floating and not floating_state["value"]:
                QtCore.QTimer.singleShot(100, fit_floating_window)
            floating_state["value"] = is_floating

        timer.timeout.connect(watch_floating_state)
        timer.start()

    control.setFixedWidth(WINDOW_WIDTH)
    control.updateGeometry()
    QtWidgets.QApplication.processEvents()
    fit_floating_window()


def show():
    """Open or restore the dockable X-Gen Template Tool panel."""
    if cmds.window(LEGACY_WINDOW_NAME, exists=True):
        cmds.deleteUI(LEGACY_WINDOW_NAME)

    if cmds.workspaceControl(WORKSPACE_CONTROL_NAME, query=True, exists=True):
        cmds.workspaceControl(
            WORKSPACE_CONTROL_NAME,
            edit=True,
            label=WINDOW_TITLE,
            restore=True,
            initialWidth=WINDOW_WIDTH,
            minimumWidth=WINDOW_WIDTH,
            widthProperty="fixed",
            loadImmediately=True,
            checksPlugins=True,
            requiredPlugin="xgenToolkit",
            uiScript=_workspace_ui_script(),
        )
        _build_ui()
        return

    cmds.workspaceControl(
        WORKSPACE_CONTROL_NAME,
        label=WINDOW_TITLE,
        retain=True,
        initialWidth=WINDOW_WIDTH,
        initialHeight=WINDOW_HEIGHT,
        minimumWidth=WINDOW_WIDTH,
        widthProperty="fixed",
        dockToMainWindow=("right", False),
        loadImmediately=True,
        checksPlugins=True,
        requiredPlugin="xgenToolkit",
        uiScript=_workspace_ui_script(),
    )
    _build_ui()


def _build_ui():
    if cmds.scrollLayout(SCROLL_LAYOUT_NAME, exists=True):
        cmds.deleteUI(SCROLL_LAYOUT_NAME)
    # Maya may rebuild retained workspace controls and run the shelf command too.
    for child in cmds.layout(
        WORKSPACE_CONTROL_NAME, query=True, childArray=True
    ) or []:
        cmds.deleteUI(child)
    cmds.setParent(WORKSPACE_CONTROL_NAME)
    cmds.columnLayout(
        adjustableColumn=True,
        rowSpacing=0,
        columnAttach=("both", 4),
    )

    # Top Action Button: SAVE TEMPLATE
    cmds.button(
        "xGenToolsSaveTemplateButton",
        label="SAVE TEMPLATE",
        height=SECTION_HEADER_HEIGHT,
        backgroundColor=(0.52, 0.72, 0.53),
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='225' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td><b><i>Saves</i></b> or "
            "<b><i>Overwrites</i></b> a <b><i>.json File</i></b> "
            "<b><i>Template</i></b><br>"
            "of the current <b><i>Selected Description</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>Saved into "
            "<b><i>/xgen/template</i></b> folder.</td></tr>"
            "</table></span>"
        ),
        command=_save_template_from_window,
    )
    _style_action_button(
        "xGenToolsSaveTemplateButton",
        pressed_color=(46, 75, 48),
        hover_color=(99, 184, 102),
        pressed_text_color="white",
    )

    apply_row_color = (0.23, 0.22, 0.40)
    number_color = (0.57, 0.56, 0.78)
    field_color = (0.16, 0.16, 0.16)

    # Row 1: Selected Template Dropdown
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(ROW_NUMBER_WIDTH, WINDOW_CONTENT_WIDTH - ROW_NUMBER_WIDTH),
        columnAttach2=("both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=apply_row_color,
    )
    cmds.text(
        "xGenToolsStep1",
        label="1",
        align="center",
        height=24,
        backgroundColor=number_color,
    )
    cmds.optionMenu(
        "xGenToolsTemplatePath",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_save_template_selection,
        beforeShowPopup=refresh_save_template_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='210' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> the <b><i>Saved Template</i></b> you want<br>"
            "to apply to your <b><i>Generation Bases</i></b>.</td></tr>"
            "</table></span>"
        ),
    )
    cmds.setParent("..")
    refresh_save_template_menu()

    # Row 2: Generation Bases Group
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(ROW_NUMBER_WIDTH, WINDOW_CONTENT_WIDTH - ROW_NUMBER_WIDTH),
        columnAttach2=("both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=apply_row_color,
    )
    cmds.text(
        "xGenToolsStep2",
        label="2",
        align="center",
        height=24,
        backgroundColor=number_color,
    )
    cmds.optionMenu(
        "xGenToolsGenerationGroup",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_generation_group_selection,
        beforeShowPopup=refresh_generation_group_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='235' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> the <b><i>Top-Level Group</i></b> in the "
            "<b><i>Outliner</i></b> "
            "containing the <b><i>Generation Bases</i></b>.</td></tr>"
            "</table></span>"
        ),
    )
    cmds.setParent("..")
    refresh_generation_group_menu()

    # Row 3: Guide Curves Group
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(ROW_NUMBER_WIDTH, WINDOW_CONTENT_WIDTH - ROW_NUMBER_WIDTH),
        columnAttach2=("both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=apply_row_color,
    )
    cmds.text(
        "xGenToolsStep3",
        label="3",
        align="center",
        height=24,
        backgroundColor=number_color,
    )
    cmds.optionMenu(
        "xGenToolsGuideGroup",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_guide_group_selection,
        beforeShowPopup=refresh_guide_group_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='235' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> the <i>Top-Level Group</i> in the "
            "<b><i>Outliner</i></b><br>"
            "containing the <b><i>Guide Curves</i></b>.</td></tr>"
            "</table></span>"
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
        backgroundColor=apply_row_color,
    )
    cmds.text(
        "xGenToolsStep4",
        label="4",
        align="center",
        height=24,
        backgroundColor=number_color,
    )
    cmds.text(label="From", align="center", height=24)
    cmds.optionMenu(
        "xGenToolsFromPrefix",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_from_prefix_selection,
        beforeShowPopup=refresh_from_prefix_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='270' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> the <b><i>Prefix Range</i></b> to "
            "<b><i>Apply</i></b> across the<br>"
            "<b><i>Generation Bases</i></b> &amp; the matching "
            "<b><i>Guide Curves</i></b>.</td></tr>"
            "</table></span>"
        ),
    )
    cmds.text(label="To", align="center", height=24)
    cmds.optionMenu(
        "xGenToolsToPrefix",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_to_prefix_selection,
        beforeShowPopup=refresh_to_prefix_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='270' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> the <b><i>Prefix Range</i></b> to "
            "<b><i>Apply</i></b> across the<br>"
            "<b><i>Generation Bases</i></b> &amp; the matching "
            "<b><i>Guide Curves</i></b>.</td></tr>"
            "</table></span>"
        ),
    )
    cmds.setParent("..")
    _refresh_prefix_menus()

    # Row 5: Material Selection
    cmds.separator(height=3, style="none")
    cmds.rowLayout(
        numberOfColumns=2,
        adjustableColumn=2,
        columnWidth2=(ROW_NUMBER_WIDTH, WINDOW_CONTENT_WIDTH - ROW_NUMBER_WIDTH),
        columnAttach2=("both", "both"),
        height=FIELD_ROW_HEIGHT,
        backgroundColor=apply_row_color,
    )
    cmds.text(
        "xGenToolsStep5",
        label="5",
        align="center",
        height=24,
        backgroundColor=number_color,
    )
    cmds.optionMenu(
        "xGenToolsApplyMaterial",
        height=FIELD_HEIGHT,
        backgroundColor=field_color,
        changeCommand=_persist_material_selection,
        beforeShowPopup=refresh_material_menu,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='250' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Choose</i></b> the <b><i>Material</i></b> for all the "
            "<b><i>Descriptions</i></b><br>"
            "within the <b><i>Specified</i></b> <b><i>Range</i></b>."
            "</td></tr></table></span>"
        ),
    )
    cmds.setParent("..")
    refresh_material_menu()
    _install_dropdown_hover_effects()
    _install_step_hover_effects()
    cmds.scriptJob(
        event=("SceneOpened", _refresh_scene_dropdowns),
        parent=WORKSPACE_CONTROL_NAME,
        replacePrevious=True,
    )

    # LOAD TEMPLATE Button
    cmds.separator(height=3, style="none")
    cmds.button(
        "xGenToolsLoadButton",
        label="LOAD TEMPLATE",
        height=SECTION_HEADER_HEIGHT,
        backgroundColor=(0.53, 0.52, 0.78),
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='350' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td><b><i>Creates "
            "Descriptions</i></b> under the <b><i>Selected Collection</i></b> "
            "by pairing<br>"
            "<b><i>Generation Bases</i></b> to <b><i>Guide Curves</i></b> by "
            "naming convention<br>"
            "<b><i>Across The Range</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td><b><i>Copies All "
            "Settings</i></b> from the <b><i>Template</i></b> including "
            "<b><i>Modifiers</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>Applies the selected "
            "<b><i>Material</i></b> to the <b><i>Collection</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td><b><i>Hides</i></b> the "
            "<b><i>XGen Description Guides</i></b> &amp; "
            "<b><i>Previews All Descriptions</i></b>.</td></tr>"
            "</table></span>"
        ),
        command=_apply_from_window,
    )
    _style_action_button(
        "xGenToolsLoadButton",
        pressed_color=(51, 49, 77),
        hover_color=(105, 102, 199),
        pressed_text_color="white",
    )

    # CLEAN START Button
    cmds.separator(height=3, style="none")
    cmds.button(
        "xGenToolsResetButton",
        label="CLEAN START",
        height=SECTION_HEADER_HEIGHT,
        backgroundColor=CLEAN_START_HEADER_BACKGROUND,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='255' "
            "bgcolor='#3b3b3b'>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Deletes All Descriptions</i></b> from the "
            "<b><i>Collection</i></b>.<br>"
            "<b><i>Tweak The Curves</i></b> then "
            "<b><i>Reload The Template</i></b>.</td></tr>"
            "</table></span>"
        ),
        command=_clean_start_from_window,
    )
    _style_action_button(
        "xGenToolsResetButton",
        pressed_color=(83, 66, 2),
        hover_color=(214, 183, 57),
        pressed_text_color="white",
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
    cmds.text(
        label="",
        width=FOOTER_SIDE_PADDING,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    cmds.iconTextButton(
        "xGenToolsFooterHelp",
        style="iconOnly",
        image="help.png",
        width=18,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
        annotation=(
            "<span style='color: #ffffff;'>"
            "<table cellspacing='0' cellpadding='3' border='0' width='304' "
            "bgcolor='#3b3b3b'>"
            "<tr><td align='left'>"
            "<b><i>[[ WORKFLOW ]]</i></b></td></tr>"
            "<tr><td>"
            "<table cellspacing='0' cellpadding='3' border='0' width='298'>"
            "<tr><td width='8' valign='top'>•</td><td>Prepare your "
            "<b><i>Generation Bases &amp; Guide Curves</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>Finalize a "
            "<b><i>Description</i></b> under an existing "
            "<b><i>Collection</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Save Template</i></b> "
            "saves <b><i>All Settings</i></b> on <b><i>All Tabs</i></b>, "
            "<b><i>Set Stray Percentages</i></b> "
            "&amp; <b><i>Modifiers</i></b> to a "
            "<b><i>.json File</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Select</i></b> your "
            "<b><i>Template</i></b>, <b><i>Generation Base</i></b> | "
            "<b><i>Guide Curve</i></b><br>"
            "outliner groups, <b><i>Prefix Range</i></b> &amp; the display "
            "<b><i>Material</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Load Template</i></b> "
            "applies the template to all<br>"
            "the <b><i>Generation Bases</i></b> in the "
            "<b><i>Range Specified</i></b>.</td></tr>"
            "<tr><td width='8' valign='top'>•</td><td>"
            "<b><i>Clean Start</i></b> will "
            "remove <b><i>All Descriptions</i></b>. Tweak the<br>"
            "curves &amp; reload the template. "
            "<b><i>Iterate until happy. :-D</i></b></td></tr>"
            "</table></td></tr>"
            "</table></span>"
        ),
    )
    cmds.text(
        "xGenToolsFooterAuthor",
        label="InstructorJeff",
        align="left",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    cmds.text(
        "xGenToolsFooterVersion",
        label="V1.00",
        align="right",
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    cmds.text(
        label="",
        width=FOOTER_SIDE_PADDING,
        height=FOOTER_TEXT_HEIGHT,
        backgroundColor=CLEAN_START_BODY_BACKGROUND,
    )
    _install_fast_tooltips()
    _set_footer_text_color()
    cmds.setParent("..")

    cmds.setParent("..")
    _set_workspace_control_fixed_width()


if __name__ == "__main__":
    show()
