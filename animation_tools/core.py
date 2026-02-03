import maya.cmds as cmds
import json
from pathlib import Path

######## DEFAULT CONTROLLER SETTINGS ########

DEFAULT_CONTROLLER_DATA = {
    "controllers": {
        "HeadTop_End_ctl": {"radius": 0.0, "color": 17, "lineWidth": -1.0},
        "Head_ctl": {"radius": 10.0, "color": 17, "lineWidth": -1.0},
        "Hips_ctl": {"radius": 25.0, "color": 14, "lineWidth": 3.0},

        "LeftArm_ctl": {"radius": 9.0, "color": 18, "lineWidth": -1.0},
        "LeftForeArm_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},
        "LeftHand_ctl": {"radius": 6.0, "color": 18, "lineWidth": -1.0},

        "LeftHandThumb1_ctl": {"radius": 3.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandIndex1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandMiddle1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandRing1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandPinky1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftShoulder_ctl": {"radius": 10.0, "color": 18, "lineWidth": 3.0},
        "LeftUpLeg_ctl": {"radius": 15.0, "color": 18, "lineWidth": 2.0},
        "LeftLeg_ctl": {"radius": 12.0, "color": 18, "lineWidth": -1.0},
        "LeftFoot_ctl": {"radius": 10.0, "color": 18, "lineWidth": -1.0},
        "LeftToeBase_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},
        "LeftToe_End_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},

        "Spine_ctl": {"radius": 13.0, "color": 17, "lineWidth": -1.0},
        "Spine1_ctl": {"radius": 15.0, "color": 17, "lineWidth": -1.0},
        "Spine2_ctl": {"radius": 19.0, "color": 17, "lineWidth": -1.0},
        "Neck_ctl": {"radius": 12.0, "color": 17, "lineWidth": -1.0},

        "RightArm_ctl": {"radius": 9.0, "color": 20, "lineWidth": -1.0},
        "RightForeArm_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0},
        "RightHand_ctl": {"radius": 6.0, "color": 20, "lineWidth": -1.0},

        "RightHandThumb1_ctl": {"radius": 3.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandIndex1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandMiddle1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandRing1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandPinky1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightShoulder_ctl": {"radius": 10.0, "color": 20, "lineWidth": 3.0},
        "RightUpLeg_ctl": {"radius": 15.0, "color": 20, "lineWidth": 2.0},
        "RightLeg_ctl": {"radius": 12.0, "color": 20, "lineWidth": -1.0},
        "RightFoot_ctl": {"radius": 10.0, "color": 20, "lineWidth": -1.0},
        "RightToeBase_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0},
        "RightToe_End_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0}
    }
}

######## SAVING ########

def set_controllers_to_default(*args):
    saved_controllers = DEFAULT_CONTROLLER_DATA.get("controllers", {})

    for ctl, settings in saved_controllers.items():
        if not cmds.objExists(ctl):
            print(f"[DEFAULT] Missing controller: {ctl}")
            continue

        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        if make_circle and settings["radius"] is not None:
            cmds.setAttr(make_circle[0] + ".radius", settings["radius"])

        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", settings["color"])
        cmds.setAttr(shape + ".lineWidth", settings["lineWidth"])


def save_controller_layout(*args):
    file_path = cmds.fileDialog2(
        fileFilter="JSON (*.json)",
        caption="Save Controller Layout",
        dialogStyle=2,
        fileMode=0
    )
    if not file_path:
        return
    file_path = file_path[0]

    controller_data = {"controllers": {}}

    controllers = cmds.ls("*_ctl")

    for ctl in controllers:
        # GET SHAPE
        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        # FIND CONSTRUCTION NODE (where radius lives)
        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        radius = None
        if make_circle:
            radius = cmds.getAttr(make_circle[0] + ".radius")

        # GET COLOR + WIDTH FROM SHAPE
        color = cmds.getAttr(shape + ".overrideColor")
        line_width = cmds.getAttr(shape + ".lineWidth")

        # Save to JSON structure
        controller_data["controllers"][ctl] = {
            "radius": radius,
            "color": color,
            "lineWidth": line_width
        }

    with open(file_path, "w") as f:
        json.dump(controller_data, f, indent=4)

    cmds.inViewMessage(amg="Controller layout <hl>saved</hl>.", pos="topCenter", fade=True)
    
######## IMPORTING ########
    
def load_controller_layout(*args):
    file_path = cmds.fileDialog2(
        fileFilter="JSON (*.json)",
        caption="Load Controller Layout",
        dialogStyle=2,
        fileMode=1
    )
    if not file_path:
        return
    file_path = file_path[0]

    with open(file_path, "r") as f:
        data = json.load(f)

    saved_controllers = data["controllers"]

    for ctl, settings in saved_controllers.items():
        if not cmds.objExists(ctl):
            print(f"[WARNING] Controller not found: {ctl} — skipping")
            continue

        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        # FIND makeNurbCircle node to set radius
        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        if settings["radius"] is not None and make_circle:
            cmds.setAttr(make_circle[0] + ".radius", settings["radius"])

        # Restore color
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", settings["color"])

        # Restore lineWidth
        cmds.setAttr(shape + ".lineWidth", settings["lineWidth"])

    cmds.inViewMessage(amg="Controller layout <hl>loaded</hl>.", pos="topCenter", fade=True)

    

######## RADIUS OPTIONS ########

def get_entered_number(*args):
    return cmds.intField("radiusValue", query=True, value=True)


def singleSelectRadius(*args): 
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    selShapeHistory = cmds.listHistory(selShape)
    editableCurveNode = cmds.ls(selShapeHistory, type = 'makeNurbCircle')
    
    radiusNumber = get_entered_number()
    for i in editableCurveNode:
        get_entered_number()
        cmds.setAttr(i + '.radius', radiusNumber)

def allChildrenRadius(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True)
    selShapeHistory = cmds.listHistory(selShape)
    editableCurveNode = cmds.ls(selShapeHistory, type = 'makeNurbCircle')
    
    radiusNumber = get_entered_number()
    for i in editableCurveNode:
        get_entered_number()
        cmds.setAttr(i + '.radius', radiusNumber)



####### COLOR OPTIONS ########


def get_slider_number(*args):
    return cmds.intField("colorValue", query=True, value=True)
    
def singleSelectColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    colorNumber = get_slider_number()
    for i in selShape:
        get_slider_number()
        cmds.setAttr(i + '.overrideColor', colorNumber)

def allChildrenColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    colorNumber = get_slider_number()
    for i in selShape:
        get_slider_number()
        cmds.setAttr(i + '.overrideColor', colorNumber)

maya_index_colors = {
    0: (0.0, 0.0, 0.1),
    1: (0.0, 0.0, 0.0),
    2: (0.3, 0.3, 0.3),
    3: (0.5, 0.5, 0.5),
    4: (0.5, 0.0, 0.0),
    5: (0.0, 0.0, 0.2),
    6: (0.0, 0.0, 1.0),
    7: (0.0, 0.2, 0.0),
    8: (0.1, 0.0, 0.2),
    9: (1.0, 0.0, 1.0),
    10: (0.5, 0.2, 0.0),
    11: (0.2, 0.1, 0.0),
    12: (0.7, 0.2, 0.0),
    13: (1.0, 0.0, 0.0),
    14: (0.0, 1.0, 0.0),
    15: (0.0, 0.2, 0.7),
    16: (1.0, 1.0, 1.0),
    17: (1.0, 1.0, 0.0),
    18: (0.0, 1.0, 1.0),
    19: (0.0, 1.0, 0.5),
    20: (1.0, 0.7, 0.7),
    21: (0.9, 0.7, 0.5),
    22: (1.0, 1.0, 0.5),
    23: (0.0, 0.6, 0.3),
    24: (0.6, 0.4, 0.2),
    25: (0.6, 0.6, 0.2),
    26: (0.4, 0.6, 0.2),
    27: (0.2, 0.6, 0.4),
    28: (0.2, 0.6, 0.6),
    29: (0.2, 0.4, 0.6),
}
        
def set_color_value(val, *args): 
    cmds.intField("colorValue", edit = True, value = val, minValue=0, maxValue=31, ed = False)
    if val in maya_index_colors:
        cmds.intField("colorValue", edit = True, bgc = maya_index_colors[val])
    

####### LINE WIDTH OPTIONS ########

def get_width_number(*args):
    return cmds.intField("widthValue", query=True, value=True)
    
def singleSelectWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    widthNumber = get_width_number()
    for i in selShape:
        get_width_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)

def allChildrenWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    widthNumber = get_slider_number()
    for i in selShape:
        get_slider_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)

####### CONTROLLER BUILDER & ANIMATION KEYFRAME COPYING ########

def fk_controller_builder(*args):
    sel = cmds.ls(selection=True)
    if not sel:
        cmds.error("Select a root joint.")

    obj_list = cmds.listRelatives(sel[0], ad=True, typ='joint')
    obj_list.append(sel[0])  
    obj_list.reverse()       

    joint_ctl_map = {}

    for joint in obj_list:
        
        jntOX = cmds.getAttr(joint + '.jointOrientX')
        jntOY = cmds.getAttr(joint + '.jointOrientY')
        jntOZ = cmds.getAttr(joint + '.jointOrientZ')
        
        
        ctl = cmds.circle(n=joint + '_ctl', r=10, nr=[0, 1, 0])
        ctlshape = cmds.listRelatives(ctl[0], c=True, typ='shape')
        if ctlshape:
            cmds.setAttr(ctlshape[0] + '.overrideEnabled', 1)
            cmds.setAttr(ctlshape[0] + '.overrideColor', 17)

        ctl_grp = cmds.group(ctl, n=joint + '_animOffset')
        
        correction_grp = cmds.group(ctl_grp, n=joint + '_correctionOffset')

        cmds.matchTransform(correction_grp, joint, pos = True, rot = False)
        
        cmds.setAttr(correction_grp + '.rotateX', jntOX)
        cmds.setAttr(correction_grp + '.rotateY', jntOY)
        cmds.setAttr(correction_grp + '.rotateZ', jntOZ)

        parent_joint = cmds.listRelatives(joint, parent=True, type='joint')

        if parent_joint:
            parent_joint = parent_joint[0]
            if parent_joint in joint_ctl_map:
                cmds.parent(correction_grp, joint_ctl_map[parent_joint])

        joint_ctl_map[joint] = ctl[0]
        
        keyTransData = cmds.copyKey(joint, at = 'translate', o = 'keys')
        
        if keyTransData:
            pasteKeyData = cmds.pasteKey(correction_grp)
            
        keyRotData = cmds.copyKey(joint, at = 'rotate', o = 'keys')
        
        if keyRotData:
            pasteKeyData = cmds.pasteKey(ctl_grp)
            
        cmds.setAttr(correction_grp + '.rotateX', jntOX)
        cmds.setAttr(correction_grp + '.rotateY', jntOY)
        cmds.setAttr(correction_grp + '.rotateZ', jntOZ)
        
        cmds.setAttr(ctl_grp + '.translate', lock = True)
        cmds.setAttr(ctl_grp + '.rotate', lock = True)
        cmds.setAttr(ctl_grp + '.scale', lock = True)
        cmds.setAttr(ctl_grp + '.visibility', lock = True)
        
        cmds.setAttr(correction_grp + '.translate', lock = True)
        cmds.setAttr(correction_grp + '.rotate', lock = True)
        cmds.setAttr(correction_grp + '.scale', lock = True)
        cmds.setAttr(correction_grp + '.visibility', lock = True)
        
        cmds.lockNode(ctl)
        cmds.lockNode(ctl_grp)
        cmds.lockNode(correction_grp)
        
        
        cmds.cutKey(joint, cl = True)
        
        cmds.parentConstraint(ctl, joint, mo = True)
        
    set_controllers_to_default()

######## LOADING DEFAULT CONTROLLERS ########

def load_default_cons():
    # Get a list of all top items in the hierarchy
    outliner_top_nodes = cmds.ls(assemblies=True)
    # Define the one item name we're looking for (Mixamo's rig root is Hips joint)
    root_controller = "Hips"
    # If the Hips joint is found, select it, build FK controllers, and load default controllers JSON file
    if root_controller in outliner_top_nodes:
        cmds.select("Hips")
        fk_controller_builder()
    else:
        print("No Hips joint found. Do you have a Mixamo rig loaded?")
