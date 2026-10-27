import maya.cmds as cmds

def fk_controller_deconstructor():
    
    controllers = cmds.ls("*_ctl", type="transform")
    
    for ctl in controllers:
        
        if not cmds.objExists(ctl):
            continue
        
        cmds.lockNode(ctl, lock=False)
        
        
        cmds.setAttr(ctl + '.translate', lock = False)
        cmds.setAttr(ctl + '.rotate', lock = False)
        cmds.setAttr(ctl + '.scale', lock = False)
        cmds.setAttr(ctl + '.visibility', lock = False)
        
        joint = ctl.replace("_ctl", "")
        
        if not cmds.objExists(joint):
            continue
        
        anim_grp = joint + "_animOffset"
        
        cmds.lockNode(anim_grp, lock=False)
        
        cmds.setAttr(anim_grp + '.translate', lock=False)
        cmds.setAttr(anim_grp + '.rotate', lock=False)
        cmds.setAttr(anim_grp + '.scale', lock=False)
        cmds.setAttr(anim_grp + '.visibility', lock=False)
            
            
        correction_grp = joint + "_correctionOffset"
        
        cmds.lockNode(correction_grp, lock=False)
        
        cmds.setAttr(correction_grp + '.translate', lock=False)
        cmds.setAttr(correction_grp + '.rotate', lock=False)
        cmds.setAttr(correction_grp + '.scale', lock=False)
        cmds.setAttr(correction_grp + '.visibility', lock=False)
            
        constraints = cmds.listConnections(joint, type="parentConstraint")
        if constraints:
            cmds.delete(constraints)
        
        keyTransData = cmds.copyKey(correction_grp, at = 'translate', o = 'keys')
        
        if keyTransData:
            pasteKeyData = cmds.pasteKey(joint)
            
        keyRotData = cmds.copyKey(anim_grp, at = 'rotate', o = 'keys')
        
        if keyRotData:
            pasteKeyData = cmds.pasteKey(joint)
        
    
    all_joints = cmds.ls(type="joint")    

    root_joints = []

    for jnt in all_joints:
        parent = cmds.listRelatives(jnt, parent=True)

        if not parent or cmds.nodeType(parent[0]) != "joint":
            root_joints.append(jnt)

    
    root_joint = root_joints[0]
    correction_root = root_joint + "_correctionOffset"

    
    cmds.delete(correction_root)
    
    
    cmds.inViewMessage(
        amg="Controllers <hl>removed</hl> and animation restored to joints.",
        pos="topCenter",
        fade=True
    )

