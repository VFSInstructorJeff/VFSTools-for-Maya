# ------------ IMPORT LIBRARIES/MODULES ------------
from pathlib import Path

from maya import cmds

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMessageBox

# ------------ BATCH EXPORT (Export Selected / Export All) ------------
# Checks every layer's export paths up front (asking the user what to do about problems), exports the
# layers one after another without interrupting, then shows ONE summary with whatever went wrong.

MAX_LISTED = 12     # Longest list shown in a dialog before it says "... and N more"


def _bullets(lines):
    shown = [f"    \u2022 {line}" for line in lines[:MAX_LISTED]]
    if len(lines) > MAX_LISTED:
        shown.append(f"    ... and {len(lines) - MAX_LISTED} more")
    return "\n".join(shown)


def _folder_problem(path):
    """None if the folder is usable, otherwise a short reason."""
    if not path:
        return "no path set"
    if not Path(path).exists():
        return "folder does not exist"
    return None


# ------------ DIALOGS (kept separate so they are easy to reword) ------------

def _ask_missing_export_paths(parent, problems, valid_count):
    """Part 1: layers without a usable export path. Returns True to export only the layers that have one."""
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Warning)
    box.setWindowTitle("Missing Export Paths")
    box.setText("Some layers don't have a valid export path, so they can't be exported:")
    box.setInformativeText(
        _bullets([f"{name}  ({reason})" for name, reason in problems]) +
        ("" if valid_count else "\n\nNone of the layers can be exported. Set their export paths first.")
    )

    export_btn = None
    if valid_count:
        export_btn = box.addButton(f"Export Only Layers With Paths ({valid_count})", QMessageBox.AcceptRole)
    cancel_btn = box.addButton("Cancel" if valid_count else "Close", QMessageBox.RejectRole)
    box.setDefaultButton(cancel_btn)
    box.exec()
    return export_btn is not None and box.clickedButton() is export_btn


def _ask_missing_rgbm_paths(parent, problems):
    """Part 2: layers with RGBm turned on but no usable RGBm path.
    Returns "use_regular_path", "skip", or None (cancel)."""
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Warning)
    box.setWindowTitle("Missing RGBm Export Paths")
    box.setText("These layers have RGBm turned on, but no valid RGBm export path:")
    box.setInformativeText(
        _bullets([f"{name}  ({reason})" for name, reason in problems]) +
        "\n\nUse Regular Export Path: the RGBm file is saved next to the regular FBX. "
        "(The layer's own RGBm path is not changed.)"
        "\nSkip RGBm: these layers are exported without the RGBm file."
    )
    regular_btn = box.addButton("Use Regular Export Path", QMessageBox.AcceptRole)
    skip_btn = box.addButton("Skip RGBm For These Layers", QMessageBox.DestructiveRole)
    cancel_btn = box.addButton("Cancel", QMessageBox.RejectRole)
    box.setDefaultButton(cancel_btn)
    box.exec()

    clicked = box.clickedButton()
    if clicked is regular_btn:
        return "use_regular_path"
    if clicked is skip_btn:
        return "skip"
    return None


def _show_summary(parent, exported, total, not_exported, failures, warnings):
    """One dialog at the end. `failures` / `warnings` are lists of (layer, title, message)."""
    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Warning if failures else QMessageBox.Information)
    box.setWindowTitle("Export Finished")
    box.setText(f"Exported {exported} of {total} layer(s).")

    parts = []
    if failures:
        parts.append("Failed:\n" + _bullets([f"{layer}: {message.splitlines()[0]}" for layer, _, message in failures]))
    if not_exported:
        parts.append("Not exported (no valid export path):\n" + _bullets(not_exported))
    if warnings:
        parts.append("Finished with warnings:\n" + _bullets([f"{layer}: {title}" for layer, title, _ in warnings]))
    box.setInformativeText("\n\n".join(parts))

    # Full messages (long mesh lists, Maya errors) go in the expandable details
    details = [f"[{layer}] {title}\n{message}" for layer, title, message in failures + warnings]
    if details:
        box.setDetailedText("\n\n".join(details))
    box.addButton("OK", QMessageBox.AcceptRole)
    box.exec()


# ------------ MAIN ENTRY POINT ------------

def run_batch_export(parent, entries):
    """Export the given layer entries ({"data": ..., "widget": ...}), top to bottom."""
    if not entries:
        cmds.inViewMessage(amg="There are no layers to export.", pos="topCenter", fade=True)
        return

    # ---- Part 1: regular export paths ----
    valid, problems = [], []
    for entry in entries:
        reason = _folder_problem(entry["data"].export_path)
        if reason:
            problems.append((entry["data"].maya_layer_name, reason))
        else:
            valid.append(entry)

    if problems:
        if not _ask_missing_export_paths(parent, problems, len(valid)):
            return      # Cancelled (or nothing exportable): nothing is exported

    not_exported = [f"{name}  ({reason})" for name, reason in problems]

    # ---- Part 2: RGBm export paths (only for layers that are still going to be exported) ----
    rgbm_problems = []
    for entry in valid:
        if entry["widget"]._should_run_legc():
            reason = _folder_problem(entry["data"].legc_export_path)
            if reason:
                rgbm_problems.append((entry, reason))

    legc_modes = {}
    if rgbm_problems:
        choice = _ask_missing_rgbm_paths(parent, [(e["data"].maya_layer_name, r) for e, r in rgbm_problems])
        if choice is None:
            return      # Cancelled: nothing is exported
        for entry, _ in rgbm_problems:
            legc_modes[entry["data"].uuid] = choice

    # ---- Export ----
    exported = 0
    failures, warnings = [], []

    QApplication.setOverrideCursor(Qt.WaitCursor)
    try:
        for entry in valid:
            layer_report = []
            try:
                ok = entry["widget"].export_layer_batch(layer_report, legc_modes.get(entry["data"].uuid))
            except Exception as error:      # One broken layer must not stop the others
                ok = False
                layer_report.append({
                    "layer": entry["data"].maya_layer_name,
                    "title": "Unexpected error",
                    "message": str(error) or error.__class__.__name__,
                    "fatal": True,
                })

            if ok:
                exported += 1
            for item in layer_report:
                target = failures if item["fatal"] else warnings
                target.append((item["layer"], item["title"], item["message"]))
    finally:
        QApplication.restoreOverrideCursor()

    # ---- Summary ----
    if not failures and not warnings and not not_exported:
        cmds.inViewMessage(amg=f"{exported} layer(s) exported <hl>successfully</hl>.", pos="topCenter", fade=True)
    else:
        _show_summary(parent, exported, len(entries), not_exported, failures, warnings)
