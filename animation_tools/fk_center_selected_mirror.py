###########- CENTER CONTROLLER ANIMATION MIRROR -###########

import maya.cmds as cmds 
    
sel = cmds.ls(sl=True)


selControllers = [sel]


attrs = ['translate', 'rotate', 'scale']

for selC in selControllers:
    
    sourceKeyTime = cmds.keyframe(selC, query=True, timeChange=True)
    
    if not sourceKeyTime:
        print(selC + "has no keys")
        continue
    
    firstKey = min(sourceKeyTime)        
    lastKey = max(sourceKeyTime)        
    halfKeyRange = (firstKey+lastKey)/2
    keyMidOffset = lastKey - halfKeyRange
    totalFrames = lastKey - firstKey
    beginningOffset = (firstKey - firstKey) - totalFrames
    endingOffset = (firstKey - firstKey) + lastKey
    
    pastedBeginningOffset = keyMidOffset - totalFrames
    pastedEndingOffset = keyMidOffset + totalFrames

    for attr in attrs:

        copy = cmds.copyKey(selC, at=attr, option='keys')
        if copy > 0:
            cmds.pasteKey(selC, at=attr, option='merge', to = totalFrames)
        else:
            print("No attribute to copy paste keys from")
            
            
            
    scaleKeyTrxX = cmds.scaleKey(sel[0], time=(lastKey , None), at = 'translateX', valueScale = 1)
    scaleKeyTrxY = cmds.scaleKey(sel[0], time=(lastKey , None), at = 'translateY', valueScale = 1)
    scaleKeyTrxZ = cmds.scaleKey(sel[0], time=(lastKey , None), at = 'translateZ', valueScale = -1)
    
    scaleKeyRotX = cmds.scaleKey(selC, time=(totalFrames , None), at = 'rotateX', valueScale = -1)
    scaleKeyRotY = cmds.scaleKey(selC, time=(totalFrames , None), at = 'rotateY', valueScale = -1)
    scaleKeyRotZ = cmds.scaleKey(selC, time=(totalFrames , None), at = 'rotateZ', valueScale = 1)