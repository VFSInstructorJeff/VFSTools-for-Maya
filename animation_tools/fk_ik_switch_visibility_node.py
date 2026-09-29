import maya.cmds as cmds

def visNodeSetup():

    sel = cmds.ls(sl = True)
    switchAttr = cmds.listAttr(sel[0], ud = True)

    visReverse = cmds.shadingNode('reverse', n = sel[0] + '_Visibility_Reverse', au = True)

    cmds.connectAttr(sel[0] + '.' + switchAttr[0], sel[1] + '.visibility', f = True)

    cmds.connectAttr(sel[0] + '.' + switchAttr[0], visReverse + '.inputX', f = True)
    cmds.connectAttr(visReverse + '.outputX', sel[2] + '.visibility', f = True)