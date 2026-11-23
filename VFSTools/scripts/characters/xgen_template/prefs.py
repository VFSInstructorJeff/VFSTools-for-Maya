"""Saved preferences (Maya optionVars) for the X-Gen Template Tool."""

import maya.cmds as cmds


def read_option_var_string(name, default=""):
    if not cmds.optionVar(exists=name):
        return default
    value = cmds.optionVar(query=name)
    return default if value is None else value


def write_option_var_string(name, value):
    cmds.optionVar(stringValue=(name, value))
