"""Qt styling for the panel: dropdown placeholder colors, hover and press effects, fast tooltips, fixed panel width."""

import maya.cmds as cmds

from characters.xgen_template.constants import (
    BUTTON_CLEAN_START,
    BUTTON_LOAD_TEMPLATE,
    BUTTON_SAVE_TEMPLATE,
    DROPDOWN_MENUS,
    FOOTER_AUTHOR,
    FOOTER_HELP,
    FOOTER_VERSION,
    MENU_FROM_PREFIX,
    MENU_GENERATION_GROUP,
    MENU_GUIDE_GROUP,
    MENU_MATERIAL,
    MENU_TEMPLATE,
    MENU_TO_PREFIX,
    STEP_1,
    STEP_2,
    STEP_3,
    STEP_4,
    STEP_5,
    STEP_LABELS,
    WINDOW_WIDTH,
    WORKSPACE_CONTROL_NAME,
)
from characters.xgen_template.qt import find_widget, load_qt

# Qt only keeps weak references to event filters, so the filters are held here.
_DROPDOWN_HOVER_FILTERS = []
_ACTION_BUTTON_FILTERS = []
_STEP_HOVER_FILTERS = []
_FAST_TOOLTIP_FILTERS = []


def set_footer_text_color():
    for control_name in (FOOTER_AUTHOR, FOOTER_VERSION):
        label = find_widget(control_name)
        if label is None:
            raise RuntimeError(
                "Maya could not find the X-GenTools footer label '{}'.".format(
                    control_name
                )
            )
        label.setStyleSheet("color: rgb(153, 153, 153);")


def set_dropdown_placeholder_color(menu_name, placeholder_label):
    if not cmds.optionMenu(menu_name, exists=True):
        return

    items = cmds.optionMenu(menu_name, query=True, itemListLong=True) or []
    value = cmds.optionMenu(menu_name, query=True, value=True) if items else ""
    qt = load_qt()
    QtCore, QtGui, QtWidgets = qt.QtCore, qt.QtGui, qt.QtWidgets

    menu = find_widget(menu_name, QtWidgets.QComboBox)
    if menu is None:
        raise RuntimeError(
            "Maya could not find the X-GenTools dropdown '{}'.".format(menu_name)
        )
    if menu_name == MENU_TEMPLATE:
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


def install_dropdown_hover_effects():
    """Lighten dropdown backgrounds by about 25% while hovered."""
    qt = load_qt()
    QtCore, QtWidgets = qt.QtCore, qt.QtWidgets

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
    for control_name in DROPDOWN_MENUS:
        widget = find_widget(control_name, QtWidgets.QComboBox)
        if widget is None:
            continue
        hover_filter = DropdownHoverFilter(widget, widget)
        widget.setMouseTracking(True)
        widget.installEventFilter(hover_filter)
        _DROPDOWN_HOVER_FILTERS.append(hover_filter)


def _create_action_button_filter(
    widget, pressed_color, hover_color, pressed_text, text_color, weight, normal_style
):
    """Event filter that applies explicit colors during mouse and keyboard press / release."""
    QtCore = load_qt().QtCore

    def color_style(color, text):
        return (
            "QPushButton {{ background-color: rgb({}, {}, {}); "
            "border: 1px solid rgb({}, {}, {}); color: {}; "
            "font-weight: {}; }}".format(
                color[0],
                color[1],
                color[2],
                max(0, color[0] - 18),
                max(0, color[1] - 18),
                max(0, color[2] - 18),
                text,
                weight,
            )
        )

    hover_style = color_style(hover_color, text_color)
    pressed_style = color_style(pressed_color, pressed_text)

    class ActionButtonFilter(QtCore.QObject):
        def eventFilter(self, watched, event):
            event_type = event.type()
            if event_type in (QtCore.QEvent.MouseButtonPress, QtCore.QEvent.KeyPress):
                widget.setStyleSheet(pressed_style)
                widget.update()
            elif event_type == QtCore.QEvent.Enter:
                widget.setStyleSheet(hover_style)
                widget.update()
            elif event_type == QtCore.QEvent.Leave:
                widget.setStyleSheet(normal_style)
                widget.update()
            elif event_type in (
                QtCore.QEvent.MouseButtonRelease,
                QtCore.QEvent.KeyRelease,
            ):
                widget.setStyleSheet(
                    hover_style if widget.underMouse() else normal_style
                )
                widget.update()
            return False

    return ActionButtonFilter(widget)


def style_action_button(
    control_name,
    pressed_color,
    hover_color,
    text_color="rgb(0, 0, 0)",
    pressed_text_color="white",
    font_weight="bold",
):
    button = find_widget(control_name)
    if button is None:
        return
    normal_style = "QPushButton { color: %s; font-weight: %s; }" % (
        text_color,
        font_weight,
    )
    button.setStyleSheet(normal_style)
    effect = _create_action_button_filter(
        button,
        pressed_color,
        hover_color,
        pressed_text_color,
        text_color,
        font_weight,
        normal_style,
    )
    button.installEventFilter(effect)
    _ACTION_BUTTON_FILTERS.append(effect)


def install_step_hover_effects():
    """Lighten numbered labels and turn their digit white on hover."""
    qt = load_qt()
    QtCore, QtWidgets = qt.QtCore, qt.QtWidgets

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
    for number, control_name in enumerate(STEP_LABELS, start=1):
        widget = find_widget(control_name, QtWidgets.QLabel)
        if widget is None:
            continue
        hover_filter = StepHoverFilter(widget, str(number), widget)
        widget.setMouseTracking(True)
        widget.installEventFilter(hover_filter)
        _STEP_HOVER_FILTERS.append(hover_filter)


def install_fast_tooltips():
    """Show selected controls' existing section help with a short delay."""
    qt = load_qt()
    QtCore, QtWidgets = qt.QtCore, qt.QtWidgets

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
                    cmds.iconTextButton(self.icon_control, edit=True, image="help.png")
            elif event.type() == QtCore.QEvent.ToolTip:
                return True
            return False

    _FAST_TOOLTIP_FILTERS[:] = []
    # (numbered label, dropdown whose help text moves onto that label)
    sections = (
        (STEP_1, MENU_TEMPLATE),
        (STEP_2, MENU_GENERATION_GROUP),
        (STEP_3, MENU_GUIDE_GROUP),
        (STEP_4, MENU_FROM_PREFIX),
        (STEP_5, MENU_MATERIAL),
    )
    control_help = [
        (FOOTER_HELP, cmds.iconTextButton(FOOTER_HELP, query=True, annotation=True)),
    ]
    for control_name in (
        BUTTON_SAVE_TEMPLATE,
        BUTTON_LOAD_TEMPLATE,
        BUTTON_CLEAN_START,
    ):
        control_help.append(
            (
                control_name,
                cmds.button(control_name, query=True, annotation=True),
            )
        )
    for label_name, source_name in sections:
        section_tooltip = cmds.optionMenu(source_name, query=True, annotation=True)
        control_help.append((label_name, section_tooltip))
        # Keep the section help on its numbered label, not on the dropdown.
        cmds.optionMenu(source_name, edit=True, annotation="")
    cmds.optionMenu(MENU_TO_PREFIX, edit=True, annotation="")

    for control_name, tooltip_html in control_help:
        if not tooltip_html:
            continue
        widget = find_widget(control_name)
        if widget is None:
            continue
        widget.setToolTip(tooltip_html)
        delay_ms = 0 if control_name in STEP_LABELS else 120
        tooltip_filter = FastTooltipFilter(
            widget,
            tooltip_html,
            delay_ms=delay_ms,
            icon_control=(FOOTER_HELP if control_name == FOOTER_HELP else None),
            parent=widget,
        )
        widget.installEventFilter(tooltip_filter)
        _FAST_TOOLTIP_FILTERS.append(tooltip_filter)


def set_workspace_control_fixed_width():
    qt = load_qt()
    QtCore, QtWidgets, is_valid = qt.QtCore, qt.QtWidgets, qt.is_valid

    control = find_widget(WORKSPACE_CONTROL_NAME)
    if control is None:
        raise RuntimeError("Maya could not find the X-GenTools workspace control.")

    def fit_floating_window():
        if not is_valid(control):
            return
        if not cmds.workspaceControl(WORKSPACE_CONTROL_NAME, query=True, exists=True):
            return
        if not cmds.workspaceControl(WORKSPACE_CONTROL_NAME, query=True, floating=True):
            return

        control.adjustSize()
        floating_window = control.window()
        target_size = QtCore.QSize(control.width(), control.height())
        # Ignore Maya's wider dock-tab size hint and lock to the content size.
        floating_window.setFixedSize(target_size)

    legacy_filter = control.findChild(QtCore.QObject, "xGenToolsFloatingSizeFilter")
    if legacy_filter is not None:
        legacy_filter.deleteLater()

    legacy_timer = control.findChild(QtCore.QTimer, "xGenToolsFloatingSizeTimer")
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
