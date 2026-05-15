import json

from maya import cmds

from layer_editor_tools.layer_data import VFSLayerData
from layer_editor_tools.layer_widget import LayerWidget


class LayerManager:

    FILE_INFO_KEY = "VFSLayers"

    def __init__(self):

        self.layers = []

    # --------------------------------
    # Create
    # --------------------------------

    def create_layer(
        self,
        empty=True,
        name="Layer"
    ):

        maya_layer = cmds.createDisplayLayer(
            e=empty,
            n=name,
            mc=True
        )

        uuid = cmds.ls(
            maya_layer,
            uuid=True
        )[0]

        data = VFSLayerData(
            uuid=uuid,
            maya_layer_name=maya_layer
        )

        widget = LayerWidget(data)

        widget.deleted.connect(
            self.remove_layer
        )

        entry = {
            "data": data,
            "widget": widget
        }

        self.layers.append(entry)

        return widget

    # --------------------------------
    # Remove
    # --------------------------------

    def remove_layer(self, widget):

        entry = next(
            (
                x for x in self.layers
                if x["widget"] == widget
            ),
            None
        )

        if not entry:
            return

        layer_name = entry["data"].maya_layer_name

        if cmds.objExists(layer_name):
            cmds.delete(layer_name)

        widget.setParent(None)

        widget.deleteLater()

        self.layers.remove(entry)

    # --------------------------------
    # Save
    # --------------------------------

    def save(self):

        payload = [
            x["data"].to_dict()
            for x in self.layers
        ]

        cmds.fileInfo(
            self.FILE_INFO_KEY,
            json.dumps(payload)
        )

    # --------------------------------
    # Load
    # --------------------------------

    def load(self):

        raw = cmds.fileInfo(
            self.FILE_INFO_KEY,
            q=True
        )

        if not raw:
            return []

        try:

            payload = json.loads(raw[0])

        except json.JSONDecodeError:

            return []

        widgets = []

        for item in payload:

            data = VFSLayerData.from_dict(item)

            widget = LayerWidget(data)

            widget.deleted.connect(
                self.remove_layer
            )

            entry = {
                "data": data,
                "widget": widget
            }

            self.layers.append(entry)

            widgets.append(widget)

        return widgets