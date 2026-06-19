# ------------ IMPORTING MODULES ------------

from dataclasses import dataclass, asdict, fields

# ------------ SETUP DATA CLASS ------------
# Using data class for cleaner code (automatically handles __init__ and self.var = var assignments)
@dataclass
class VFSLayerData:    
    
    # ------------ INITIALIZE VALUES ------------
    uuid: str
    maya_layer_name: str

    visibility: bool = True
    display_type: int = 0               # TODO: Make this a button, for now it's just a value in data and doesn't reflect on the UI
    color_rgb: tuple = (1.0, 1.0, 1.0)

    select_sm: bool = False
    select_ucx: bool = False

    use_origin: bool = True
    export_path: str = ""

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