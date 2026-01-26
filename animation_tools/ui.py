from animation_tools import core as anim_tools_core
from maya import cmds
######## WINDOW & UI ########

def mixamo_anim_editor():
    
    winName = "mixamoEditorWindow"
    
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName, window=True)
        print('Deleted old Mixamo Editor UI')

    window = cmds.window(winName, title="VFS Mixamo Animation Editor", iconName='MAE', widthHeight=(350, 500) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.text( label='Select HIPS joint', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    cmds.button( label='Build FK Controllers', command = anim_tools_core.fk_controller_builder, w = 200)
    cmds.text( label='Controller Settings', align='center', fn = 'boldLabelFont', w = 20, h = 30)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Radius', align='left', w = 100 )
    cmds.intField("radiusValue", value=10, minValue=0, maxValue=100) 
    cmds.button(label="Selected", command = anim_tools_core.singleSelectRadius, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenRadius, w = 70, bgc=[0.3, 0.8, 0.7])

    cmds.setParent( '..' )

    cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Color', align='left', w = 100 )
    cmds.intField("colorValue", value=17, minValue=0, maxValue=31, ed = False, bgc = [1.0, 1.0, 0.0]) 
    cmds.button(label="Selected", command = anim_tools_core.singleSelectColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 11)
    
    cmds.button(label='', w = 30, bgc=[0.0, 0.0, 0.1], command=lambda x: anim_tools_core.set_color_value(0))
    cmds.button(label='', w = 30, bgc=[0.0, 0.0, 0.0], command=lambda x: anim_tools_core.set_color_value(1))
    cmds.button(label='', w = 30, bgc=[0.3, 0.3, 0.3], command=lambda x: anim_tools_core.set_color_value(2))
    cmds.button(label='', w = 30, bgc=[0.5, 0.5, 0.5], command=lambda x: anim_tools_core.set_color_value(3))
    cmds.button(label='', w = 30, bgc=[0.5, 0.0, 0.0], command=lambda x: anim_tools_core.set_color_value(4))
    cmds.button(label='', w = 30, bgc=[0.0, 0.0, 0.2], command=lambda x: anim_tools_core.set_color_value(5))
    cmds.button(label='', w = 30, bgc=[0.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_color_value(6))
    cmds.button(label='', w = 30, bgc=[0.0, 0.2, 0.0], command=lambda x: anim_tools_core.set_color_value(7))
    cmds.button(label='', w = 30, bgc=[0.1, 0.0, 0.2], command=lambda x: anim_tools_core.set_color_value(8))
    cmds.button(label='', w = 30, bgc=[1.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_color_value(9))
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 11)
    
    cmds.button(label='', w = 30, bgc=[0.5, 0.2, 0.0], command=lambda x: anim_tools_core.set_color_value(10))
    cmds.button(label='', w = 30, bgc=[0.2, 0.1, 0.0], command=lambda x: anim_tools_core.set_color_value(11))
    cmds.button(label='', w = 30, bgc=[0.7, 0.2, 0.0], command=lambda x: anim_tools_core.set_color_value(12))
    cmds.button(label='', w = 30, bgc=[1.0, 0.0, 0.0], command=lambda x: anim_tools_core.set_color_value(13))
    cmds.button(label='', w = 30, bgc=[0.0, 1.0, 0.0], command=lambda x: anim_tools_core.set_color_value(14))
    cmds.button(label='', w = 30, bgc=[0.0, 0.2, 0.7], command=lambda x: anim_tools_core.set_color_value(15))
    cmds.button(label='', w = 30, bgc=[1.0, 1.0, 1.0], command=lambda x: anim_tools_core.set_color_value(16))
    cmds.button(label='', w = 30, bgc=[1.0, 1.0, 0.0], command=lambda x: anim_tools_core.set_color_value(17))
    cmds.button(label='', w = 30, bgc=[0.0, 1.0, 1.0], command=lambda x: anim_tools_core.set_color_value(18))
    cmds.button(label='', w = 30, bgc=[0.0, 1.0, 0.5], command=lambda x: anim_tools_core.set_color_value(19))
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 11)
    
    cmds.button(label='', w = 30, bgc=[1.0, 0.7, 0.7], command=lambda x: anim_tools_core.set_color_value(20))
    cmds.button(label='', w = 30, bgc=[0.9, 0.7, 0.5], command=lambda x: anim_tools_core.set_color_value(21))
    cmds.button(label='', w = 30, bgc=[1.0, 1.0, 0.5], command=lambda x: anim_tools_core.set_color_value(22))
    cmds.button(label='', w = 30, bgc=[0.0, 0.6, 0.3], command=lambda x: anim_tools_core.set_color_value(23))
    cmds.button(label='', w = 30, bgc=[0.6, 0.4, 0.2], command=lambda x: anim_tools_core.set_color_value(24))
    cmds.button(label='', w = 30, bgc=[0.6, 0.6, 0.2], command=lambda x: anim_tools_core.set_color_value(25))
    cmds.button(label='', w = 30, bgc=[0.4, 0.6, 0.2], command=lambda x: anim_tools_core.set_color_value(26))
    cmds.button(label='', w = 30, bgc=[0.2, 0.6, 0.4], command=lambda x: anim_tools_core.set_color_value(27))
    cmds.button(label='', w = 30, bgc=[0.2, 0.6, 0.6], command=lambda x: anim_tools_core.set_color_value(28))
    cmds.button(label='', w = 30, bgc=[0.2, 0.4, 0.6], command=lambda x: anim_tools_core.set_color_value(29))
    
    
    ###

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
        
    
    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Line Thickness', align='left', w = 100 )
    cmds.intField("widthValue", value=-1, minValue=-1, maxValue=10) 
    cmds.button(label="Selected", command = anim_tools_core.singleSelectWidth, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenWidth, w = 70, bgc=[0.3, 0.8, 0.7])

    
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.button(label="Save CTLS", w=170, bgc=[0.5, 0.5, 0.5], command=anim_tools_core.save_controller_layout)
    cmds.button(label="Load CTLS", w=170, bgc=[0.6, 0.6, 0.6], command=anim_tools_core.load_controller_layout)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=1)
    
    cmds.text(label = 'VFS GD76 Roman Karoly', align = 'left', w = 150)
    

        
    cmds.showWindow( window )