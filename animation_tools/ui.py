from animation_tools import core as anim_tools_core
from maya import cmds

######## WINDOW & UI ########

def mixamo_anim_editor():
    
    winName = "Karoly Controlly Editor"
    
    if cmds.workspaceControl(winName, exists=True):
        cmds.deleteUI(winName)
        print('Deleted old Mixamo Editor UI')

    window = cmds.workspaceControl(winName, label = "Karoly Controlly Editor", fl = True, retain = False, ih = 800, w = 400, iw = 400, wp='fixed')
    cmds.columnLayout( adjustableColumn=True )
    #cmds.text( label='Select HIPS joint', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    #cmds.button( label='Build FK Controllers', command = fk_controller_builder, w = 200)
    cmds.text( label='Local Rotation Axis', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    
    #####
    
    cmds.rowLayout(numberOfColumns=5)
    
    cmds.separator(hr = False, h = 23, w = 50, vis = False)
    cmds.button(label="Show All", w = 70, bgc=[0.5, 0.5, 1], command=anim_tools_core.enableAllTransAxis)
    cmds.separator(hr = False, h = 23, w = 30, st = 'out')
    cmds.button(label="Show Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=anim_tools_core.selectedShowTransAxis)
    cmds.button(label="Show All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=anim_tools_core.allChildrenShowTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=5)
    
    cmds.separator(hr = False, h = 23, w = 50, vis = False)
    cmds.button(label="Hide All", w = 70, bgc=[0.5, 0.5, 1], command=anim_tools_core.disableAllTransAxis)
    cmds.separator(hr = False, h = 23, w = 30, st = 'out')
    cmds.button(label="Hide Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=anim_tools_core.selectedHideTransAxis)
    cmds.button(label="Hide All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=anim_tools_core.allChildrenHideTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='Outliner Settings', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    
    cmds.rowLayout(numberOfColumns=3)

    cmds.colorSliderGrp('outlinerColorValue', label='Outliner Color', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(100, 80, 72) )
    cmds.button(label="Selected", command = anim_tools_core.selectedChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.7])    
    
    

    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=5)
    
    cmds.text( label='Reset Colors', align='left', w = 100)
    cmds.button(label="Reset All", w = 79, bgc=[0.5, 0.5, 1], command=anim_tools_core.allSceneResetOutlinerColor)
    cmds.button(label="Undo Reset", w = 79, bgc=[0.5, 0.6, 1], command=anim_tools_core.allSceneUndoResetOutlinerColor)
    cmds.button(label="Selected", w = 70, bgc=[0.3, 0.8, 0.9], command=anim_tools_core.selectedResetOutlinerColor)
    cmds.button(label="All Children", w = 70, bgc=[0.3, 0.8, 0.7], command=anim_tools_core.allChildrenResetOutlinerColors)
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 108)
    
    cmds.button(label='', w = 35, bgc=[1.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_float_color_value(0))
    cmds.button(label='', w = 35, bgc=[1.0, 1.0, 0.0], command=lambda x: anim_tools_core.set_float_color_value(1))
    cmds.button(label='', w = 35, bgc=[0.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_float_color_value(2))
    cmds.button(label='', w = 35, bgc=[1.0, 0.0, 0.0], command=lambda x: anim_tools_core.set_float_color_value(3))
    cmds.button(label='', w = 35, bgc=[0.3, 0.3, 8.0], command=lambda x: anim_tools_core.set_float_color_value(4)) 
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 108)
    
    cmds.button(label='', w = 35, bgc=[0.0, 1.0, 0.0], command=lambda x: anim_tools_core.set_float_color_value(5))
    cmds.button(label='', w = 35, bgc=[0.4, 0.4, 0.1], command=lambda x: anim_tools_core.set_float_color_value(6))
    cmds.button(label='', w = 35, bgc=[0.0, 1.0, 1.0], command=lambda x: anim_tools_core.set_float_color_value(7))
    cmds.button(label='', w = 35, bgc=[2.4, 0.6, 0.6], command=lambda x: anim_tools_core.set_float_color_value(8))
    cmds.button(label='', w = 35, bgc=[0.78, 0.78, 0.78], command=lambda x: anim_tools_core.set_float_color_value(9)) 
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='Controller Creator', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    
    cmds.rowLayout(numberOfColumns=2, columnWidth=(1, 100))


    cmds.text( label='Controller Name', align='left', w = 100 )
    cmds.textField("controllerNameField", w = 200)
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 43, w = 82, vis = False)
    cmds.button(label="Create Controller", w = 100, bgc=[0.9, 0.4, 0.3], command=anim_tools_core.createJustController)
    cmds.button(label="ZO", w = 70, bgc=[0.9, 0.5, 0.3], command=anim_tools_core.createZeroOffsetController)
    cmds.button(label="MZO", w = 70, bgc=[0.9, 0.6, 0.3], command=anim_tools_core.createJustController)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='Controller Settings', align='center', fn = 'boldLabelFont', w = 20, h = 30)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Scale', align='left', w = 100 )
    cmds.floatField("scaleValue", value=1, minValue=0, maxValue=100, w=160, pre = 1) 
    cmds.button(label="Selected", command = anim_tools_core.singleSelectScale, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenScale, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####

    cmds.setParent( '..' )
    
    cmds.separator(st='none', h=10)

    cmds.rowLayout(numberOfColumns=4)

    cmds.text(label='Controller Shape', align='left', w=100)

    cmds.optionMenu("shapeMenu", w=160)


    cmds.menuItem(label='00 - Triangle', data = 0)
    cmds.menuItem(label='01 - Square', data = 1)
    cmds.menuItem(label='02 - Hexagon')
    cmds.menuItem(label='03 - Octagon')
    cmds.menuItem(label='04 - Circle')
    cmds.menuItem(label='05 - Half Circle')
    cmds.menuItem(label='06 - Pill')
    cmds.menuItem(label='07 - Circle Star')
    cmds.menuItem(label='08 - Star')
    cmds.menuItem(label='09 - Flower')
    cmds.menuItem(label='10 - Locator')
    cmds.menuItem(label='11 - Pyramid')
    cmds.menuItem(label='12 - Diamond')
    cmds.menuItem(label='13 - Cube')
    cmds.menuItem(label='14 - Sphere')
    cmds.menuItem(label='15 - Half Cylinder')
    cmds.menuItem(label='16 - Taco')
    cmds.menuItem(label='17 - Skinny Arrow')
    cmds.menuItem(label='18 - Fat Arrow')
    cmds.menuItem(label='19 - Double Arrow')
    cmds.menuItem(label='20 - Arrow 90')
    cmds.menuItem(label='21 - Arrow 180')
    cmds.menuItem(label='22 - Arrow 270')
    cmds.menuItem(label='23 - 3D Arrow')
    cmds.menuItem(label='24 - Skinny Circle Pin')
    cmds.menuItem(label='25 - Fat Circle Pin')
    cmds.menuItem(label='26 - Skinny Square Pin')
    cmds.menuItem(label='27 - Fat Square Pin')
    cmds.menuItem(label='28 - Locator Pin')
    cmds.menuItem(label='29 - Gear')

    cmds.button(label="Selected", command = anim_tools_core.singleSelectShape, w=70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenShape, w=70, bgc=[0.3, 0.8, 0.7])

    cmds.setParent('..')
    
    cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=9) 
    
    cmds.separator(st = 'none', w = 106)
    
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', command =  anim_tools_core.rotateXCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateXclockwise', command = anim_tools_core.rotateXClockwise)
    
    cmds.separator(hr = False, h = 18, w = 2, st = 'out')
    
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateYcounterclockwise', command =  anim_tools_core.rotateYCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateYclockwise', command =  anim_tools_core.rotateYClockwise)
    
    cmds.separator(hr = False, h = 18, w = 2, st = 'out')
    
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateZcounterclockwise', command =  anim_tools_core.rotateZCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateZclockwise',  command =  anim_tools_core.rotateZClockwise)

    cmds.setParent('..')
    
    #cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=9) 

    cmds.text( label='Controller Orient', align='left', w = 100 )
    cmds.text( label='X:', align='left', w = 10 )
    cmds.intField("XValue", value=0, w = 40)
    cmds.text( label='Y:', align='left', w = 10 )
    cmds.intField("YValue", value=0, w = 40)
    cmds.text( label='Z:', align='left', w = 10 )
    cmds.intField("ZValue", value=0, w = 40)
    cmds.button(label="Selected", command = anim_tools_core.singleSelectOrient, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenOrient, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####
    
    cmds.setParent( '..' )

    cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Controller Color', align='left', w = 100 )
    cmds.intField("colorValue", value=17, minValue=0, maxValue=31, ed = False, bgc = [1.0, 1.0, 0.0], w=160) 
    cmds.button(label="Selected", command = anim_tools_core.singleSelectColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = anim_tools_core.allChildrenColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 17)
    
    cmds.button(label='0', w = 35, bgc=[0.0, 0.0, 0.1], command=lambda x: anim_tools_core.set_color_value(0))
    cmds.button(label='1', w = 35, bgc=[0.0, 0.0, 0.0], command=lambda x: anim_tools_core.set_color_value(1))
    cmds.button(label='2', w = 35, bgc=[0.3, 0.3, 0.3], command=lambda x: anim_tools_core.set_color_value(2))
    cmds.button(label='3', w = 35, bgc=[0.5, 0.5, 0.5], command=lambda x: anim_tools_core.set_color_value(3))
    cmds.button(label='4', w = 35, bgc=[0.5, 0.0, 0.0], command=lambda x: anim_tools_core.set_color_value(4)) 
    cmds.button(label='5', w = 35, bgc=[0.0, 0.0, 0.2], command=lambda x: anim_tools_core.set_color_value(5))
    cmds.button(label='6', w = 35, bgc=[0.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_color_value(6))
    cmds.button(label='7', w = 35, bgc=[0.0, 0.2, 0.0], command=lambda x: anim_tools_core.set_color_value(7))
    cmds.button(label='8', w = 35, bgc=[0.1, 0.0, 0.2], command=lambda x: anim_tools_core.set_color_value(8))
    cmds.button(label='9', w = 35, bgc=[1.0, 0.0, 1.0], command=lambda x: anim_tools_core.set_color_value(9))
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 17)
    
    cmds.button(label='10', w = 35, bgc=[0.5, 0.2, 0.0], command=lambda x:  anim_tools_core.set_color_value(10))
    cmds.button(label='11', w = 35, bgc=[0.2, 0.1, 0.0], command=lambda x:  anim_tools_core.set_color_value(11))
    cmds.button(label='12', w = 35, bgc=[0.7, 0.2, 0.0], command=lambda x:  anim_tools_core.set_color_value(12))
    cmds.button(label='13', w = 35, bgc=[1.0, 0.0, 0.0], command=lambda x:  anim_tools_core.set_color_value(13))
    cmds.button(label='14', w = 35, bgc=[0.0, 1.0, 0.0], command=lambda x:  anim_tools_core.set_color_value(14))
    cmds.button(label='15', w = 35, bgc=[0.0, 0.2, 0.7], command=lambda x:  anim_tools_core.set_color_value(15))
    cmds.button(label='16', w = 35, bgc=[1.0, 1.0, 1.0], command=lambda x:  anim_tools_core.set_color_value(16))
    cmds.button(label='17', w = 35, bgc=[1.0, 1.0, 0.0], command=lambda x:  anim_tools_core.set_color_value(17))
    cmds.button(label='18', w = 35, bgc=[0.0, 1.0, 1.0], command=lambda x:  anim_tools_core.set_color_value(18))
    cmds.button(label='19', w = 35, bgc=[0.0, 1.0, 0.5], command=lambda x:  anim_tools_core.set_color_value(19))
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 17)
    
    cmds.button(label='20', w = 35, bgc=[1.0, 0.7, 0.7], command=lambda x:  anim_tools_core.set_color_value(20))
    cmds.button(label='21', w = 35, bgc=[0.9, 0.7, 0.5], command=lambda x:  anim_tools_core.set_color_value(21))
    cmds.button(label='22', w = 35, bgc=[1.0, 1.0, 0.5], command=lambda x:  anim_tools_core.set_color_value(22))
    cmds.button(label='23', w = 35, bgc=[0.0, 0.6, 0.3], command=lambda x:  anim_tools_core.set_color_value(23))
    cmds.button(label='24', w = 35, bgc=[0.6, 0.4, 0.2], command=lambda x:  anim_tools_core.set_color_value(24))
    cmds.button(label='25', w = 35, bgc=[0.6, 0.6, 0.2], command=lambda x:  anim_tools_core.set_color_value(25))
    cmds.button(label='26', w = 35, bgc=[0.4, 0.6, 0.2], command=lambda x:  anim_tools_core.set_color_value(26))
    cmds.button(label='27', w = 35, bgc=[0.2, 0.6, 0.4], command=lambda x:  anim_tools_core.set_color_value(27))
    cmds.button(label='28', w = 35, bgc=[0.2, 0.6, 0.6], command=lambda x:  anim_tools_core.set_color_value(28))
    cmds.button(label='29', w = 35, bgc=[0.2, 0.4, 0.6], command=lambda x:  anim_tools_core.set_color_value(29))
    
    
    ###

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)

    
    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Line Thickness', align='left', w = 100 )
    cmds.intField("widthValue", value=-1, minValue=-1, maxValue=10, w=160) 
    cmds.button(label="Selected", command =  anim_tools_core.singleSelectWidth, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command =  anim_tools_core.allChildrenWidth, w = 70, bgc=[0.3, 0.8, 0.7])

    
    
    #####
    
    #cmds.setParent( '..' )
    
    #cmds.separator(st = 'none', h = 10)
    
    #cmds.rowLayout(numberOfColumns=2)
    
    #cmds.button(label="Save CTLS", w=202, bgc=[0.5, 0.5, 0.5], command=save_controller_layout)
    #cmds.button(label="Load CTLS", w=202, bgc=[0.6, 0.6, 0.6], command=load_controller_layout)
    
    #####
    
    #cmds.setParent( '..' )
    
    #cmds.separator(st = 'none', h = 20)
    
    #cmds.rowLayout(numberOfColumns=1)
    
    #cmds.button(label="Delete CTLS", command=fk_controller_deconstructor, bgc=[0.50, 0, 0], w = 80, al = 'right')
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.text(label = 'VFS GD76 Roman Karoly', align = 'left', w = 150)
    
    
    #cmds.dockControl( area='left', content=window )

        
    #cmds.showWindow( window )

