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

    rgb_255 = tuple(
        int(value[i:i+2], 16)
        for i in (0, 2, 4))

    return tuple(v / 255.0 for v in rgb_255)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )

def shifted_background_color(rgb_color):
    hsv = colorsys.rgb_to_hsv(*rgb_color)

    shifted = []

    if hsv[2] > 0.5:
        for value in rgb_color:
            shifted.append(max(value * 0.5, 0))

    else:
        for value in rgb_color:
            if value <= 0:
                value = 0.075
            shifted.append(min(value * 1.5, 1))

    return tuple(shifted)