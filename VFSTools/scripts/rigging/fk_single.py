import maya.cmds as cmds 

'''
FK Single Mirror: FK Single controller mirror
(Select animated controller then target controller)
'''

def fk_single():
    sel = cmds.ls(sl=True)

    keyTransData = cmds.copyKey(sel[0], at = 'translate', o = 'keys')
        
    if keyTransData:
        pasteKeyData = cmds.pasteKey(sel[1])
                    
    keyRotData = cmds.copyKey(sel[0], at = 'rotate', o = 'keys')
        
    if keyRotData:
        pasteKeyData = cmds.pasteKey(sel[1])
