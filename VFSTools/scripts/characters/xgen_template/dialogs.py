"""Message boxes and confirmations."""

import html
import os

import maya.cmds as cmds

from characters.xgen_template.paths import project_root
from characters.xgen_template.qt import load_qt, main_window


def show_message(title, message, icon="information"):
    cmds.confirmDialog(
        title=title,
        message=message,
        button=["OK"],
        defaultButton="OK",
        icon=icon,
    )


def show_completion_message(message):
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


def _ask(title, text, accept_label, reject_label):
    """Warning box with two buttons (the reject button is the default). True if the accept button was clicked."""
    qt = load_qt()
    QtCore, QtWidgets = qt.QtCore, qt.QtWidgets

    dialog = QtWidgets.QMessageBox(main_window())
    dialog.setWindowTitle(title)

    warning_icon = getattr(QtWidgets.QMessageBox, "Warning", None)
    if warning_icon is None:
        warning_icon = QtWidgets.QMessageBox.Icon.Warning
    dialog.setIcon(warning_icon)

    rich_text = getattr(QtCore.Qt, "RichText", None)
    if rich_text is None:
        rich_text = QtCore.Qt.TextFormat.RichText
    dialog.setTextFormat(rich_text)
    dialog.setText(text)

    accept_role = getattr(QtWidgets.QMessageBox, "AcceptRole", None)
    reject_role = getattr(QtWidgets.QMessageBox, "RejectRole", None)
    if accept_role is None:
        accept_role = QtWidgets.QMessageBox.ButtonRole.AcceptRole
    if reject_role is None:
        reject_role = QtWidgets.QMessageBox.ButtonRole.RejectRole
    accept_button = dialog.addButton(accept_label, accept_role)
    reject_button = dialog.addButton(reject_label, reject_role)
    dialog.setDefaultButton(reject_button)
    dialog.setEscapeButton(reject_button)

    execute = getattr(dialog, "exec", None)
    if execute is None:
        execute = dialog.exec_
    execute()
    return dialog.clickedButton() is accept_button


def confirm_clean_start(palette, descriptions):
    escaped_palette = html.escape(palette, quote=False)
    escaped_descriptions = "<br>".join(
        html.escape(description, quote=False) for description in descriptions
    )
    return _ask(
        "Clean Start?",
        "<b><i>Delete All {} Description(s)</i></b><br>"
        "from the "
        "<b><i>'{}'?</i></b><br><br>"
        "<b><i>Generation Bases</i></b> &amp; <b><i>Guide Curves</i></b><br>"
        "will <b><i>NOT</i></b> be <b><i>Deleted.</i></b><br><br>"
        "{}<br><br><b><i>Continue?</i></b>".format(
            len(descriptions), escaped_palette, escaped_descriptions
        ),
        "Yes",
        "No",
    )


def confirm_description_replacement(descriptions):
    escaped_descriptions = "<br>".join(
        html.escape(description, quote=False) for description in descriptions
    )
    return _ask(
        "Replace Existing XGen Descriptions?",
        "This will <b><i>Replace {} Existing Description(s)</i>"
        "</b>,<br>including their <b><i>Settings &amp; Bindings</i></b>:<br><br>"
        "{}<br><br><b><i>Continue?</i></b>".format(
            len(descriptions), escaped_descriptions
        ),
        "Replace",
        "Cancel",
    )


def confirm_template_overwrite(output_path):
    return _ask(
        "Overwrite Template?",
        template_overwrite_text(output_path),
        "Overwrite",
        "Cancel",
    )


def template_overwrite_text(output_path):
    relative_path = os.path.relpath(output_path, project_root()).replace("\\", "/")
    return (
        "<div style='text-align: left;'>"
        "A file already exists at:<br>{}"
        "</div>"
        "<div style='text-align: center; margin-top: 8px;'>"
        "Overwrite it with selected description?"
        "</div>"
    ).format(html.escape(relative_path, quote=True))
