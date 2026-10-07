import colorsys
from maya import OpenMayaUI as omui
from PySide6 import QtWidgets
from shiboken6 import wrapInstance


# ------------ PYSIDE6 WINDOW WRAPPER ------------


def get_main_window() -> QtWidgets.QWidget:
    ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QtWidgets.QWidget)


# ------------ COLOR CONVERSION FUNCTIONS ------------

def hex_to_rgb(value):
    value = value.lstrip('#')
    rgb_255 = tuple(int(value[i:i+2], 16) for i in (0, 2, 4))

    return tuple(v / 255.0 for v in rgb_255)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )

def shifted_background_color(rgb_color):
    # Unpack each separate variable (Hue, Saturation, Value)
    h, s, v = colorsys.rgb_to_hsv(*rgb_color)

    # Define the factor by which we're making th BG color darker/brighter based on the picked color value
    factor = 0.5 if v > 0.5 else 1.5

    return tuple(
        max(min(c * factor, 1.0), 0.075) if factor > 1 else max(c * factor, 0.0)
        for c in rgb_color
    )