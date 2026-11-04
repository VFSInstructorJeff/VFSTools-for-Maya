# ------------ IMPORTING MODULES ------------

from dataclasses import dataclass, asdict, fields, field
from typing import ClassVar

# ------------ SETUP DATA CLASS ------------
# Using data class for cleaner code (automatically handles __init__ and self.var = var assignments)
@dataclass
class VFSLayerData:    
    
    # ------------ INITIALIZE VALUES ------------
    uuid: str
    maya_layer_name: str

    visibility: bool = True
    display_type: int = 0
    color_rgb: tuple = (1.0, 1.0, 1.0)

    select_sm: bool = False
    select_ucx: bool = False

    use_origin: bool = False
    export_path: str = ""
    legc_export_path: str = ""
    legc_on_export: bool = False    # Run the RGB Mask (LEGC) pass when this layer is exported (stored, no longer resets after export)
    legc_applied: bool = False      # The RGB Mask pass has already been run on this layer (Undo button visible)

    # ------------ FUNCTIONS ------------

    # Write all data to a dictionary to store it neatly
    def to_dict(self):
        # asdict() is specific to @dataclass, it converts an instance of dataclass to a dictionary format
        data = asdict(self)
        # Make the color_rgb parameter a list instead of a tuple since JSON doesn't support tuples
        data["color_rgb"] = list(self.color_rgb)

        return data

    # @classmethod means it's a method that is bound to the class instead of the instances
    # Using this to have an alternative constructor/a factory method that uses data from somewhere else (the dictionary saved to the .ma file)
    @classmethod
    def from_dict(cls, data):
        # Make the color_rbg parameters a tuple again
        data["color_rgb"] = tuple(
            data.get("color_rgb", [1, 1, 1])
        )

        # Strip any keys that no longer exist on the dataclass
        # This handles backwards compatibility when fields are removed
        valid_fields = {f.name for f in fields(cls)}
        data = {k: v for k, v in data.items() if k in valid_fields} # k = key, v = value

        # **data is unpacking a dictionary
        # cls(**data) is calling the class (making an instance) and passing the unpacked dictionary data as the parameters
        return cls(**data)


# ------------ TEMPLATE LAYER ------------
# Not a layer. It stores the settings new layers should start with, and the settings the user can push onto ALL layers.
#
#   draft   -> what the user is currently editing in the TEMPLATE row (staged, not used by anything yet)
#   applied -> what was last confirmed with the Apply button (saved in the scene, used for new layers)
#
# Only settings the user explicitly set are stored. Anything missing falls back to the normal presets when a layer is created.
@dataclass
class LayerTemplate:

    # Every setting the template can hold, with the value the TEMPLATE row displays while it hasn't been set
    FIELDS: ClassVar[dict] = {
        "layer_name": "",
        "visibility": True,
        "display_type": 0,
        "color_rgb": (1.0, 1.0, 1.0),
        "use_origin": False,
        "export_path": "",
        "legc_export_path": "",
        "legc_on_export": False,
    }

    applied: dict = field(default_factory=dict)
    draft: dict = field(default_factory=dict)

    @staticmethod
    def _normalize(name, value):
        return tuple(value) if name == "color_rgb" else value

    # ---- draft (staged edits) ----

    def set_draft(self, name, value):
        if name in self.FIELDS:
            self.draft[name] = self._normalize(name, value)

    def get(self, name):
        """The value the TEMPLATE row shows: the staged value if the user set one, else the default."""
        return self.draft.get(name, self.FIELDS[name])

    def mark_set(self, name):
        """Count a setting as explicitly set (used when an override is applied without the user touching it)."""
        self.draft.setdefault(name, self.FIELDS[name])

    def clear_draft(self):
        self.draft.clear()

    @property
    def is_dirty(self):
        return self.draft != self.applied

    def fill_display(self, data):
        """Copy the staged values onto a VFSLayerData so the TEMPLATE row can display them."""
        for name in self.FIELDS:
            if name != "layer_name":
                setattr(data, name, self.get(name))

    # ---- applied (committed) ----

    def commit(self):
        self.applied = dict(self.draft)

    def apply_to(self, data):
        """Copy every applied setting onto a new layer's VFSLayerData. Returns the field names copied.
        (layer_name is handled when the Maya layer is created, not here.)"""
        copied = []
        for name, value in self.applied.items():
            if name == "layer_name":
                continue
            setattr(data, name, value)
            copied.append(name)
        return copied

    # ---- saving ----

    def to_dict(self):
        out = dict(self.applied)
        if "color_rgb" in out:
            out["color_rgb"] = list(out["color_rgb"])  # JSON has no tuples
        return out

    def load_dict(self, raw):
        self.applied = {}
        for name, value in (raw or {}).items():
            if name in self.FIELDS:
                self.applied[name] = self._normalize(name, value)
        self.draft = dict(self.applied)
