import maya.cmds as cmds 

## IK SINGLE CONTROLLER MIRROR ##

'''
IK Single Mirror: IK Single controller mirror
(Select animated controller then target controller)
'''
def ik_single():
    sel = cmds.ls(sl=True)
    
    keyTransData = cmds.copyKey(sel[0], at = 'translate', o = 'keys')
    
            
    if keyTransData:
        pasteKeyData = cmds.pasteKey(sel[1])
        scaleKeyTrxX = cmds.scaleKey(sel[1], at = 'translateX', valueScale = -1)
        
    keyRotData = cmds.copyKey(sel[0], at = 'rotate', o = 'keys')
            
    if keyRotData:
        pasteKeyData = cmds.pasteKey(sel[1])
        scaleKeyRotX = cmds.scaleKey(sel[1], at = 'rotateY', valueScale = -1)
        scaleKeyRotX = cmds.scaleKey(sel[1], at = 'rotateZ', valueScale = -1)
