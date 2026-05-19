from dataclasses import dataclass, asdict

@dataclass
class VFSLayerData:    
    
    # Setup all data relevant to VFS layer
    uuid: str
    maya_layer_name: str

    visibility: bool = True
    display_type: int = 0
    color_rgb: tuple = (1.0, 1.0, 1.0)

    select_sm: bool = False
    select_ucx: bool = False

    export_mode: str = "Single File"
    use_origin: bool = True
    export_path: str = ""

    def to_dict(self):

        # asdict() is specific to @dataclass
        data = asdict(self)
        data["color_rgb"] = list(self.color_rgb)

        return data

    @classmethod
    def from_dict(cls, data):
        data["color_rgb"] = tuple(
            data.get("color_rgb", [1, 1, 1])
        )

        return cls(**data)