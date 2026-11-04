# ------------ IMPORT LIBRARIES/MODULES ------------
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QColorDialog, QFileDialog

from general.layer_editor.layer_data import VFSLayerData
from general.layer_editor.layer_widget import LayerWidget, LAYER_MODES
from general.layer_editor.utils import hex_to_rgb
from general.layer_editor.constants import VISIBLE, HIDDEN, TEMPLATE_LAYER_UUID

# ------------ TEMPLATE LAYER ROW ------------
# Looks like a normal layer row, but it is NOT tied to any Maya layer node.
# It only edits the TEMPLATE's *draft*: nothing is saved or applied until the user presses Apply
# (see TemplatePanel).

class TemplateLayerWidget(LayerWidget):

    value_set = Signal(str, object)     # The user changed a setting: field name, new value
    reset_requested = Signal()          # The user asked to clear the template (still needs Apply)

    def __init__(self, template):
        data = VFSLayerData(uuid=TEMPLATE_LAYER_UUID, maya_layer_name="")
        template.fill_display(data)
        super().__init__(data)

        self.template = template
        self._loading = False
        self._customize_ui()

    # ------------ UI TWEAKS ------------

    def _customize_ui(self):
        self.setToolTip("Settings new layers start with.\n"
                        "Changes only take effect after clicking Apply.")

        # The name field holds the base name for layers: Name_01, Name_02, ...
        self.name_edit.setReadOnly(False)
        self.name_edit.setText(self.template.get("layer_name"))
        self.name_edit.setPlaceholderText("Layer name")
        self.name_edit.setToolTip("Base name for layers: Name_01, Name_02, ...\n"
                                  "Leave empty to keep Maya's default layer names.")
        self.name_edit.setStyleSheet("QLineEdit { border: none; background: rgba(255, 255, 255, 10); }")

        # Nothing to export
        self.export_button.setVisible(False)

        self.color_button.setToolTip("Color layers start with")
        self.visibility_button.setToolTip("Visibility layers start with")
        self.mode_button.setToolTip("Layer mode layers start with: Normal / Template / Reference")
        self.export_toggle.setToolTip("Toggle export settings")
        self.path_button.setToolTip("Export folder layers start with")
        self.origin_checkbox.setToolTip("Layers start with 'move to origin' enabled")
        self.legc_checkbox.setToolTip("Layers start with 'run RGB Mask on export' enabled.\n"
                                      "Also switches between the regular and the RGBm export folder.")

    # ------------ REFRESH ------------

    def refresh(self):
        """Re-read everything from the template draft (after Reset, or after a scene change)."""
        self._loading = True
        try:
            self.data = VFSLayerData(uuid=TEMPLATE_LAYER_UUID, maya_layer_name="")
            self.template.fill_display(self.data)
            d = self.data

            self.name_edit.setText(self.template.get("layer_name"))
            self.name_edit.setCursorPosition(0)
            self.visibility_button.setChecked(not d.visibility)
            self.visibility_button.setIcon(QIcon(VISIBLE) if d.visibility else QIcon(HIDDEN))
            self.mode_button.setText(LAYER_MODES[d.display_type])
            self.origin_checkbox.setChecked(d.use_origin)
            self.legc_checkbox.setChecked(d.legc_on_export)
            self.path_edit.setText(d.export_path)
            self.legc_path_edit.setText(d.legc_export_path)
            if d.export_path or d.legc_export_path or d.legc_on_export:
                self.export_toggle.setChecked(True)
            self.apply_color_styles()
            self._refresh_path_view()
        finally:
            self._loading = False

    def _emit_value(self, name, value):
        if not self._loading:
            self.value_set.emit(name, value)

    # ------------ OVERRIDES: edit the draft only, never touch Maya ------------

    def finish_rename(self):
        self.name_edit.setCursorPosition(0)
        self._emit_value("layer_name", self.name_edit.text().strip())

    def on_visibility_changed(self, hidden):
        self.data.visibility = not hidden
        self.visibility_button.setIcon(QIcon(HIDDEN) if hidden else QIcon(VISIBLE))
        self._emit_value("visibility", self.data.visibility)

    def cycle_layer_mode(self):
        next_mode = (self.data.display_type + 1) % len(LAYER_MODES)
        self.data.display_type = next_mode
        self.mode_button.setText(LAYER_MODES[next_mode])
        self._emit_value("display_type", next_mode)

    def on_origin_changed(self, checked):
        self.data.use_origin = checked
        self._emit_value("use_origin", checked)

    def on_legc_toggled(self, checked):
        self.data.legc_on_export = checked
        self._refresh_path_view()
        self._emit_value("legc_on_export", checked)

    def pick_color(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return
        rgb = hex_to_rgb(color.name())
        self.data.color_rgb = rgb
        self.apply_color_styles()
        self._emit_value("color_rgb", rgb)

    def pick_export_path(self):
        is_legc = self._should_run_legc()
        current_path = self.data.legc_export_path if is_legc else self.data.export_path

        path = QFileDialog.getExistingDirectory(
            self,
            "Select Template RGBm Export Folder" if is_legc else "Select Template Export Folder",
            current_path or ""
        )
        if not path:
            return
        if is_legc:
            self.data.legc_export_path = path
            self.legc_path_edit.setText(path)
            self._emit_value("legc_export_path", path)
        else:
            self.data.export_path = path
            self.path_edit.setText(path)
            self._emit_value("export_path", path)

    def start_rename(self):
        pass  # The name field is always editable

    def export_layer(self):
        pass  # Nothing to export

    def eventFilter(self, obj, event):
        return False  # No double-click rename, no selection

    # ------------ CONTEXT MENU / MOUSE ------------

    def show_context_menu(self, pos):
        menu = QMenu(self)
        title = menu.addAction("Template Layer")
        title.setEnabled(False)
        menu.addSeparator()
        menu.addAction("Reset Template", self.reset_requested.emit)
        menu.exec(pos)

    def mousePressEvent(self, event):
        # Never selectable (so it can't be deleted/moved from the toolbar); right click only opens the menu
        if event.button() == Qt.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())

    def mouseMoveEvent(self, event):
        pass  # No drag
