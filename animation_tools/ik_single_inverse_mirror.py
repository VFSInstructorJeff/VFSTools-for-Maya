###########- IK SINGLE INVERSE MIRROR -###########
    
import maya.cmds as cmds 

sel = cmds.ls(sl=True)

selControllers = [sel[0]]
destControllers = [sel[1]]

attrs = ['translate', 'rotate', 'scale']

for selC, destC in zip(selControllers, destControllers):
    
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
            #cmds.pasteKey(selC, at=attr, option='merge', to = totalFrames)
            #cmds.pasteKey(selC, at=attr, option='merge', to = beginningOffset)
            cmds.pasteKey(destC, at=attr, option='replaceCompletely', to = keyMidOffset)
            cmds.pasteKey(destC, at=attr, option='merge', to = pastedBeginningOffset)
            cmds.pasteKey(destC, at=attr, option='merge', to = pastedEndingOffset)
        else:
            print("No attribute to copy paste keys from")
            
    scaleKeyTrxX = cmds.scaleKey(sel[1], at = 'translateX', valueScale = -1)
    
    scaleKeyRotX = cmds.scaleKey(sel[1], at = 'rotateY', valueScale = -1)
    scaleKeyRotZ = cmds.scaleKey(sel[1], at = 'rotateZ', valueScale = -1)