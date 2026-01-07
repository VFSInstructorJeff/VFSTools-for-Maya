from animation_tools import core as animation_tools_core
from maya import cmds

def mixamo_anim_editor():

    window = cmds.window( title="VFS Mixamo Animation Editor", iconName='MAE', widthHeight=(350, 500) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.text( label='Select HIPS joint', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    cmds.button( label='Build FK Controllers', command = animation_tools_core.fk_controller_builder, w = 200)
    cmds.text( label='Controller Settings', align='center', fn = 'boldLabelFont', w = 20, h = 30)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Radius', align='left', w = 100 )
    cmds.intField("radiusValue", value=10, minValue=0, maxValue=100) 
    cmds.button(label="Selected", command = animation_tools_core.singleSelectRadius, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = animation_tools_core.allChildrenRadius, w = 70, bgc=[0.3, 0.8, 0.7])

    cmds.setParent( '..' )

    cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Color', align='left', w = 100 )
    cmds.intField("colorValue", value=17, minValue=0, maxValue=31) 
    cmds.button(label="Selected", command = animation_tools_core.singleSelectColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = animation_tools_core.allChildrenColor, w = 70, bgc=[0.3, 0.8, 0.7])

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
        
    
    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Line Thickness', align='left', w = 100 )
    cmds.intField("widthValue", value=-1, minValue=-1, maxValue=10) 
    cmds.button(label="Selected", command = animation_tools_core.singleSelectWidth, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = animation_tools_core.allChildrenWidth, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '6 =  ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(0, 0, 1) )
    
    #####

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '13 = ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(1, 0, 0) )
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '14 =  ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(0, 1, 0) )
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '17 =  ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(1, 1, 0) )

    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '18 =  ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(0.5, 0.9, 1) )
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = '20 =  ', align = 'left', w = 30)
    
    cmds.text( label='', align='left', w = 50, bgc=(1, 0.75, 0.75) )
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=1)
    
    cmds.text(label = 'VFS GD76 Roman Karoly', align = 'left', w = 150)
    

        
    cmds.showWindow( window )