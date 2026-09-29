import maya.cmds as cmds

def blendFKIKjointsNodeSetup():

    sel = cmds.ls(sl = True)
    switchAttr = cmds.listAttr(sel[0], ud = True)

    jntTrxBlend = cmds.shadingNode('blendColors', n = sel[3] + 'Translate_BlendColors', au = True )
    jntRotBlend = cmds.shadingNode('blendColors', n = sel[3] + 'Rotate_BlendColors', au = True )

    cmds.connectAttr(sel[0] + '.' + switchAttr[0], jntTrxBlend + '.blender', f = True)
    cmds.connectAttr(sel[0] + '.' + switchAttr[0], jntRotBlend + '.blender', f = True)

    cmds.connectAttr(sel[1] + '.translate', jntTrxBlend + '.color1', f = True)
    cmds.connectAttr(sel[2] + '.translate', jntTrxBlend + '.color2', f = True)

    cmds.connectAttr(sel[1] + '.rotate', jntRotBlend + '.color1', f = True)
    cmds.connectAttr(sel[2] + '.rotate', jntRotBlend + '.color2', f = True)

    cmds.connectAttr(jntTrxBlend + '.output', sel[3] + '.translate', f = True)
    cmds.connectAttr(jntRotBlend + '.output', sel[3] + '.rotate', f = True)