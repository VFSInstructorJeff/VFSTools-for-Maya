import maya.cmds as cmds 

## FK ALL CHILDREN CONTROLLER MIRROR ##

'''
FK Children Mirror: FK All children controller mirror
(Select animated controller then target controller)
[!!!] ONLY WORKS IF CONTROLLER HIERARCHY IS PERFECT MIRROR
'''

def fk_child():
    sel = cmds.ls(sl=True)
    
    selControllersHier = cmds.listRelatives(sel[0], ad=True, type='transform')
    selControllersHier.reverse()
    
    destControllersHier = cmds.listRelatives(sel[1], ad=True, type='transform')
    destControllersHier.reverse()
    
    selControllers = [sel[0]] + selControllersHier
    destControllers = [sel[1]] + destControllersHier
    
    cmds.copyKey(selControllers, hi='none')
    
    cmds.pasteKey(destControllers, option='replace')