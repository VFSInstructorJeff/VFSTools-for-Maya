import maya.cmds as cmds
import webbrowser

#######################################################
##################- SHAPE LIBRARY -####################
#######################################################


##########- FLAT SHAPES -##########
###################################

### 0 ###

trianglePoints = [(-0.0, -10.0, 10.0), (0.0, 10.0, 0.0), (-0.0, -10.0, -10.0), (-0.0, -10.0, 10.0)]


### 1 ###

squarePoints = [(0.0, 10.0, 10.0), (0.0, 10.0, -10.0), (-0.0, -10.0, -10.0), (-0.0, -10.0, 10.0), (0.0, 10.0, 10.0)]


### 2 ###

hexagonPoints = [(0.0, 5.0, -8.6603), (-0.0, -5.0, -8.6603), (-0.0, -10.0, 0.0), (-0.0, -5.0, 8.6603), (0.0, 5.0, 8.6603), (0.0, 10.0, 0.0), (0.0, 5.0, -8.6603)]


### 3 ###

octagonPoints = [(-0.0, 4.2095, -10.1627), (0.0, -4.2095, -10.1627), (-0.0, -10.1627, -4.2095), (-0.0, -10.1627, 4.2095), (0.0, -4.2095, 10.1627),
    (-0.0, 4.2095, 10.1627), (0.0, 10.1627, 4.2095), (0.0, 10.1627, -4.2095), (-0.0, 4.2095, -10.1627)
]


### 4 ###

circlePoints = [(0.0, -10.0, 0.0), (0.0, -9.8481, 1.7365), (-0.0, -9.3969, 3.4202), (0.0, -8.6603, 5.0), (0.0, -7.6604, 6.4279),
    (-0.0, -6.4279, 7.6604), (0.0, -5.0, 8.6603), (-0.0, -3.4202, 9.3969), (0.0, -1.7365, 9.8481), (0.0, 0.0, 10.0),
    (-0.0, 1.7365, 9.8481), (0.0, 3.4202, 9.3969), (0.0, 5.0, 8.6603), (0.0, 6.4279, 7.6604), (0.0, 7.6604, 6.4279),
    (-0.0, 8.6603, 5.0), (0.0, 9.3969, 3.4202), (-0.0, 9.8481, 1.7365), (0.0, 10.0, 0.0), (-0.0, 9.8481, -1.7365),
    (0.0, 9.3969, -3.4202), (0.0, 8.6602, -5.0), (0.0, 7.6604, -6.4279), (0.0, 6.4279, -7.6604), (0.0, 5.0, -8.6603),
    (0.0, 3.4202, -9.3969), (-0.0, 1.7365, -9.8481), (0.0, 0.0, -10.0), (0.0, -1.7365, -9.8481), (-0.0, -3.4202, -9.3969),
    (0.0, -5.0, -8.6602), (-0.0, -6.4279, -7.6604), (0.0, -7.6604, -6.4279), (0.0, -8.6603, -5.0), (-0.0, -9.3969, -3.4202),
    (0.0, -9.8481, -1.7365), (0.0, -10.0, 0.0)
]


### 5 ###

halfCirclePoints = [(-0.0, 0.0, 10.0), (-0.0, 1.7365, 9.8481), (-0.0, 3.4202, 9.3969), (0.0, 5.0, 8.6603), (0.0, 6.4279, 7.6604),
    (-0.0, 7.6604, 6.4279), (0.0, 8.6603, 5.0), (0.0, 9.3969, 3.4202), (-0.0, 9.8481, 1.7365), (0.0, 10.0, -0.0),
    (-0.0, 9.8481, -1.7365), (0.0, 9.3969, -3.4202), (0.0, 8.6603, -5.0), (-0.0, 7.6604, -6.4279), (0.0, 6.4279, -7.6604),
    (0.0, 5.0, -8.6603), (-0.0, 3.4202, -9.3969), (0.0, 1.7365, -9.8481), (0.0, -0.0, -10.0), (-0.0, 0.0, 10.0)
]


### 6 ###

pillPoints = [(-0.0, -10.0, -10.0), (0.0, -9.6593, -12.5882), (0.0, -8.6603, -15.0), (-0.0, -7.0711, -17.0711), (-0.0, -5.0, -18.6603),
    (0.0, -2.5882, -19.6593), (0.0, 0.0, -20.0), (-0.0, 2.5882, -19.6593), (0.0, 5.0, -18.6603), (0.0, 7.0711, -17.0711),
    (-0.0, 8.6603, -15.0), (-0.0, 9.6593, -12.5882), (0.0, 10.0, -10.0), (0.0, 10.0, 10.0), (-0.0, 9.6593, 12.5882),
    (-0.0, 8.6603, 15.0), (0.0, 7.0711, 17.0711), (0.0, 5.0, 18.6603), (-0.0, 2.5882, 19.6593), (0.0, 0.0, 20.0),
    (0.0, -2.5882, 19.6593), (-0.0, -5.0, 18.6603), (-0.0, -7.0711, 17.0711), (0.0, -8.6603, 15.0), (0.0, -9.6593, 12.5882),
    (-0.0, -10.0, 10.0), (-0.0, -10.0, -10.0)
]


### 7 ###

circleStarPoints = [(0.0, 0.0, 17.5), (0.0, -3.4202, 9.3969), (-0.0, -5.0, 8.6603), (0.0, -6.4279, 7.6604), (0.0, -7.6604, 6.4279),
    (0.0, -8.6603, 5.0), (0.0, -9.3969, 3.4202), (0.0, -17.5, 0.0), (0.0, -9.3969, -3.4202), (0.0, -8.6603, -5.0),
    (0.0, -7.6604, -6.4279), (0.0, -6.4279, -7.6604), (-0.0, -5.0, -8.6602), (0.0, -3.4202, -9.3969), (0.0, 0.0, -17.5),
    (0.0, 3.4202, -9.3969), (0.0, 5.0, -8.6603), (0.0, 6.4279, -7.6604), (-0.0, 7.6604, -6.4279), (-0.0, 8.6603, -5.0),
    (0.0, 9.3969, -3.4202), (0.0, 17.5, 0.0), (0.0, 9.3969, 3.4202), (-0.0, 8.6603, 5.0), (-0.0, 7.6604, 6.4279),
    (0.0, 6.4279, 7.6604), (0.0, 5.0, 8.6603), (0.0, 3.4202, 9.3969), (0.0, 0.0, 17.5)
]

### 8 ###

starPoints = [(0.0, 0.0, -17.5), (0.0, 5.0, -5.0), (0.0, 17.5, 0.0), (0.0, 5.0, 5.0), (0.0, 0.0, 17.5),
    (-0.0, -5.0, 5.0), (-0.0, -17.5, 0.0), (-0.0, -5.0, -5.0), (0.0, 0.0, -17.5)
]


### 9 ###

flowerPoints = [(-0.0, 31.3263, 0.0), (-0.0, 38.0477, 15.3592), (0.0, 32.3254, 25.2707), (0.0, 15.6632, 27.1294), (0.0, 5.7224, 40.6299),
    (-0.0, -5.7224, 40.6299), (-0.0, -15.6632, 27.1294), (-0.0, -32.3254, 25.2707), (0.0, -38.0477, 15.3592), (-0.0, -31.3264, 0.0),
    (0.0, -38.0477, -15.3592), (0.0, -32.3253, -25.2707), (-0.0, -15.6632, -27.1294), (-0.0, -5.7224, -40.6299), (0.0, 5.7224, -40.6299),
    (0.0, 15.6632, -27.1294), (0.0, 32.3254, -25.2707), (-0.0, 38.0477, -15.3592), (-0.0, 31.3263, 0.0)
]

###########- 3D SHAPES -###########
###################################

### 10 ###

locatorPoints = [( 0.0,  5.0,  0.0), ( 0.0, -5.0,  0.0), ( 0.0,  0.0,  0.0), ( 5.0,  0.0,  0.0), (-5.0,  0.0,  0.0), ( 0.0,  0.0,  0.0),
    ( 0.0,  0.0, -5.0), ( 0.0,  0.0,  5.0)
]


### 11 ###

pyramidPoints = [(-7.5, -0.0, 10.0), (7.5, 0.0, 0.0), (-7.5, -0.0, 10.0), (-7.5, 10.0, 0.0), (7.5, 0.0, 0.0),
    (-7.5, 10.0, 0.0), (-7.5, -0.0, -10.0), (7.5, 0.0, 0.0), (-7.5, -0.0, -10.0), (-7.5, -10.0, 0.0),
    (7.5, 0.0, 0.0), (-7.5, -10.0, 0.0), (-7.5, -0.0, 10.0)
]


### 12 ###

diamondPoints = [(15.0, -0.0, 0.0), (0.0, 0.0, 10.0), (0.0, 10.0, 0.0), (15.0, -0.0, 0.0), (0.0, 10.0, 0.0),
    (0.0, 0.0, -10.0), (15.0, -0.0, 0.0), (0.0, 0.0, -10.0), (-0.0, -10.0, 0.0), (15.0, -0.0, 0.0),
    (-0.0, -10.0, 0.0), (0.0, 0.0, 10.0), (-15.0, 0.0, 0.0), (-0.0, -10.0, 0.0), (0.0, 0.0, -10.0),
    (-15.0, 0.0, 0.0), (0.0, 10.0, 0.0)
]


### 13 ###

cubePoints = [(10.0, 10.0, 10.0), (10.0, -10.0, 10.0), (-10.0, -10.0, 10.0), (-10.0, 10.0, 10.0), (10.0, 10.0, 10.0), (10.0, 10.0, -10.0), (10.0, -10.0, -10.0), 
    (10.0, -10.0, 10.0), (10.0, 10.0, 10.0), (10.0, 10.0, -10.0), (-10.0, 10.0, -10.0), (-10.0, -10.0, -10.0), (10.0, -10.0, -10.0), (10.0, 10.0, -10.0), 
    (-10.0, 10.0, -10.0), (-10.0, 10.0, 10.0), (-10.0, -10.0, 10.0), (-10.0, -10.0, -10.0), (-10.0, 10.0, -10.0)
]


### 14 ###

spherePoints = [(10.0, 0.0, 0.0), (9.7493, 2.2252, 0.0), (9.0097, 4.3388, 0.0), (7.8183, 6.2349, 0.0), (6.2349, 7.8183, 0.0),
    (4.3388, 9.0097, 0.0), (2.2252, 9.7493, 0.0), (0.0, 10.0, 0.0), (-2.2252, 9.7493, 0.0), (-4.3388, 9.0097, 0.0),
    (-6.2349, 7.8183, 0.0), (-7.8183, 6.2349, 0.0), (-9.0097, 4.3388, 0.0), (-9.7493, 2.2252, 0.0), (-10.0, 0.0, 0.0),
    (-9.7493, -2.2252, 0.0), (-9.0097, -4.3388, 0.0), (-7.8183, -6.2349, 0.0), (-6.2349, -7.8183, 0.0), (-4.3388, -9.0097, 0.0),
    (-2.2252, -9.7493, 0.0), (0.0, -10.0, 0.0), (2.2252, -9.7493, 0.0), (4.3388, -9.0097, 0.0), (6.2349, -7.8183, 0.0),
    (7.8183, -6.2349, 0.0), (9.0097, -4.3388, 0.0), (9.7493, -2.2252, 0.0), (10.0, 0.0, 0.0), (9.8769, 0.0, 1.5643),
    (9.5106, 0.0, 3.0902), (8.9101, 0.0, 4.5399), (8.0902, 0.0, 5.8779), (7.0711, 0.0, 7.0711), (5.8779, 0.0, 8.0902),
    (4.5399, 0.0, 8.9101), (3.0902, 0.0, 9.5106), (1.5643, 0.0, 9.8769), (0.0, 0.0, 10.0), (-1.5643, 0.0, 9.8769),
    (-3.0902, 0.0, 9.5106), (-4.5399, 0.0, 8.9101), (-5.8779, 0.0, 8.0902), (-7.0711, 0.0, 7.0711), (-8.0902, 0.0, 5.8779),
    (-8.9101, 0.0, 4.5399), (-9.5106, 0.0, 3.0902), (-9.8769, 0.0, 1.5643), (-10.0, 0.0, 0.0), (-9.8769, 0.0, -1.5643),
    (-9.5106, 0.0, -3.0902), (-8.9101, 0.0, -4.5399), (-8.0902, 0.0, -5.8779), (-7.0711, 0.0, -7.0711), (-5.8779, 0.0, -8.0902),
    (-4.5399, 0.0, -8.9101), (-3.0902, 0.0, -9.5106), (-1.5643, 0.0, -9.8769), (0.0, 0.0, -10.0), (1.5643, 0.0, -9.8769),
    (3.0902, 0.0, -9.5106), (4.5399, 0.0, -8.9101), (5.8779, 0.0, -8.0902), (7.0711, 0.0, -7.0711), (8.0902, 0.0, -5.8779),
    (8.9101, 0.0, -4.5399), (9.5106, 0.0, -3.0902), (9.8769, 0.0, -1.5643), (10.0, 0.0, 0.0)
]


### 15 ###

halfCylinderPoints = [(-4.0, 0.0, 12.0), (4.0, -0.0, 12.0), (4.0, 2.0838, 11.8177), (4.0, 4.1042, 11.2763), (4.0, 6.0, 10.3923),
    (4.0, 7.7134, 9.1925), (4.0, 9.1925, 7.7135), (4.0, 10.3923, 6.0), (4.0, 11.2763, 4.1042), (4.0, 11.8177, 2.0838),
    (4.0, 12.0, 0.0), (4.0, 11.8177, -2.0838), (4.0, 11.2763, -4.1042), (4.0, 10.3923, -6.0), (4.0, 9.1925, -7.7134),
    (4.0, 7.7135, -9.1925), (4.0, 6.0, -10.3923), (4.0, 4.1042, -11.2763), (4.0, 2.0838, -11.8177), (4.0, -0.0, -12.0),
    (-4.0, 0.0, -12.0), (-4.0, 2.0838, -11.8177), (-4.0, 4.1042, -11.2763), (-4.0, 6.0, -10.3923), (-4.0, 7.7135, -9.1925),
    (-4.0, 9.1925, -7.7134), (-4.0, 10.3923, -6.0), (-4.0, 11.2763, -4.1042), (-4.0, 11.8177, -2.0838), (-4.0, 12.0, 0.0),
    (-4.0, 11.8177, 2.0838), (-4.0, 11.2763, 4.1042), (-4.0, 10.3923, 6.0), (-4.0, 9.1925, 7.7135), (-4.0, 7.7134, 9.1925),
    (-4.0, 6.0, 10.3923), (-4.0, 4.1042, 11.2763), (-4.0, 2.0838, 11.8177), (-4.0, 0.0, 12.0)
]

### 16 ###

tacoPoints = [(0.0, 0.0, 10.0), (1.5834, 0.5189, 9.6593), (2.8312, 1.8646, 8.6603), (3.5876, 3.5395, 7.0711), (3.9156, 5.0363, 5.0), (3.9982, 6.0256, 2.5882), 
    (4.0040, 6.3662, 0.0), (3.9982, 6.0256, -2.5882), (3.9156, 5.0363, -5.0), (3.5876, 3.5395, -7.0711), (2.8312, 1.8646, -8.6603), (1.5834, 0.5189, -9.6593), 
    (0.0, 0.0, -10.0), (-1.5834, 0.5189, -9.6593), (-2.8312, 1.8646, -8.6603), (-3.5876, 3.5395, -7.0711), (-3.9156, 5.0363, -5.0), (-3.9982, 6.0256, -2.5882), 
    (-4.0040, 6.3662, 0.0), (-3.9982, 6.0256, 2.5882), (-3.9156, 5.0363, 5.0), (-3.5876, 3.5395, 7.0711), (-2.8312, 1.8646, 8.6603), (-1.5834, 0.5189, 9.6593), 
    (0.0, 0.0, 10.0)
]


#########- ARROW SHAPES -##########
###################################

### 17 ###

skinnyArrowPoints = [(0.0, 0.0, 0.0), (25.0, 0.0, 0.0), (25.0, 0.0, 10.0), (40.0, 0.0, 0.0), (25.0, 0.0, -10.0), (25.0, 0.0, 0.0)]


### 18 ###

fatArrowPoints = [(0.0, 0.0, 5.0), (25.0, 0.0, 5.0), (25.0, 0.0, 10.0), (40.0, 0.0, 0.0), (25.0, 0.0, -10.0),
    (25.0, 0.0, -5.0), (0.0, 0.0, -5.0), (0.0, 0.0, 5.0)
]


### 19 ###

doubleSidedArrowPoints = [(25.0, 0.0, 0.0), (10.0, 0.0, -10.0), (10.0, 0.0, -5.0), (-10.0, 0.0, -5.0), (-10.0, 0.0, -10.0), (-25.0, 0.0, 0.0), (-10.0, 0.0, 10.0), 
    (-10.0, 0.0, 5.0), (10.0, 0.0, 5.0), (10.0, 0.0, 10.0), (25.0, 0.0, 0.0)
]


### 20 ###

arrow90DegreesPoints = [(-25.0, 0.0, -5.0), (-35.0, 0.0, 10.0), (-30.0, 0.0, 10.0), (-28.0667, 0.0, 14.3007), (-25.4840, 0.0, 18.5152), (-22.2739, 0.0, 22.2739), 
    (-18.5152, 0.0, 25.4840), (-14.3007, 0.0, 28.0667), (-10.0, 0.0, 30.0), (-10.0, 0.0, 35.0), (5.0, 0.0, 25.0), (-10.0, 0.0, 15.0), (-10.0, 0.0, 20.0), 
    (-13.0777, 0.0, 18.0), (-15.7325, 0.0, 15.7325), (-18.0, 0.0, 13.0777), (-20.0, 0.0, 10.0), (-15.0, 0.0, 10.0), (-25.0, 0.0, -5.0)
]

### 21 ###

arrow180DegreesPoints = [(-25.0, 0.0, -5.0), (-35.0, 0.0, 10.0), (-30.0, 0.0, 10.0), (-28.0667, 0.0, 14.3007), (-25.4840, 0.0, 18.5152), (-22.2739, 0.0, 22.2739), 
    (-18.5152, 0.0, 25.4840), (-14.3007, 0.0, 28.0667), (-9.7340, 0.0, 29.9583), (-4.9277, 0.0, 31.1122), (0.0, 0.0, 31.5), (4.9277, 0.0, 31.1122), 
    (9.7340, 0.0, 29.9583), (14.3007, 0.0, 28.0667), (18.5152, 0.0, 25.4840), (22.2739, 0.0, 22.2739), (25.4840, 0.0, 18.5152), (28.0667, 0.0, 14.3007), 
    (30.0, 0.0, 10.0), (35.0, 0.0, 10.0), (25.0, 0.0, -5.0), (15.0, 0.0, 10.0), (20.0, 0.0, 10.0), (18.0, 0.0, 13.0777), (15.7325, 0.0, 15.7325), 
    (13.0777, 0.0, 18.0), (10.1009, 0.0, 19.8241), (6.8753, 0.0, 21.1601), (3.4805, 0.0, 21.9751), (0.0, 0.0, 22.2491), (-3.4805, 0.0, 21.9751), 
    (-6.8753, 0.0, 21.1601), (-10.1009, 0.0, 19.8241), (-13.0777, 0.0, 18.0), (-15.7325, 0.0, 15.7325), (-18.0, 0.0, 13.0777), (-20.0, 0.0, 10.0), 
    (-15.0, 0.0, 10.0), (-25.0, 0.0, -5.0)
]


### 22 ###

arrow270DegreesPoints = [(-25.0, 0.0, -5.0), (-35.0, 0.0, 10.0), (-30.0, 0.0, 10.0), (-28.0667, 0.0, 14.3007), (-25.4840, 0.0, 18.5152), (-22.2739, 0.0, 22.2739), 
    (-18.5152, 0.0, 25.4840), (-14.3007, 0.0, 28.0667), (-9.7340, 0.0, 29.9583), (-4.9277, 0.0, 31.1122), (0.0, 0.0, 31.5), (4.9277, 0.0, 31.1122), 
    (9.7340, 0.0, 29.9583), (14.3007, 0.0, 28.0667), (18.5152, 0.0, 25.4840), (22.2739, 0.0, 22.2739), (25.4840, 0.0, 18.5152), (28.0667, 0.0, 14.3007), 
    (29.9583, 0.0, 9.7340), (31.1122, 0.0, 4.9277), (31.5, 0.0, 0.0), (31.1122, 0.0, -4.9277), (29.9583, 0.0, -9.7340), (28.0667, 0.0, -14.3007), 
    (25.4841, 0.0, -18.5152), (22.2739, 0.0, -22.2739), (18.5153, 0.0, -25.4840), (14.3007, 0.0, -28.0667), (10.0, 0.0, -30.0), (10.0, 0.0, -35.0), 
    (-5.0, 0.0, -25.0), (10.0, 0.0, -15.0), (10.0, 0.0, -20.0), (13.0777, 0.0, -17.9999), (15.7325, 0.0, -15.7325), (17.9999, 0.0, -13.0777), 
    (19.8241, 0.0, -10.1009), (21.1601, 0.0, -6.8753), (21.9752, 0.0, -3.4805), (22.2491, 0.0, 0.0), (21.9751, 0.0, 3.4805), (21.1601, 0.0, 6.8753), 
    (19.8241, 0.0, 10.1009), (17.9999, 0.0, 13.0777), (15.7325, 0.0, 15.7325), (13.0777, 0.0, 17.9999), (10.1009, 0.0, 19.8241), (6.8753, 0.0, 21.1601), 
    (3.4805, 0.0, 21.9751), (0.0, 0.0, 22.2491), (-3.4805, 0.0, 21.9751), (-6.8753, 0.0, 21.1601), (-10.1009, 0.0, 19.8241), (-13.0777, 0.0, 17.9999), 
    (-15.7325, 0.0, 15.7325), (-17.9999, 0.0, 13.0777), (-20.0, 0.0, 10.0), (-15.0, 0.0, 10.0), (-25.0, 0.0, -5.0)
]


### 23 ###

arrow3DPoints = [(0.0, 0.0, 0.0), (25.0, 0.0, 0.0), (25.0, -5.0, -5.0), (36.8664, 0.0, 0.0), (25.0, 5.0, 5.0),
    (25.0, 0.0, 0.0), (25.0, -5.0, 5.0), (36.8664, 0.0, 0.0), (25.0, 5.0, -5.0), (25.0, 0.0, 0.0)
]


##########- PIN SHAPES -###########
###################################

### 24 ###

skinnyCirclePinPoints = [(0.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 25.1519, -1.7365), (0.0, 25.6031, -3.4202), (0.0, 26.3397, -5.0),
    (0.0, 27.3396, -6.4279), (0.0, 28.5721, -7.6604), (0.0, 30.0, -8.6603), (0.0, 31.5798, -9.3969), (0.0, 33.2635, -9.8481),
    (0.0, 35.0, -10.0), (0.0, 36.7365, -9.8481), (0.0, 38.4202, -9.3969), (0.0, 40.0, -8.6603), (0.0, 41.4279, -7.6604),
    (0.0, 42.6604, -6.4279), (0.0, 43.66, -5.0), (0.0, 44.3969, -3.4202), (0.0, 44.8481, -1.7365), (0.0, 45.0, 0.0),
    (0.0, 44.8481, 1.7365), (0.0, 44.3969, 3.4202), (0.0, 43.66, 5.0), (0.0, 42.6604, 6.4279), (0.0, 41.4279, 7.6604),
    (0.0, 40.0, 8.6602), (0.0, 38.4202, 9.3969), (0.0, 36.7365, 9.8481), (0.0, 35.0, 10.0), (0.0, 33.2635, 9.8481),
    (0.0, 31.5798, 9.3969), (0.0, 30.0, 8.6603), (0.0, 28.5721, 7.6604), (0.0, 27.3396, 6.4279), (0.0, 26.3397, 5.0),
    (0.0, 25.6031, 3.4202), (0.0, 25.1519, 1.7365), (0.0, 25.0, 0.0)
]


### 25 ###

fatCirclePinPoints = [(0.0, 0.0, 0.0), (0.0, 26.3397, -5.0), (0.0, 27.3396, -6.4279), (0.0, 28.5721, -7.6604), (0.0, 30.0, -8.6603),
    (0.0, 31.5798, -9.3969), (0.0, 33.2635, -9.8481), (0.0, 35.0, -10.0), (0.0, 36.7365, -9.8481), (0.0, 38.4202, -9.3969),
    (0.0, 40.0, -8.6603), (0.0, 41.4279, -7.6604), (0.0, 42.6604, -6.4279), (0.0, 43.66, -5.0), (0.0, 44.3969, -3.4202),
    (0.0, 44.8481, -1.7365), (0.0, 45.0, 0.0), (0.0, 44.8481, 1.7365), (0.0, 44.3969, 3.4202), (0.0, 43.66, 5.0),
    (0.0, 42.6604, 6.4279), (0.0, 41.4279, 7.6604), (0.0, 40.0, 8.6602), (0.0, 38.4202, 9.3969), (0.0, 36.7365, 9.8481),
    (0.0, 35.0, 10.0), (0.0, 33.2635, 9.8481), (0.0, 31.5798, 9.3969), (0.0, 30.0, 8.6603), (0.0, 28.5721, 7.6604),
    (0.0, 27.3396, 6.4279), (0.0, 26.3397, 5.0), (0.0, 0.0, 0.0)
]

### 26 ###

skinnySquarePinPoints = [(0.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 25.0, 10.0), (0.0, 45.0, 10.0), (0.0, 45.0, -10.0),
    (0.0, 25.0, -10.0), (0.0, 25.0, 0.0)
]

### 27 ###

fatSquarePinPoints = [(0.0, 0.0, 0.0), (0.0, 25.0, 5.0), (0.0, 25.0, 10.0), (0.0, 45.0, 10.0), (0.0, 45.0, -10.0),
    (0.0, 25.0, -10.0), (0.0, 25.0, -5.0), (0.0, 0.0, 0.0)
]


### 28 ###

locatorPinPoints = [(0.0, 0.0, 0.0), (0.0, 45.0, 0.0), (0.0, 35.0, 0.0), (0.0, 35.0, -10.0), (0.0, 35.0, 10.0),
    (0.0, 35.0, 0.0), (-10.0, 35.0, 0.0), (10.0, 35.0, 0.0)
]


#########- MISC SHAPES -###########
###################################

### 29 ###

gearPoints = [(-9.8767, 0.0, 0.0), (-9.7826, 0.0, 1.6513), (-12.8866, 0.0, 4.8670), (-10.6582, 0.0, 8.7266), (-6.3214, 0.0, 7.6463), (-3.4612, 0.0, 9.2976), 
    (-2.2284, 0.0, 13.5936), (2.2284, 0.0, 13.5936), (3.4612, 0.0, 9.2976), (6.3214, 0.0, 7.6463), (10.6582, 0.0, 8.7266), (12.8866, 0.0, 4.8670), 
    (9.7826, 0.0, 1.6513), (9.7826, 0.0, -1.6513), (12.8866, 0.0, -4.8670), (10.6582, 0.0, -8.7266), (6.3214, 0.0, -7.6463), (3.4612, 0.0, -9.2976), 
    (2.2284, 0.0, -13.5936), (-2.2284, 0.0, -13.5936), (-3.4612, 0.0, -9.2976), (-6.3214, 0.0, -7.6463), (-10.6582, 0.0, -8.7266), (-12.8866, 0.0, -4.8670), 
    (-9.7826, 0.0, -1.6513), (-9.8767, 0.0, 0.0), (-5.0, 0.0, 0.0), (-4.7553, 0.0, 1.5451), (-4.0451, 0.0, 2.9389), (-2.9389, 0.0, 4.0451), (-1.5451, 0.0, 4.7553), 
    (0.0, 0.0, 5.0), (1.5451, 0.0, 4.7553), (2.9389, 0.0, 4.0451), (4.0451, 0.0, 2.9389), (4.7553, 0.0, 1.5451), (5.0, 0.0, 0.0), (4.7553, 0.0, -1.5451), 
    (4.0451, 0.0, -2.9389), (2.9389, 0.0, -4.0451), (1.5451, 0.0, -4.7553), (0.0, 0.0, -5.0), (-1.5451, 0.0, -4.7553), (-2.9389, 0.0, -4.0451), 
    (-4.0451, 0.0, -2.9389), (-4.7553, 0.0, -1.5451), (-5.0, 0.0, 0.0)
]


#########- SHAPES INDEX -##########
###################################

controllerShapes = [
	trianglePoints,#0 
	squarePoints,#1
	hexagonPoints,#2 
	octagonPoints,#3 
	circlePoints,#4
	halfCirclePoints,#5 
	pillPoints,#6 
	circleStarPoints,#7 
	starPoints,#8
	flowerPoints,#9
	locatorPoints,#10
	pyramidPoints,#11
	diamondPoints,#12
	cubePoints,#13
	spherePoints,#14
	halfCylinderPoints,#15
	tacoPoints,#16
	skinnyArrowPoints,#17	
	fatArrowPoints,#18
	doubleSidedArrowPoints,#19
	arrow90DegreesPoints,#20
	arrow180DegreesPoints,#21
	arrow270DegreesPoints,#22
	arrow3DPoints,#23
	skinnyCirclePinPoints,#24 
	fatCirclePinPoints,#25
	skinnySquarePinPoints,#26 
	fatSquarePinPoints,#27
	locatorPinPoints,#28
	gearPoints,#29
	
]

#######################################################
##################- SHAPE LIBRARY -####################
#######################################################

    
######## LOCAL ROTATION AXIS OPTIONS ########


def disableAllTransAxis(*args):
    jointList = cmds.ls(type = 'joint')
    for i in jointList:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 0)


def selectedShowTransAxis(*args):
    jointSelection = cmds.ls(sl = True)
    for i in jointSelection:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 1)


def selectedHideTransAxis(*args):
    jointSelection = cmds.ls(sl = True)
    for i in jointSelection:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 0)


def allChildrenShowTransAxis(*args):        
    allChildrenSelection = cmds.ls(sl = True)
    for i in allChildrenSelection:
        objectCheck = cmds.nodeType(i)
        if objectCheck == 'joint':
            jointsList = cmds.listRelatives(i, ad = True, type = 'joint')
            jointsList.append(i)
            for obj in jointsList:
                setAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 1)
                
            print (i + ' is a joint')
            
        if cmds.listRelatives(i, s=True, type='nurbsCurve'):
            controllersList = [i]
            descendingObjects = cmds.listRelatives(i, ad = True, type = 'transform')
            for obj in descendingObjects:
                controllerShapeObjects = cmds.listRelatives(obj, s = True, type ='nurbsCurve')
                if controllerShapeObjects:
                    controllersList.append(obj)
                    
            for obj in controllersList:
                setAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 1)
            
            print(i + ' is a controller')
        else:
            print ('Object is neither a joint or controller')

        
def allChildrenHideTransAxis(*args):        
    allChildrenSelection = cmds.ls(sl = True)
    for i in allChildrenSelection:
        objectCheck = cmds.nodeType(i)
        if objectCheck == 'joint':
            jointsList = cmds.listRelatives(i, ad = True, type = 'joint')
            jointsList.append(i)
            for obj in jointsList:
                setAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 0)
                
            print (i + ' is a joint')
            
        if cmds.listRelatives(i, s=True, type='nurbsCurve'):
            controllersList = [i]
            descendingObjects = cmds.listRelatives(i, ad = True, type = 'transform')
            for obj in descendingObjects:
                controllerShapeObjects = cmds.listRelatives(obj, s = True, type ='nurbsCurve')
                if controllerShapeObjects:
                    controllersList.append(obj)
                    
            for obj in controllersList:
                setAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 0)
            
            print(i + ' is a controller')
        else:
            print ('Object is neither a joint or controller')

######## OUTLINER SETTINGS OPTIONS ########

def get_outliner_color_number(*args):
    return cmds.colorSliderGrp("outlinerColorValue", query=True, rgb=True)

def selectedChangeOutlinerColor(*args):
    
    outlinerColor = get_outliner_color_number()
    
    sel = cmds.ls(sl = True)
    for i in sel:
        colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
        if colorCheck == 0:
            cmds.setAttr(i + '.useOutlinerColor', True)
        if colorCheck == 1:
            pass
            
        colorChange = cmds.setAttr(i + '.outlinerColor', outlinerColor[0], outlinerColor[1], outlinerColor[2], type = 'double3')
    
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)
        
def allChildrenChangeOutlinerColor(*args):
    
    outlinerColor = get_outliner_color_number()
    
    sel = cmds.ls(sl = True)
    selChildren = cmds.listRelatives(ad = True)
    outlinerAllChildren = selChildren + sel
    for i in outlinerAllChildren:
        colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
        if colorCheck == 0:
            cmds.setAttr(i + '.useOutlinerColor', True)
        if colorCheck == 1:
            pass
            
        colorChange = cmds.setAttr(i + '.outlinerColor', outlinerColor[0], outlinerColor[1], outlinerColor[2], type = 'double3')
        
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)
        
def allSceneResetOutlinerColor(*args):
    outlinerObjects = cmds.ls(transforms = True)
    for i in outlinerObjects:
        colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
        if colorCheck == 0:
            pass
        if colorCheck == 1:
            cmds.setAttr(i + '.useOutlinerColor', False)
        
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)
            
def allSceneUndoResetOutlinerColor(*args):
    outlinerObjects = cmds.ls(transforms = True)
    for i in outlinerObjects:
        colorValueCheck = cmds.getAttr(i + '.outlinerColor')
        
        if colorValueCheck != [(0.0, 0.0, 0.0)]:
        
            colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
            if colorCheck == 0:
                cmds.setAttr(i + '.useOutlinerColor', True)
            if colorCheck == 1:
                pass
    
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)
        
def selectedResetOutlinerColor(*args):
    
    sel = cmds.ls(sl = True)
    for i in sel:
        colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
        if colorCheck == 0:
            pass
        if colorCheck == 1:
            cmds.setAttr(i + '.useOutlinerColor', False)
            
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)
            
def allChildrenResetOutlinerColors(*args):
    
    sel = cmds.ls(sl = True)
    selChildren = cmds.listRelatives(ad = True)
    outlinerAllChildren = selChildren + sel
    for i in outlinerAllChildren:
        colorCheck = cmds.getAttr(i + '.useOutlinerColor')
        
        if colorCheck == 0:
            pass
        if colorCheck == 1:
            cmds.setAttr(i + '.useOutlinerColor', False)
            
    outliners = cmds.getPanel(type="outlinerPanel")

    for outliner in outliners:
        cmds.outlinerEditor(outliner, edit=True, refresh=True)

######## CONTROLLER CREATION OPTIONS ########

def get_controller_name(*args):
    return cmds.textField("controllerNameField", query=True, text=True)

def createJustController(*args):
    
    ctlName = get_controller_name()
    
    newController = cmds.circle(n = ctlName + '_CON')
    
def createZeroOffsetController(*args): 
    
    ctlName = get_controller_name()
    
    newController = cmds.circle(n = ctlName + '_CON',  nr=(1, 0, 0))
    
    offsetGroup = cmds.group(newController, n = 'OFFSET_' + ctlName)
    
    zeroGroup = cmds.group(offsetGroup, n = 'ZERO_' + ctlName)
    
    cmds.select(cl = True)
    
def MZO(*args):

    sel = cmds.ls(selection=True)

    if not sel:
        cmds.warning("Select Zero group first.")
        return

    original = sel[0]

    descendants = cmds.listRelatives(original, ad=True, type='transform') or []
    controller = original

    for node in descendants:
        if node.endswith('_CON'):
            controller = node
            break

    controllerName = controller.split('|')[-1]

    mirrorName = controllerName.replace('Left', 'TEMP_SIDE')
    mirrorName = mirrorName.replace('Right', 'Left')
    mirrorName = mirrorName.replace('TEMP_SIDE', 'Right')

    dupBranch = cmds.duplicate(original, renameChildren=True)[0]

    newScaleGrp = cmds.group(
        em=True,
        w=True,
        name='MIRROR_' + mirrorName
    )

    cmds.parent(dupBranch, newScaleGrp)
    cmds.setAttr(newScaleGrp + '.scaleX', -1)

    nodes = cmds.listRelatives(
        dupBranch,
        ad=True,
        fullPath=True
    ) or []

    for node in nodes:
        shortName = node.split('|')[-1]

        baseName = shortName
        if baseName[-1:].isdigit():
            baseName = baseName.rstrip('0123456789')

        newName = baseName.replace('Left', 'TEMP_SIDE')
        newName = newName.replace('Right', 'Left')
        newName = newName.replace('TEMP_SIDE', 'Right')

        if newName != shortName:
            cmds.rename(node, newName)

    rootName = original.split('|')[-1]
    rootName = rootName.replace('Left', 'TEMP_SIDE')
    rootName = rootName.replace('Right', 'Left')
    rootName = rootName.replace('TEMP_SIDE', 'Right')
    rootName = rootName.rstrip('0123456789')

    cmds.rename(dupBranch, rootName)
    cmds.select(newScaleGrp, replace=True)
    
    
######## SCALE OPTIONS ########

def get_entered_number(*args):
    return cmds.floatSliderGrp("scaleValue", query=True, value=True)


def singleSelectScale(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    scaleNumber = get_entered_number()
    for i in selShape:
        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        get_entered_number()
        cmds.scale(scaleNumber, scaleNumber, scaleNumber, shapeCVs)

def allChildrenScale(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    
    scaleNumber = get_entered_number()
    for i in selShape:        
        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        get_entered_number()
        cmds.scale(scaleNumber, scaleNumber, scaleNumber, shapeCVs)
        

######## SHAPE OPTIONS ########

def get_shape_number(*args):
    return cmds.optionMenu("shapeMenu", q=True, select=True) - 1


def singleSelectShape(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True, type = 'shape')
    shapeNumber = get_shape_number()
    print (selShape)
    print (shapeNumber)
    
    for i in selShape:

        shapeColor = cmds.getAttr(i + '.overrideColorRGB')
        isRGBenabled = cmds.getAttr(i + '.overrideRGBColors')
        lineWidth = cmds.getAttr(i + '.lineWidth')

        newController = cmds.curve(d = 1, p = controllerShapes[shapeNumber], n = 'tempName')
        newControllerShape = cmds.listRelatives(newController, s = True)
        
        existingParent = cmds.listRelatives(i, p = True)
        print (existingParent)

        deleteOldShape = cmds.delete(i)
        replaceController = cmds.parent(newControllerShape, sel, s = True, r = True)
        deleteNewShell = cmds.delete(newController)
        
        if isRGBenabled == 0:
            cmds.setAttr(newControllerShape[0] + '.overrideRGBColors', 0)
        else:
            cmds.setAttr(newControllerShape[0] + '.overrideRGBColors', 1)

        enableColor = cmds.setAttr(newControllerShape[0] + '.overrideEnabled', 1)
        recolorShape = cmds.setAttr(newControllerShape[0] + '.overrideColorRGB', *shapeColor[0], type = 'double3')
        rethickenLine = cmds.setAttr(newControllerShape[0] + '.lineWidth', lineWidth)
        renameShape = cmds.rename(newControllerShape, sel[0] + 'Shape')
        
    deselect = cmds.select(cl = True)

def allChildrenShape(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, ad = True, type = 'shape')
    shapeNumber = get_shape_number()
    print (shapeNumber)
    print (selShape)
    
    for i in selShape:
        print(i)
        parent = cmds.listRelatives(i, p=True)
        
        shapeColor = cmds.getAttr(i + '.overrideColorRGB')[0]
        isRGBenabled = cmds.getAttr(i + '.overrideRGBColors')
        lineWidth = cmds.getAttr(i + '.lineWidth')

        newController = cmds.curve(d = 1, p = controllerShapes[shapeNumber], n = 'tempName')
        newControllerShape = cmds.listRelatives(newController, s = True)

        deleteOldShape = cmds.delete(i)
        replaceController = cmds.parent(newControllerShape, parent[0], s = True, r = True)
        deleteNewShell = cmds.delete(newController)
        
        newShape = newControllerShape[0]
        
        if isRGBenabled == 0:
            cmds.setAttr(newControllerShape[0] + '.overrideRGBColors', 0)
        else:
            cmds.setAttr(newControllerShape[0] + '.overrideRGBColors', 1)

        enableColor = cmds.setAttr(newShape + '.overrideEnabled', 1)
        recolorShape = cmds.setAttr(newShape + '.overrideColorRGB', *shapeColor, type = 'double3')
        rethickenLine = cmds.setAttr(newShape + '.lineWidth', lineWidth)
        renameShape = cmds.rename(newControllerShape, parent[0] + 'Shape')
        
    deselect = cmds.select(cl = True)


####### ORIENT OPTIONS ########


def get_orientX_numbers(*args):
    return cmds.intField("XValue", query=True, value=True)
def get_orientY_numbers(*args):
    return cmds.intField("YValue", query=True, value=True)   
def get_orientZ_numbers(*args):
    return cmds.intField("ZValue", query=True, value=True)
    
    
    
def rotateXCounterClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientXNumbers = get_orientX_numbers()
    controllerXOrient = [orientXNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(-orientXNumbers, 0, 0, shapeCVs, r = True, os = True, fo = True)
        
        
def rotateXClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientXNumbers = get_orientX_numbers()
    controllerXOrient = [orientXNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(orientXNumbers, 0, 0, shapeCVs, r = True, os = True, fo = True)


def rotateYCounterClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientYNumbers = get_orientY_numbers()
    controllerYOrient = [orientYNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(0, -orientYNumbers, 0, shapeCVs, r = True, os = True, fo = True)
        
        
def rotateYClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientYNumbers = get_orientY_numbers()
    controllerYOrient = [orientYNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(0, orientYNumbers, 0, shapeCVs, r = True, os = True, fo = True)
        

def rotateZCounterClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientZNumbers = get_orientZ_numbers()
    controllerZOrient = [orientZNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(0, 0, -orientZNumbers, shapeCVs, r = True, os = True, fo = True)
        
        
def rotateZClockwise(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    orientZNumbers = get_orientZ_numbers()
    controllerZOrient = [orientZNumbers]
    
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(0, 0, orientZNumbers, shapeCVs, r = True, os = True, fo = True)
    
    
def singleSelectOrient(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    
    orientXNumbers = get_orientX_numbers()
    orientYNumbers = get_orientY_numbers()
    orientZNumbers = get_orientZ_numbers()
    
    controllerOrient = [orientXNumbers, orientYNumbers, orientZNumbers]
    
    print (controllerOrient)
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(controllerOrient[0], controllerOrient[1], controllerOrient[2], shapeCVs, r = True, os = True, fo = True)
        

def allChildrenOrient(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, ad = True, type = 'shape')
    
    
    orientXNumbers = get_orientX_numbers()
    orientYNumbers = get_orientY_numbers()
    orientZNumbers = get_orientZ_numbers()
    
    controllerOrient = [orientXNumbers, orientYNumbers, orientZNumbers]
    
    print (controllerOrient)
    print (selShape)
    for i in selShape:

        shapeCVs = cmds.ls(i + '.cv[*]', fl=True)
        cmds.rotate(controllerOrient[0], controllerOrient[1], controllerOrient[2], shapeCVs, r = True, os = True, fo = True)

####### COLOR OPTIONS ########


def get_controller_color_number(*args):
    return cmds.colorSliderGrp("controllerColorValue", query=True, rgb=True)
    
def singleSelectControllerColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    controllerColorNumber = get_controller_color_number()
    
    for i in selShape:
        get_controller_color_number()
        isOverideEnabled = cmds.getAttr(i + '.overrideEnabled')
        if isOverideEnabled == 0:
            cmds.setAttr(i + '.overrideEnabled', 1)
        else: 
            pass
        
        isRGBenabled = cmds.getAttr(i + '.overrideRGBColors')
        if isRGBenabled == 0:
            cmds.setAttr(i + '.overrideRGBColors', 1)
        else:
            pass
        
        colorChange = cmds.setAttr(i + '.overrideColorRGB', controllerColorNumber[0], controllerColorNumber[1], controllerColorNumber[2], type = 'double3')
        

def allChildrenControllerColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    controllerColorNumber = get_controller_color_number()
    
    for i in selShape:
        get_controller_color_number()
        isOverideEnabled = cmds.getAttr(i + '.overrideEnabled')
        if isOverideEnabled == 0:
            cmds.setAttr(i + '.overrideEnabled', 1)
        else: 
            pass
        isRGBenabled = cmds.getAttr(i + '.overrideRGBColors')
        if isRGBenabled == 0:
            cmds.setAttr(i + '.overrideRGBColors', 1)
        else:
            pass
            
        colorChange = cmds.setAttr(i + '.overrideColorRGB', controllerColorNumber[0], controllerColorNumber[1], controllerColorNumber[2], type = 'double3')

maya_index_colors = {
    0: (1.0, 0.0, 1.0),
    1: (6.710, 12.505, 0.0),
    2: (0.1, 0.031, 3.658),
    3: (1.240, 0.106, 0.018),
    4: (0.175, 0.402, 0.174),
    5: (0.294, 5.113, 0.0),
    6: (0.615, 0.615, 0.154),
    7: (0.432, 1.215, 8.664),
    8: (2.319, 0.605, 0.573),
    9: (0.029, 0.016, 0.186),
}
        
def set_controller_color_value(val, *args): 
        
    if val in maya_index_colors:
        color = maya_index_colors[val]
        cmds.colorSliderGrp("controllerColorValue", edit=True, rgb=color)

        cmds.button("controllerColorButton", edit=True, backgroundColor=color)
        
        
custom_outliner_colors = {
    0: (1.0, 0.0, 1.0),
    1: (1.0, 1.0, 0.0),
    2: (0.433, 0.433, 11.391),
    3: (1.0, 0.0, 0.0),
    4: (0.459, 0.702, 0.478),
    5: (0.0, 1.0, 0.0),
    6: (0.615, 0.615, 0.154),
    7: (0.0, 1.0, 1.0),
    8: (2.4, 0.6, 0.6),
    9: (0.78, 0.78, 0.78),
}
        
def set_float_color_value(val, *args):
    if val in custom_outliner_colors:
        color = custom_outliner_colors[val]
        cmds.colorSliderGrp("outlinerColorValue", edit=True, rgb=color)

        cmds.button("outlinerColorButton", edit=True, backgroundColor=color)
        
def choose_outliner_color(*args):
    current = cmds.colorSliderGrp('outlinerColorValue', q=True, rgb=True)

    cmds.colorEditor(rgb=current)

    if cmds.colorEditor(q=True, result=True):
        new_color = cmds.colorEditor(q=True, rgb=True)

        cmds.colorSliderGrp('outlinerColorValue', e=True, rgb=new_color)

        cmds.button('outlinerColorButton', e=True, backgroundColor=new_color)
        
        
def choose_controller_color(*args):
    current = cmds.colorSliderGrp('controllerColorValue', q=True, rgb=True)

    cmds.colorEditor(rgb=current)

    if cmds.colorEditor(q=True, result=True):
        new_color = cmds.colorEditor(q=True, rgb=True)

        cmds.colorSliderGrp('controllerColorValue', e=True, rgb=new_color)

        cmds.button('controllerColorButton', e=True, backgroundColor=new_color)

    
####### LINE WIDTH OPTIONS ########

        
def get_width_number(*args):
    return cmds.floatSliderGrp("widthValue", query=True, value=True)


def singleSelectWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    widthNumber = get_width_number()
    for i in selShape:
        shapeCVs = cmds.ls(i + '.lineWidth', fl=True)
        get_width_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)

def allChildrenWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    
    widthNumber = get_width_number()
    for i in selShape:        
        shapeCVs = cmds.ls(i + '.lineWidth', fl=True)
        get_width_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)
        
####### MATCH TRANSFORMS OPTIONS ########
        
def matchTransformsButton(*args):
    sel = cmds.ls(selection=True)
    
    matchTrxBox = "matchTrxBox"
    matchRotBox = "matchRotBox"
    matchSclBox = "matchSclBox"
    matchPivBox = "matchPivBox"
    
    checkMatchBoxTrx = cmds.checkBox(matchTrxBox, q=True, v=True)
    checkMatchBoxRot = cmds.checkBox(matchRotBox, q=True, v=True)
    checkMatchBoxScl = cmds.checkBox(matchSclBox, q=True, v=True)
    checkMatchBoxPiv = cmds.checkBox(matchPivBox, q=True, v=True)
    
    if len(sel) < 2:
        print ("selection has less than 2 objects")
    elif len(sel) > 2: 
        print ("more than 2 objects selected")
    else:
        print ("only 2 objects selected")
        if checkMatchBoxTrx:
            matchTrx = cmds.matchTransform(sel[0], sel[1], pos = True)
        if checkMatchBoxRot:
            matchTrx = cmds.matchTransform(sel[0], sel[1], rot = True)
        if checkMatchBoxScl:
            matchTrx = cmds.matchTransform(sel[0], sel[1], scl = True)
        if checkMatchBoxPiv:
            matchTrx = cmds.matchTransform(sel[0], sel[1], piv = True)
        
        
        
####### LOCK ATTRIBUTE OPTIONS ########


trxAttrs = ['.translateX', '.translateY', '.translateZ']
rotAttrs = ['.rotateX', '.rotateY', '.rotateZ']
scaleAttrs = ['.scaleX', '.scaleY', '.scaleZ']
visAttrs = ['.visibility']



        
######## SCENE LOCKING OPTIONS ########

def child_safety_lock(lockedValue):
    
    nodes = cmds.ls(dag = True, l = True)
    
    for i in nodes:
        try: 
            cmds.lockNode(i, l = lockedValue)
        except RuntimeError:
            pass
            
def toggle_child_safety_lock(*args):
    
    button = "childSafetyLockButton"
    status = cmds.button(button, q = True, label = True)
    
    if status == "Status: UNLOCKED":
        clickResult = cmds.confirmDialog(t = "Lock scene objects?",
        m = "WARNING: Locking scene nodes means all objects cannot be deleted, renamed, reparented, or have modified attributes. Locked nodes can still be animated. Only recommended once a rig is FINALIZED!",
        b = ["Lock", "Cancel"], db = "Cancel", cb = "Cancel")
        
        if clickResult:
            child_safety_lock(True)
            
            cmds.button(button, e = True, label = "Status: LOCKED", bgc = [0.4, 0.0, 0.0])
        
        
    elif status == "Status: LOCKED":
        clickResult = cmds.confirmDialog(t = "Unlock scene objects?",
        m = "WARNING: Unlocking scene nodes means all objects can be deleted, renamed, reparented, or have modified attributes.",
        b = ["Unlock", "Cancel"], db = "Cancel", cb = "Cancel")
        
        if clickResult:
        
            child_safety_lock(False)
            
            cmds.button(button, e = True, label = "Status: UNLOCKED", bgc = [0.1, 0.4, 0.])
            
######## HELP BUTTON OPTIONS ########

def open_help_website(*args):
    webbrowser.open("https://www.karolyart.com/works/breakdowns/vfs-student-tools")
        
######## WINDOW & UI ########

WIN_NAME = "KarolyControllyEditor"      # internal control name: no spaces (same style as the UV tool)
WIN_LABEL = "Karoly Controlly Editor"   # what the user sees on the tab / title bar


def karoly_controlly_editor():
    """Launcher (called by the shelf button). Creates the workspaceControl ONCE, then only shows it.

    Never deleteUI / workspaceControlState(remove=True) a control that may be docked - that's what
    crashed Maya. Maya builds the contents by calling uiScript -> build_ui().
    """
    if not cmds.workspaceControl(WIN_NAME, exists=True):
        # Fully qualified so Maya can rebuild the UI on its own (restore a docked layout, etc.)
        uiScript = "import {0}; {0}.build_ui()".format(__name__)
        cmds.workspaceControl(WIN_NAME, label = WIN_LABEL, fl = True, retain = False,
                              ih = 1000, iw = 200, wp = 'free', rsw = 200, uiScript = uiScript)

    cmds.workspaceControl(WIN_NAME, edit = True, restore = True)
    cmds.workspaceControl(WIN_NAME, edit = True, visible = True)


def build_ui(*args):
    """Builds the tool's UI inside the workspaceControl. Maya calls this through uiScript."""
    scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16, w = 267)

    bigHeaderColor = [0.15, 0.15, 0.15]
    smallHeaderColor = [0.2, 0.2, 0.2]
    #scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=50)
    cmds.columnLayout( adjustableColumn=True )
    #cmds.text( label='Select HIPS joint', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    #cmds.button( label='Build FK Controllers', command = fk_controller_builder, w = 200)
    #cmds.separator(st = 'none', h = 15)
    cmds.text( label='LOCAL ROTATION AXIS', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=bigHeaderColor)
    cmds.separator(st = 'none', h = 2)
    #cmds.separator(st = 'none', h = 5)
                    
                    
    cmds.rowLayout(numberOfColumns=6)
    cmds.separator(hr = False, h = 15, w = 50, vis = False)
    cmds.text(label = 'Joints: ')
    jointsLRTBoxes = cmds.checkBox(label = '', v = 1)
    cmds.separator(hr = False, h = 15, w = 18, vis = False)
    cmds.text(label = 'Controllers: ')
    controllersLRTBoxes = cmds.checkBox(label = '')
    
    
    def showAllOptionsBox(*args):
    
        jointList = cmds.ls(type = 'joint')
        transformsList = cmds.ls(tr = True)
        
        controllerList = []
        
        for i in transformsList:
            objShapes = cmds.listRelatives(i, shapes = True, type = 'nurbsCurve')         

            if objShapes:
                controllerList.append(i) 
            
        
        checkLRTBoxJoints = cmds.checkBox(jointsLRTBoxes, q = True, v = True)
        checkLRTBoxControllers = cmds.checkBox(controllersLRTBoxes, q = True, v = True)
        
        if checkLRTBoxJoints:
            print ("Joints is checked")
            
        if checkLRTBoxControllers:
            print ("Controllers is checked")
            
        if checkLRTBoxJoints:
            for obj in jointList:
                if checkLRTBoxJoints:
                    setJointAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 1)
                    
        if checkLRTBoxControllers:
            for obj in controllerList:
                if checkLRTBoxControllers:
                    setControllerAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 1)


    def hideAllOptionsBox(*args):
    
        jointList = cmds.ls(type = 'joint')
        transformsList = cmds.ls(tr = True)
        
        controllerList = []
        
        for i in transformsList:
            objShapes = cmds.listRelatives(i, shapes = True, type = 'nurbsCurve')         

            if objShapes:
                controllerList.append(i) 
            
        
        checkLRTBoxJoints = cmds.checkBox(jointsLRTBoxes, q = True, v = True)
        checkLRTBoxControllers = cmds.checkBox(controllersLRTBoxes, q = True, v = True)
        
        if checkLRTBoxJoints:
            print ("Joints is checked")
            
        if checkLRTBoxControllers:
            print ("Controllers is checked")
            
        if checkLRTBoxJoints:
            for obj in jointList:
                if checkLRTBoxJoints:
                    setJointAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 0)
                    
        if checkLRTBoxControllers:
            for obj in controllerList:
                if checkLRTBoxControllers:
                    setControllerAxisDisplay = cmds.setAttr(obj + '.displayLocalAxis', 0)
                    
                    
    #####
    
    cmds.setParent( '..' )
    
    #cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=5)
    
    cmds.separator(hr = False, h = 5, w = 18, vis = False)
    cmds.button(label="Show All", w = 100, bgc=[0.5, 0.5, 1], command=showAllOptionsBox)
    cmds.separator(hr = False, w = 1, vis = False)
    cmds.button(label="Hide All", w = 100, bgc=[0.5, 0.5, 1], command=hideAllOptionsBox)

    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'single', h = 5)
    
    cmds.rowLayout(numberOfColumns=5)
    
    cmds.separator(hr = False, h = 23, w = 18, vis = False)
    cmds.button(label="Show Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=selectedShowTransAxis)
    cmds.separator(hr = False, w = 1, vis = False)
    cmds.button(label="Show All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=allChildrenShowTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=4)
    
    cmds.separator(hr = False, h = 23, w = 18, vis = False)
    cmds.button(label="Hide Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=selectedHideTransAxis)
    cmds.separator(hr = False, w = 1, vis = False)
    cmds.button(label="Hide All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=allChildrenHideTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 3)
    
    cmds.rowLayout(numberOfColumns=1)
    
    cmds.text( label='MATCH TRANSFORMS', align='center', fn = 'boldLabelFont', w = 245, h = 25, bgc=bigHeaderColor)
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=13) 
    
    cmds.button(label="Match", command = matchTransformsButton, w = 70, bgc=[0.9, 0.6, 0.3])

    cmds.columnLayout(adjustableColumn=True, w=105)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 7, st = 'none')
    cmds.text(label = 'Translation: ')
    matchTrxBox = cmds.checkBox("matchTrxBox", label = '', v = 1)
    cmds.separator(hr = False, h = 18, w = 19, st = 'out')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=5)
    cmds.separator(hr = False, h = 18, w = 19, st = 'none') 
    cmds.text(label = 'Rotation: ')
    matchRotBox = cmds.checkBox("matchRotBox", label = '', v = 1)
    cmds.separator(hr = False, h = 18, w = 6, st = 'none')
    cmds.separator(hr = False, h = 18, w = 3, st = 'out')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    cmds.columnLayout(adjustableColumn=True, w=60)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 1, st = 'none')
    cmds.text(label = 'Scale: ')
    matchSclBox = cmds.checkBox("matchSclBox", label = '')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 1, st = 'none')
    cmds.text(label = 'Pivot: ')
    matchPivBox = cmds.checkBox("matchPivBox", label = '')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    

    
    #####
    

    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.text( label='OUTLINER COLOR', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=bigHeaderColor)
    cmds.separator(st = 'none', h = 3)

    
    
    cmds.rowLayout(numberOfColumns=1)

    #cmds.text( label='Color', align='left', w = 50 )
    #cmds.colorSliderGrp('outlinerColorValue', label='', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(1, 80, 72), vis = False )
    
    #cmds.columnLayout(adjustableColumn=True, w=70)
    
    #cmds.button(label="Selected", command = selectedChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.9])
    #cmds.separator(st='none', h=3)
    #cmds.button(label="All Children", command = allChildrenChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #cmds.setParent( '..' )    
    
    cmds.setParent( '..' ) 
    
    cmds.rowLayout(numberOfColumns=10)
    
    cmds.colorSliderGrp('outlinerColorValue', label='', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(0, 0, 0), w = 1)
    
    swatchWidth = 25
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='OG', ann = "Original outliner color", w = swatchWidth, bgc=[0.78, 0.78, 0.78], command=lambda x: set_float_color_value(9))
    cmds.separator(st='none', h=3)
    cmds.button(label='0', w = swatchWidth, bgc=[1.0, 0.0, 1.0], command=lambda x: set_float_color_value(0))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='1', w = swatchWidth, bgc=[1.0, 1.0, 0.0], command=lambda x: set_float_color_value(1))
    cmds.separator(st='none', h=3)
    cmds.button(label='2', w = swatchWidth, bgc=[0.4, 0.4, 0.1], command=lambda x: set_float_color_value(6))

    cmds.setParent( '..' ) 

    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='3', w = swatchWidth, bgc=[0.0, 0.25, 1.0], command=lambda x: set_float_color_value(2))
    cmds.separator(st='none', h=3)
    cmds.button(label='4', w = swatchWidth, bgc=[0.0, 1.0, 1.0], command=lambda x: set_float_color_value(7))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='5', w = swatchWidth, bgc=[1.0, 0.0, 0.0], command=lambda x: set_float_color_value(3))
    cmds.separator(st='none', h=3)
    cmds.button(label='6', w = swatchWidth, bgc=[2.4, 0.6, 0.6], command=lambda x: set_float_color_value(8))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='7', w = swatchWidth, bgc=[0.0, 1.0, 0.0], command=lambda x: set_float_color_value(5)) 
    cmds.separator(st='none', h=3)
    cmds.button(label='8', w = swatchWidth, bgc=[0.46, 0.7, 0.48], command=lambda x: set_float_color_value(4)) 

    cmds.setParent( '..' ) 

    #cmds.colorSliderGrp('outlinerColorValue', label='', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(1, 80, 72) )
    #cmds.colorInputWidgetGrp('outlinerColorValue', label = '', h = 80, w = 120)
    cmds.separator(hr = False, h = 53, w = 8, st = 'out')
    cmds.button('outlinerColorButton', ann = "Create custom colors here", label='', command = choose_outliner_color, w = 20, h = 53, bgc=[0.78, 0.78, 0.78])
    cmds.separator(hr = False, h = 53, w = 3, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = selectedChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )    
    
    
    
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 5)
    
    cmds.text( label='CONTROLLER CREATOR', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=bigHeaderColor)
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=2)


    cmds.separator(hr = False, h = 23, w = 20, vis = False)
    cmds.textField("controllerNameField", w = 200, pht = 'Enter Controller Name')
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 30, w = 50, vis = False)
    #cmds.button(label="Create Controller", w = 100, bgc=[0.9, 0.4, 0.3], command=createJustController)
    cmds.button(label="ZO", ann = "Uses the name entered from above. \nCreates controller with ZO groups. \n( zero | offset )", w = 70, bgc=[0.9, 0.5, 0.3], command=createZeroOffsetController)
    cmds.separator(hr = False, w = 1, vis = False)
    cmds.button(label="MZO", ann = "Used for branches ONLY! \nConverts ZO into MZO. \n( mirrored | zero | offset )", w = 70, bgc=[0.9, 0.6, 0.3], command=MZO)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.text( label='CONTROLLER SETTINGS', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=bigHeaderColor)
    #cmds.separator(st = 'none', h = 1)
    cmds.text( label='SCALE', align='center', fn = 'smallPlainLabelFont', w = 20, h = 15, bgc=smallHeaderColor)
    cmds.separator(st = 'none', h = 1)

    cmds.rowLayout(numberOfColumns=3) 

    #cmds.text( label='Scale', align='left', w = 50 )
    cmds.floatSliderGrp("scaleValue", value=1.0, minValue=0.1, maxValue=2, pre = 1, field = True, cw2 = [50, 115]) 
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectScale, w = 40, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenScale, w = 10, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )   
    
    
    #cmds.button(label="Selected", command = singleSelectScale, w = 70, bgc=[0.3, 0.8, 0.9])
    #cmds.button(label="All Children", command = allChildrenScale, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    cmds.text( label='SHAPE', align='center', fn = 'smallPlainLabelFont', w = 20, h = 15, bgc=smallHeaderColor)
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    #cmds.separator(hr = False, h = 1, w = 40, st = 'none')
    cmds.setParent( '..' )
    
    #cmds.separator(st='none', h=1)

    cmds.rowLayout(numberOfColumns=4)

    #cmds.text(label='Shape', align='left', w=50)

    cmds.optionMenu("shapeMenu", w=172)


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

    #cmds.button(label="Selected", command = singleSelectShape, w=70, bgc=[0.3, 0.8, 0.9])
    #cmds.button(label="All Children", command = allChildrenShape, w=70, bgc=[0.3, 0.8, 0.7])
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectShape, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenShape, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )   
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    cmds.text( label='ORIENT', align='center', fn = 'smallPlainLabelFont', w = 20, h = 15, bgc=smallHeaderColor)
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    #cmds.separator(hr = False, h = 1, w = 40, st = 'none')
    cmds.setParent( '..' )

    
    #####
    
    cmds.setParent( '..' )
    
    #cmds.separator(st='none', h=1)
    
    cmds.rowLayout(numberOfColumns=26) 

    #cmds.text( label='Orient', align='left', w = 52 )
    
    cmds.columnLayout(adjustableColumn=True, w=55)
    cmds.rowLayout(numberOfColumns=3)
    cmds.separator(st='none', w=4) 
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', command =  rotateXCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateXclockwise', command = rotateXClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='X:', align='left', w = 10 )
    cmds.intField("XValue", value=90, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.columnLayout(adjustableColumn=True, w=55)
    cmds.rowLayout(numberOfColumns=3)
    cmds.separator(st='none', w=4) 
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateYcounterclockwise', command =  rotateYCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateYclockwise', command =  rotateYClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='Y:', align='left', w = 10 )
    cmds.intField("YValue", value=90, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.columnLayout(adjustableColumn=True, w=55)
    cmds.rowLayout(numberOfColumns=3) 
    cmds.separator(st='none', w=4)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateZcounterclockwise', command =  rotateZCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateZclockwise',  command =  rotateZClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='Z:', align='left', w = 10 )
    cmds.intField("ZValue", value=90, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.separator(st='none', w=1)
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    
    cmds.button(label="Selected", command = singleSelectOrient, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenOrient, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    cmds.text( label='COLOR', align='center', fn = 'smallPlainLabelFont', w = 248, h = 15, bgc=smallHeaderColor)
    cmds.separator(st = 'none', h = 3)
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    
    #cmds.separator(hr = False, h = 1, w = 40, st = 'none')


    
    #####
    
    
    cmds.setParent( '..' ) 
    
    cmds.rowLayout(numberOfColumns=10)
    
    cmds.colorSliderGrp('controllerColorValue', label='', rgb=(0.029, 0.016, 0.186), cl3 = ('left', 'left', 'left'), cw3=(0, 0, 0), w = 1)
    
    swatchWidth = 25
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='OG', ann = "Original controller color", w = swatchWidth, bgc=[0.029, 0.016, 0.186], command=lambda x: set_controller_color_value(9))
    cmds.separator(st='none', h=3)
    cmds.button(label='0', w = swatchWidth, bgc=[1.0, 0.0, 1.0], command=lambda x: set_controller_color_value(0))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='1', w = swatchWidth, bgc=[1.0, 1.0, 0.0], command=lambda x: set_controller_color_value(1))
    cmds.separator(st='none', h=3)
    cmds.button(label='2', w = swatchWidth, bgc=[0.4, 0.4, 0.1], command=lambda x: set_controller_color_value(6))

    cmds.setParent( '..' ) 

    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='3', w = swatchWidth, bgc=[0.0, 0.25, 1.0], command=lambda x: set_controller_color_value(2))
    cmds.separator(st='none', h=3)
    cmds.button(label='4', w = swatchWidth, bgc=[0.0, 1.0, 1.0], command=lambda x: set_controller_color_value(7))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='5', w = swatchWidth, bgc=[1.0, 0.0, 0.0], command=lambda x: set_controller_color_value(3))
    cmds.separator(st='none', h=3)
    cmds.button(label='6', w = swatchWidth, bgc=[2.4, 0.6, 0.6], command=lambda x: set_controller_color_value(8))

    cmds.setParent( '..' ) 
    
    cmds.columnLayout(adjustableColumn=True, w=swatchWidth)
    cmds.button(label='7', w = swatchWidth, bgc=[0.0, 1.0, 0.0], command=lambda x: set_controller_color_value(5)) 
    cmds.separator(st='none', h=3)
    cmds.button(label='8', w = swatchWidth, bgc=[0.46, 0.7, 0.48], command=lambda x: set_controller_color_value(4)) 

    cmds.setParent( '..' ) 

    #cmds.colorSliderGrp('outlinerColorValue', label='', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(1, 80, 72) )
    #cmds.colorInputWidgetGrp('outlinerColorValue', label = '', h = 80, w = 120)
    cmds.separator(hr = False, h = 53, w = 8, st = 'out')
    cmds.button('controllerColorButton', ann = "Create custom colors here", label='', command = choose_controller_color, w = 20, h = 53, bgc=[0.029, 0.016, 0.186])
    cmds.separator(hr = False, h = 53, w = 3, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectControllerColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenControllerColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )  
    
    cmds.setParent( '..' ) 
    

    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))



    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 3)
    cmds.text( label='THICKNESS', align='center', fn = 'smallPlainLabelFont', w = 248, h = 15, bgc=smallHeaderColor)
    
    cmds.separator(st = 'none', h = 1)

    
    cmds.rowLayout(numberOfColumns=4) 

    #cmds.text( label='Thickness', align='left', w = 50 )
    cmds.floatSliderGrp("widthValue", value=1, minValue=1, maxValue=10, pre = 0, field = True, cw2 = [50, 115]) 
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectWidth, w = 40, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenWidth, w = 10, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    ###
    
    def onLockChanged(value):
        if value:
            cmds.checkBox(unlockUnhideAttrBox, e = True, v = False)
            cmds.checkBox(unhideAttrBox  , e = True, v = False)
            
    def onHideChanged(value):
        if value:
            cmds.checkBox(unlockUnhideAttrBox, e = True, v = False)
            cmds.checkBox(unhideAttrBox  , e = True, v = False)
            
    def onUnlockUnhideHideChanged(value):
        if value:
            cmds.checkBox(lockAttrBox , e = True, v = False)
            cmds.checkBox(hideAttrBox  , e = True, v = False)
            cmds.checkBox(unhideAttrBox  , e = True, v = False)
            
    def onUnhideHideChanged(value):
        if value:
            cmds.checkBox(lockAttrBox , e = True, v = False)
            cmds.checkBox(hideAttrBox  , e = True, v = False)
            cmds.checkBox(unlockUnhideAttrBox  , e = True, v = False)

    cmds.rowLayout(numberOfColumns=4) 
    cmds.setParent( '..' )
    
    #cmds.separator(st = 'in', h = 1)
    
    cmds.text( label='ATTRIBUTE LOCKER', align='center', fn = 'boldLabelFont', w = 248, h = 25, bgc=bigHeaderColor)
    #cmds.separator(st = 'none', h = 1)
    

    ##############
    
    cmds.rowLayout(numberOfColumns=13) 
    
    cmds.text( label='1', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    
    cmds.separator(hr = False, h = 18, w = 20, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=90)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 15, st = 'none')
    cmds.text(label = ' Scale: ')
    scaleAttrBox = cmds.checkBox(label = '', v = 1)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    #cmds.separator(hr = False, h = 18, w = 1, st = 'none')
    cmds.text(label = ' Visibility: ')
    visAttrBox = cmds.checkBox(label = '', v = 1)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    cmds.columnLayout(adjustableColumn=True, w=85)
    cmds.rowLayout(numberOfColumns=3)
    #cmds.separator(hr = False, h = 18, w = 15, st = 'none')
    cmds.text(label = 'Translation: ')
    transAttrBox = cmds.checkBox(label = '')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 10, st = 'none')
    cmds.text(label = 'Rotation: ')
    rotAttrBox = cmds.checkBox(label = '')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=2, w=247, columnAlign=(1, 'center'))
    #cmds.separator(hr = False, h = 5, w = 40, st = 'none')
    cmds.separator(hr = True, h = 1, w = 247, st = 'single')
    cmds.setParent( '..' )
    

    
    ##############
    
    cmds.rowLayout(numberOfColumns=13) 
    
    cmds.text( label='2', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    
    cmds.separator(hr = False, h = 10, w = 20, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 2, st = 'none') 
    cmds.text(label = 'Lock: ')
    lockAttrBox = cmds.checkBox(label = '', cc = onLockChanged, v = 1)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4) 
    cmds.separator(hr = False, h = 18, w = 1, st = 'none')
    cmds.text(label = 'Hide: ')
    hideAttrBox = cmds.checkBox(label = '', cc = onHideChanged, v = 1)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    cmds.columnLayout(adjustableColumn=True, w=120)
    cmds.rowLayout(numberOfColumns=3)
    #cmds.separator(hr = False, h = 18, w = 15, st = 'none')
    cmds.text(label = 'Unlock & Unhide: ')
    unlockUnhideAttrBox = cmds.checkBox(label = '', cc = onUnlockUnhideHideChanged)
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 49, st = 'none')
    cmds.text(label = 'Unhide: ')
    unhideAttrBox = cmds.checkBox(label = '', cc = onUnhideHideChanged)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=2, w=247, columnAlign=(1, 'center'))
    #cmds.separator(hr = True, h = 10, w = 20, st = 'single')
    cmds.separator(hr = True, h = 5, w = 247, st = 'single')
    cmds.setParent( '..' )
    
    ##############
    
    
    def singleControllerAttrBoxes(*args):
        
        sel = cmds.ls(selection=True)
        
        checkBoxTrx = cmds.checkBox(transAttrBox, q=True, v=True)
        checkBoxRot = cmds.checkBox(rotAttrBox, q=True, v=True)
        checkBoxScale = cmds.checkBox(scaleAttrBox, q=True, v=True)
        checkBoxVis = cmds.checkBox(visAttrBox, q=True, v=True)
        
        checkLockBox = cmds.checkBox(lockAttrBox, q=True, v=True)
        checkHideBox = cmds.checkBox(hideAttrBox, q=True, v=True)
        checkUnlockUnhideBox = cmds.checkBox(unlockUnhideAttrBox, q=True, v=True)
        checkUnhideBox = cmds.checkBox(unhideAttrBox, q=True, v=True)
        
        if checkBoxTrx:
            print ("Translation is checked")
            
        if checkBoxRot:
            print ("Rotation is checked")
        
        if checkBoxScale:
            print ("Scale is checked")
            
        if checkBoxVis:
            print ("Visibility is checked")
            
        if checkLockBox:
            for obj in sel:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = True)
            print ("Lock is checked")
            
        if checkHideBox:
            for obj in sel:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
            print ("Hide is checked")
        
        if checkUnlockUnhideBox:
            for obj in sel:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
            print ("Unlock & Unhide is checked")
            
        if checkUnhideBox:
            for obj in sel:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, cb = True)
            print ("Unhide is checked")
            
            
            
    def allChildrenControllerAttrBoxes(*args):
        
        sel = cmds.ls(selection=True)
        selChildren = cmds.listRelatives(sel[0], ad = True, type = 'transform')
        allAttributesChildren = sel + selChildren
        
        cmds.columnLayout(adjustableColumn=True, w=70)
        
        checkBoxTrx = cmds.checkBox(transAttrBox, q=True, v=True)
        checkBoxRot = cmds.checkBox(rotAttrBox, q=True, v=True)
        checkBoxScale = cmds.checkBox(scaleAttrBox, q=True, v=True)
        checkBoxVis = cmds.checkBox(visAttrBox, q=True, v=True)
        
        checkLockBox = cmds.checkBox(lockAttrBox, q=True, v=True)
        checkHideBox = cmds.checkBox(hideAttrBox, q=True, v=True)
        checkUnlockUnhideBox = cmds.checkBox(unlockUnhideAttrBox, q=True, v=True)
        checkUnhideBox = cmds.checkBox(unhideAttrBox, q=True, v=True)
        
        if checkBoxTrx:
            print ("Translation is checked")
            
        if checkBoxRot:
            print ("Rotation is checked")
        
        if checkBoxScale:
            print ("Scale is checked")
            
        if checkBoxVis:
            print ("Visibility is checked")
            
        if checkLockBox:
            for obj in allAttributesChildren:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = True)
            print ("Lock is checked")
            
        if checkHideBox:
            for obj in allAttributesChildren:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = True, cb = False, k = False)
            print ("Hide is checked")
        
        if checkUnlockUnhideBox:
            for obj in allAttributesChildren:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, l = False, k = True)
            print ("Unlock & Unhide is checked")
            
        if checkUnhideBox:
            for obj in allAttributesChildren:
                if checkBoxTrx:
                    for attr in trxAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxRot:
                    for attr in rotAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxScale:
                    for attr in scaleAttrs:
                        cmds.setAttr(obj + attr, cb = True)
                        
                if checkBoxVis:
                    for attr in visAttrs:
                        cmds.setAttr(obj + attr, cb = True)
            print ("Unhide is checked")
        
        
        
    cmds.rowLayout(numberOfColumns=6) 
    cmds.text( label='3', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(hr = False, h = 18, w = 35, st = 'none')
    cmds.button(label="Selected", command = singleControllerAttrBoxes, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(hr = False, w = 1, vis = False)
    cmds.button(label="All Children", command = allChildrenControllerAttrBoxes, w = 70, bgc=[0.3, 0.8, 0.7])
    cmds.separator(st = 'none', h = 3)
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 5)
    

    
    cmds.text( label='CHILD PROOF LOCK', align='center', fn = 'boldLabelFont', w = 248, h = 25, bgc=bigHeaderColor)
    
    cmds.separator(st = 'none', h = 6)
    
    cmds.rowLayout(numberOfColumns=2)
    cmds.separator(st = 'none', w = 20)
    childSafetyLockButton = cmds.button("childSafetyLockButton", ann = "Use ONLY when the rig is completely finished. \nWill be Animation Ready and keyable. \nLocks all objects in the scene & prevents things from being deleted, renamed, or reorganized.", label="Status: UNLOCKED", c = toggle_child_safety_lock, w = 200, bgc=[0.1, 0.4, 0.0])
    cmds.setParent( '..' )
    #cmds.text(label="Locks DAG nodes; NOT a complete scene safeguard.", font="smallPlainLabelFont", height=14)
    cmds.rowLayout(numberOfColumns=1)
    
    
    cmds.setParent( '..' )
    
    
    cmds.separator(st = 'in', h = 10, w = 247)

    
    cmds.rowLayout(numberOfColumns=5)
    
    
    #cmds.separator(st = 'none', w = 20)
    cmds.separator(hr = False, h = 18, w = 5, st = 'out')
    
    cmds.text(label = 'GD76 Roman Karoly | Version 1.28', align = 'left', w = 170, fn = 'obliqueLabelFont')
    
    cmds.separator(hr = False, h = 18, w = 5, st = 'out')
    
    cmds.button(l = "Help?", ann = "Need help? This is a link to my website that documents my tools. \nDisclaimer: All free tools provided are intended solely for educational, informational, & personal use. \nThe tools provided are available royalty free. \nUse at your own risk.",c = open_help_website, bgc = [4.0, 4.0, 0.0], w = 60)
    
    cmds.setParent( '..' )