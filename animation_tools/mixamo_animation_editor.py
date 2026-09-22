import maya.cmds as cmds

if cmds.namespace(exists='mixamorig'):
    cmds.namespace(moveNamespace=('mixamorig', ':'), force=True)
    cmds.namespace(removeNamespace='mixamorig')

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

####### CONTROLLER BUILDER & ANIMATION KEYFRAME COPYING ########

def fk_controller_builder():
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

