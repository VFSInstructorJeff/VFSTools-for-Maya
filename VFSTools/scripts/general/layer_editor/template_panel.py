# ------------ IMPORT LIBRARIES/MODULES ------------
from maya import cmds

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                               QMenu, QMessageBox, QFrame)

from general.layer_editor.template_layer_widget import TemplateLayerWidget
from general.layer_editor.utils import rgb_to_hex
from general.layer_editor.constants import TEMPLATE_LAYER_LABEL, UNSAVED_CHANGES

# (label in the Overrides list, template field, tooltip)
OVERRIDE_OPTIONS = [
    ("Color", "color_rgb", "Layer color"),
    ("Layer Name", "layer_name", "Rename every layer to Name_01, Name_02, ... (needs a name in the TEMPLATE row)"),
    ("Visibility", "visibility", "Layer visibility"),
    ("Layer Mode", "display_type", "Normal / Template / Reference"),
    ("Export Path", "export_path", "Export folder"),
    ("RGBm Export Path", "legc_export_path", "RGB Mask export folder"),
    ("Move To Origin", "use_origin", "'Move to origin' on export"),
    ("RGB Mask", "legc_on_export", "Run the RGB Mask pass on export"),
]

MODE_NAMES = ["Normal", "Template", "Reference"]

OVERRIDES_TOOLTIP = (
    "After clicking Apply, the TEMPLATE Layer OVERRIDES every checked setting on ALL layers, "
    "including layers that already exist.\n\n"
    "If nothing is checked, Apply only saves the template: it will only affect layers created "
    "afterwards, and existing layers are left untouched."
)

# ------------ MENU THAT STAYS OPEN WHILE TICKING ITEMS ------------

class StayOpenMenu(QMenu):
    def mouseReleaseEvent(self, event):
        action = self.actionAt(event.position().toPoint())
        if action is not None and action.isEnabled() and not action.isSeparator() \
                and (action.isCheckable() or action.property("keepOpen")):
            action.trigger()    # Toggles checkable actions
            return              # ...without closing the menu
        super().mouseReleaseEvent(event)


# ------------ TEMPLATE PANEL ------------
# Pinned above the layer list: the "TEMPLATE LAYER" header row (Overrides + Apply) and the TEMPLATE row.

class TemplatePanel(QWidget):

    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.template = manager.template

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(2)

        # ---- HEADER ROW ----
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(4, 0, 4, 0)

        self.title_label = QLabel(TEMPLATE_LAYER_LABEL)
        font = self.title_label.font()
        font.setBold(True)
        self.title_label.setFont(font)

        self.unsaved_icon = QLabel()
        self.unsaved_icon.setPixmap(QIcon(UNSAVED_CHANGES).pixmap(16, 16))
        self.unsaved_icon.setToolTip("Unapplied changes. Click Apply to save the template.")
        self.unsaved_icon.setVisible(False)

        self.overrides_button = QPushButton("Overrides")
        self.overrides_button.setToolTip(OVERRIDES_TOOLTIP)
        self._build_overrides_menu()

        self.apply_button = QPushButton("Apply")
        self.apply_button.setFixedWidth(60)
        self.apply_button.setToolTip("Save the template. Checked Overrides are applied to ALL layers.")
        self.apply_button.clicked.connect(self.on_apply)

        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.unsaved_icon)
        header_layout.addStretch()
        header_layout.addWidget(self.overrides_button)
        header_layout.addWidget(self.apply_button)

        # ---- TEMPLATE ROW ----
        self.row = TemplateLayerWidget(self.template)
        self.row.value_set.connect(self.on_value_set)
        self.row.reset_requested.connect(self.on_reset)

        # ---- SEPARATOR ----
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("color: rgba(255, 255, 255, 40);")

        main_layout.addWidget(header)
        main_layout.addWidget(self.row)
        main_layout.addWidget(separator)

    # ------------ OVERRIDES MENU ------------

    def _build_overrides_menu(self):
        self.menu = StayOpenMenu(self)
        self.menu.setToolTipsVisible(True)

        for text, handler in (("All", self._check_all), ("None", self._check_none)):
            action = self.menu.addAction(text)
            action.setProperty("keepOpen", True)
            action.triggered.connect(handler)
        self.menu.addSeparator()

        self.override_actions = {}      # template field -> checkable QAction
        for label, field_name, tip in OVERRIDE_OPTIONS:
            action = QAction(label, self.menu)
            action.setCheckable(True)
            action.setToolTip(tip)
            action.toggled.connect(self._update_overrides_text)
            self.menu.addAction(action)
            self.override_actions[field_name] = action

        self.overrides_button.setMenu(self.menu)

    def _checked_fields(self):
        return [name for _, name, _ in OVERRIDE_OPTIONS if self.override_actions[name].isChecked()]

    def _set_all_checks(self, checked):
        for action in self.override_actions.values():
            action.setChecked(checked)

    def _check_all(self):
        self._set_all_checks(True)

    def _check_none(self):
        self._set_all_checks(False)

    def _update_overrides_text(self, *_):
        count = len(self._checked_fields())
        self.overrides_button.setText(f"Overrides ({count})" if count else "Overrides")

    # ------------ DRAFT TRACKING ------------

    def update_dirty(self):
        self.unsaved_icon.setVisible(self.template.is_dirty)

    def on_value_set(self, name, value):
        self.template.set_draft(name, value)
        self.update_dirty()

    def on_reset(self):
        # Staged like every other edit: nothing changes for layers until Apply is clicked
        self.template.clear_draft()
        self.row.refresh()
        self.update_dirty()

    def refresh(self):
        """Re-read the template (scene changed)."""
        self._set_all_checks(False)
        self.row.refresh()
        self.update_dirty()

    # ------------ APPLY ------------

    def _describe(self, name):
        value = self.template.get(name)
        if name == "color_rgb":
            return rgb_to_hex(value)
        if name == "visibility":
            return "Visible" if value else "Hidden"
        if name == "display_type":
            return MODE_NAMES[value]
        if name in ("use_origin", "legc_on_export"):
            return "On" if value else "Off"
        if name == "layer_name":
            return f"{value}_01, {value}_02, ..."
        return value if value else "(empty - clears the path)"

    def _labels(self):
        return {name: label for label, name, _ in OVERRIDE_OPTIONS}

    def _confirm_overrides(self, fields, layer_count):
        labels = self._labels()
        lines = "\n".join(f"\u2022 {labels[name]}  \u2192  {self._describe(name)}" for name in fields)

        box = QMessageBox(self)
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle("Apply Template Overrides")
        box.setText(f"This will OVERRIDE these settings on ALL {layer_count} existing layer(s):")
        box.setInformativeText(lines)
        apply_btn = box.addButton("Apply", QMessageBox.AcceptRole)
        box.addButton("Cancel", QMessageBox.RejectRole)
        box.setDefaultButton(box.buttons()[-1])    # Cancel is the safe default
        box.exec()
        return box.clickedButton() is apply_btn

    def on_apply(self):
        checked = self._checked_fields()
        layer_count = len(self.manager.layers)

        # A Layer Name override with no name set has nothing to apply
        skipped_name = "layer_name" in checked and not str(self.template.get("layer_name")).strip()
        fields = [name for name in checked if not (name == "layer_name" and skipped_name)]

        # Only ask when existing layers are about to be changed
        if fields and layer_count and not self._confirm_overrides(fields, layer_count):
            return

        # Checking an override and applying it counts as setting that value, so new layers copy it too
        for name in fields:
            self.template.mark_set(name)
        self.template.commit()
        self.manager.save_template()

        if fields and layer_count:
            self.manager.apply_overrides(fields)

        self._set_all_checks(False)     # Overrides are one-shot, so they can't be applied by accident next time
        self.update_dirty()

        message = "Template <hl>saved</hl>."
        if fields and layer_count:
            message = f"Template saved and applied to <hl>{layer_count}</hl> layer(s)."
        if skipped_name:
            message += " Layer Name was empty, so layers were not renamed."
        cmds.inViewMessage(amg=message, pos="topCenter", fade=True)
