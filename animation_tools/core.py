from maya import cmds

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



#######


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

#######

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

#######

def fk_controller_builder(*args):
    # Get selected root joint #
    sel = cmds.ls(selection=True)
    if not sel:
        cmds.error("Select a root joint.")

    # Get all joints in hierarchy (top-down)
    obj_list = cmds.listRelatives(sel[0], ad=True, typ='joint')
    obj_list.append(sel[0])  # Add root joint
    obj_list.reverse()       # To process from root to leaf

    # Dictionary to store which controller belongs to which joint
    joint_ctl_map = {}

    for joint in obj_list:
        
        jntOX = cmds.getAttr(joint + '.jointOrientX')
        jntOY = cmds.getAttr(joint + '.jointOrientY')
        jntOZ = cmds.getAttr(joint + '.jointOrientZ')
        
        
        # Create controller
        ctl = cmds.circle(n=joint + '_ctl', r=10, nr=[0, 1, 0])
        ctlshape = cmds.listRelatives(ctl[0], c=True, typ='shape')
        if ctlshape:
            cmds.setAttr(ctlshape[0] + '.overrideEnabled', 1)
            cmds.setAttr(ctlshape[0] + '.overrideColor', 17)

        # Create group for animation offset
        ctl_grp = cmds.group(ctl, n=joint + '_animOffset')
        
        correction_grp = cmds.group(ctl_grp, n=joint + '_correctionOffset')

        # Match group to joint
        cmds.matchTransform(correction_grp, joint, pos = True, rot = False)
        
        cmds.setAttr(correction_grp + '.rotateX', jntOX)
        cmds.setAttr(correction_grp + '.rotateY', jntOY)
        cmds.setAttr(correction_grp + '.rotateZ', jntOZ)

        # Find the parent joint
        parent_joint = cmds.listRelatives(joint, parent=True, type='joint')

        if parent_joint:
            parent_joint = parent_joint[0]
            # Parent this controller group under the parent joint's controller (not group)
            if parent_joint in joint_ctl_map:
                cmds.parent(correction_grp, joint_ctl_map[parent_joint])

        # Store the controller for this joint
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
        
        # Delete joint keyframes 
        
        cmds.cutKey(joint, cl = True)
        
        cmds.parentConstraint(ctl, joint, mo = True)


