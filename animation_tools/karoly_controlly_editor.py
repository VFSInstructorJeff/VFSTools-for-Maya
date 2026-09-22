import maya.cmds as cmds
import json

######## DEFAULT CONTROLLER SETTINGS ########

DEFAULT_CONTROLLER_DATA = {
    "controllers": {
        "HeadTop_End_ctl": {"radius": 0.0, "color": 17, "lineWidth": -1.0},
        "Head_ctl": {"radius": 10.0, "color": 17, "lineWidth": -1.0},
        "Hips_ctl": {"radius": 25.0, "color": 14, "lineWidth": 3.0},

        "LeftArm_ctl": {"radius": 9.0, "color": 18, "lineWidth": -1.0},
        "LeftForeArm_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},
        "LeftHand_ctl": {"radius": 6.0, "color": 18, "lineWidth": -1.0},

        "LeftHandThumb1_ctl": {"radius": 3.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandThumb4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandIndex1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandIndex4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandMiddle1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandMiddle4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandRing1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandRing4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftHandPinky1_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky2_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky3_ctl": {"radius": 2.0, "color": 18, "lineWidth": -1.0},
        "LeftHandPinky4_ctl": {"radius": 0.0, "color": 18, "lineWidth": -1.0},

        "LeftShoulder_ctl": {"radius": 10.0, "color": 18, "lineWidth": 3.0},
        "LeftUpLeg_ctl": {"radius": 15.0, "color": 18, "lineWidth": 2.0},
        "LeftLeg_ctl": {"radius": 12.0, "color": 18, "lineWidth": -1.0},
        "LeftFoot_ctl": {"radius": 10.0, "color": 18, "lineWidth": -1.0},
        "LeftToeBase_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},
        "LeftToe_End_ctl": {"radius": 8.0, "color": 18, "lineWidth": -1.0},

        "Spine_ctl": {"radius": 13.0, "color": 17, "lineWidth": -1.0},
        "Spine1_ctl": {"radius": 15.0, "color": 17, "lineWidth": -1.0},
        "Spine2_ctl": {"radius": 19.0, "color": 17, "lineWidth": -1.0},
        "Neck_ctl": {"radius": 12.0, "color": 17, "lineWidth": -1.0},

        "RightArm_ctl": {"radius": 9.0, "color": 20, "lineWidth": -1.0},
        "RightForeArm_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0},
        "RightHand_ctl": {"radius": 6.0, "color": 20, "lineWidth": -1.0},

        "RightHandThumb1_ctl": {"radius": 3.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandThumb4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandIndex1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandIndex4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandMiddle1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandMiddle4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandRing1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandRing4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightHandPinky1_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky2_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky3_ctl": {"radius": 2.0, "color": 20, "lineWidth": -1.0},
        "RightHandPinky4_ctl": {"radius": 0.0, "color": 20, "lineWidth": -1.0},

        "RightShoulder_ctl": {"radius": 10.0, "color": 20, "lineWidth": 3.0},
        "RightUpLeg_ctl": {"radius": 15.0, "color": 20, "lineWidth": 2.0},
        "RightLeg_ctl": {"radius": 12.0, "color": 20, "lineWidth": -1.0},
        "RightFoot_ctl": {"radius": 10.0, "color": 20, "lineWidth": -1.0},
        "RightToeBase_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0},
        "RightToe_End_ctl": {"radius": 8.0, "color": 20, "lineWidth": -1.0}
    }
}

###                                                 ###
#######################################################
##################- SHAPE LIBRARY -####################
#######################################################
###                                                 ###



##########- FLAT SHAPES -##########
###################################

### 0 ###

trianglePoints = [(10.0, 0.0,  10.0), (-10.0, 0.0,  0.0), (10.0, 0.0, -10.0), (10.0, 0.0,  10.0)]


### 1 ###

squarePoints = [(-10.0, 0.0,  10.0), (-10.0, 0.0, -10.0), ( 10.0, 0.0, -10.0), ( 10.0, 0.0,  10.0), (-10.0, 0.0,  10.0)]


### 2 ###

hexagonPoints = [(-5.0, 0.0, -8.6603), ( 5.0, 0.0, -8.6603), (10.0, 0.0,  0.0), ( 5.0, 0.0,  8.6603), (-5.0, 0.0,  8.6603), (-10.0, 0.0, 0.0), (-5.0, 0.0, -8.6603)]


### 3 ###

octagonPoints = [(-4.2095, 0.0, -10.1627), ( 4.2095, 0.0, -10.1627), (10.1627, 0.0, -4.2095), (10.1627, 0.0,  4.2095), ( 4.2095, 0.0, 10.1627),
    (-4.2095, 0.0, 10.1627), (-10.1627,0.0,  4.2095), (-10.1627,0.0, -4.2095), (-4.2095, 0.0, -10.1627)
]


### 4 ###

circlePoints = [(10.0, 0.0,  0.0), (9.8481, 0.0,  1.7365), (9.3969, 0.0,  3.4202), (8.6603, 0.0,  5.0), (7.6604, 0.0,  6.4279), (6.4279, 0.0,  7.6604),
    (5.0,    0.0,  8.6603), (3.4202, 0.0,  9.3969), (1.7365, 0.0,  9.8481), (0.0,    0.0, 10.0), (-1.7365, 0.0,  9.8481), (-3.4202, 0.0,  9.3969),
    (-5.0,    0.0,  8.6603), (-6.4279, 0.0,  7.6604), (-7.6604, 0.0,  6.4279), (-8.6603, 0.0,  5.0), (-9.3969, 0.0,  3.4202), (-9.8481, 0.0,  1.7365),
    (-10.0,   0.0,  0.0), (-9.8481, 0.0, -1.7365), (-9.3969, 0.0, -3.4202), (-8.6602, 0.0, -5.0), (-7.6604, 0.0, -6.4279), (-6.4279, 0.0, -7.6604),
    (-5.0,    0.0, -8.6603), (-3.4202, 0.0, -9.3969), (-1.7365, 0.0, -9.8481), (0.0,     0.0, -10.0), (1.7365, 0.0, -9.8481), (3.4202, 0.0, -9.3969),
    (5.0,    0.0, -8.6602), (6.4279, 0.0, -7.6604), (7.6604, 0.0, -6.4279), (8.6603, 0.0, -5.0), (9.3969, 0.0, -3.4202), (9.8481, 0.0, -1.7365), (10.0,   0.0,  0.0)
]


### 5 ###

halfCirclePoints = [(10.0, 0.0,  0.0), (9.8481, 0.0,  1.7365), (9.3969, 0.0,  3.4202), (8.6603, 0.0,  5.0), (7.6604, 0.0,  6.4279), (6.4279, 0.0,  7.6604),
    (5.0,    0.0,  8.6603), (3.4202, 0.0,  9.3969), (1.7365, 0.0,  9.8481), (0.0,    0.0, 10.0), (-1.7365, 0.0,  9.8481), (-3.4202, 0.0,  9.3969),
    (-5.0,    0.0,  8.6603), (-6.4279, 0.0,  7.6604), (-7.6604, 0.0,  6.4279), (-8.6603, 0.0,  5.0), (-9.3969, 0.0,  3.4202), (-9.8481, 0.0,  1.7365),
    (-10.0,   0.0,  0.0), (10.0, 0.0,  0.0)
]


### 6 ###

pillPoints = [(10.0, 0.0, -10.0), (9.6593, 0.0, -12.5882), (8.6603, 0.0, -15.0), (7.0711, 0.0, -17.0711), (5.0, 0.0, -18.6603), (2.5882, 0.0, -19.6593),
    (0.0, 0.0, -20.0), (-2.5882, 0.0, -19.6593), (-5.0, 0.0, -18.6603), (-7.0711, 0.0, -17.0711), (-8.6603, 0.0, -15.0), (-9.6593, 0.0, -12.5882),
    (-10.0, 0.0, -10.0), (-10.0, 0.0, 10.0), (-9.6593, 0.0, 12.5882), (-8.6603, 0.0, 15.0), (-7.0711, 0.0, 17.0711), (-5.0, 0.0, 18.6603), (-2.5882, 0.0, 19.6593),
    (0.0, 0.0, 20.0), (2.5882, 0.0, 19.6593), (5.0, 0.0, 18.6603), (7.0711, 0.0, 17.0711), (8.6603, 0.0, 15.0), (9.6593, 0.0, 12.5882),
    (10.0, 0.0, 10.0), (10.0, 0.0, -10.0)
]


### 7 ###

circleStarPoints = [(0.0,  0.0,  17.5), (3.4202, 0.0,  9.3969), (5.0,    0.0,  8.6603), (6.4279, 0.0,  7.6604), (7.6604, 0.0,  6.4279), (8.6603, 0.0,  5.0),
    (9.3969, 0.0,  3.4202), (17.5,   0.0,  0.0), (9.3969, 0.0, -3.4202), (8.6603, 0.0, -5.0), (7.6604, 0.0, -6.4279), (6.4279, 0.0, -7.6604), (5.0,    0.0, -8.6602),
    (3.4202, 0.0, -9.3969), (0.0,    0.0, -17.5), (-3.4202, 0.0, -9.3969), (-5.0,    0.0, -8.6603), (-6.4279, 0.0, -7.6604), (-7.6604, 0.0, -6.4279),
    (-8.6603, 0.0, -5.0), (-9.3969, 0.0, -3.4202), (-17.5,   0.0,  0.0), (-9.3969, 0.0,  3.4202), (-8.6603, 0.0,  5.0), (-7.6604, 0.0,  6.4279),
    (-6.4279, 0.0,  7.6604), (-5.0,    0.0,  8.6603), (-3.4202, 0.0,  9.3969), (0.0,     0.0, 17.5)
]


### 8 ###

starPoints = [(0.0, 0.0, -17.5), (-5.0, 0.0, -5.0), (-17.5, 0.0, 0.0), (-5.0, 0.0, 5.0), (0.0, 0.0, 17.5), (5.0, 0.0, 5.0), (17.5, 0.0, 0.0),
    (5.0, 0.0, -5.0), (0.0, 0.0, -17.5)
]


### 9 ###

flowerPoints = [(-31.3263, 0.0, 0.0), (-38.0477, 0.0, 15.3592), (-32.3254, 0.0, 25.2707), (-15.6632, 0.0, 27.1294), (-5.7224, 0.0, 40.6299), (5.7224, 0.0, 40.6299),
    (15.6632, 0.0, 27.1294), (32.3254, 0.0, 25.2707), (38.0477, 0.0, 15.3592), (31.3264, 0.0, 0.0), (38.0477, 0.0, -15.3592), (32.3253, 0.0, -25.2707),
    (15.6632, 0.0, -27.1294), (5.7224, 0.0, -40.6299), (-5.7224, 0.0, -40.6299), (-15.6632, 0.0, -27.1294), (-32.3254, 0.0, -25.2707),
    (-38.0477, 0.0, -15.3592), (-31.3263, 0.0, 0.0)
]

###########- 3D SHAPES -###########
###################################

### 10 ###

locatorPoints = [( 0.0,  5.0,  0.0), ( 0.0, -5.0,  0.0), ( 0.0,  0.0,  0.0), ( 5.0,  0.0,  0.0), (-5.0,  0.0,  0.0), ( 0.0,  0.0,  0.0),
    ( 0.0,  0.0, -5.0), ( 0.0,  0.0,  5.0)
]


### 11 ###

pyramidPoints = [(0.0, -7.5, 10.0), (0.0, 7.5, 0.0), (0.0, -7.5, 10.0), (-10.0, -7.5, 0.0), (0.0, 7.5, 0.0), (-10.0, -7.5, 0.0), (0.0, -7.5, -10.0),
    (0.0, 7.5, 0.0), (0.0, -7.5, -10.0), (10.0, -7.5, 0.0), (0.0, 7.5, 0.0), (10.0, -7.5, 0.0), (0.0, -7.5, 10.0)
]


### 12 ###

diamondPoints = [(0.0, 15.0, 0.0), (0.0, 0.0, 10.0), (-10.0, 0.0, 0.0), (0.0, 15.0, 0.0), (-10.0, 0.0, 0.0), (0.0, 0.0, -10.0), (0.0, 15.0, 0.0), (0.0, 0.0, -10.0), 
    (10.0, 0.0, 0.0), (0.0, 15.0, 0.0), (10.0, 0.0, 0.0), (0.0, 0.0, 10.0), (0.0, -15.0, 0.0), (10.0, 0.0, 0.0), (0.0, 0.0, -10.0), (0.0, -15.0, 0.0), 
    (-10.0, 0.0, 0.0)
]


### 13 ###

cubePoints = [(10.0, 10.0, 10.0), (10.0, -10.0, 10.0), (-10.0, -10.0, 10.0), (-10.0, 10.0, 10.0), (10.0, 10.0, 10.0), (10.0, 10.0, -10.0), (10.0, -10.0, -10.0), 
    (10.0, -10.0, 10.0), (10.0, 10.0, 10.0), (10.0, 10.0, -10.0), (-10.0, 10.0, -10.0), (-10.0, -10.0, -10.0), (10.0, -10.0, -10.0), (10.0, 10.0, -10.0), 
    (-10.0, 10.0, -10.0), (-10.0, 10.0, 10.0), (-10.0, -10.0, 10.0), (-10.0, -10.0, -10.0), (-10.0, 10.0, -10.0)
]


### 14 ###

spherePoints = [(-10.0, 0.0, 0.0), (-9.7493, 0.0, 2.2252), (-9.0097, 0.0, 4.3388), (-7.8183, 0.0, 6.2349), (-6.2349, 0.0, 7.8183), (-4.3388, 0.0, 9.0097), 
    (-2.2252, 0.0, 9.7493), (0.0, 0.0, 10.0), (2.2252, 0.0, 9.7493), (4.3388, 0.0, 9.0097), (6.2349, 0.0, 7.8183), (7.8183, 0.0, 6.2349), (9.0097, 0.0, 4.3388), 
    (9.7493, 0.0, 2.2252), (10.0, 0.0, 0.0), (9.7493, 0.0, -2.2252), (9.0097, 0.0, -4.3388), (7.8183, 0.0, -6.2349), (6.2349, 0.0, -7.8183), (4.3388, 0.0, -9.0097), 
    (2.2252, 0.0, -9.7493), (0.0, 0.0, -10.0), (-2.2252, 0.0, -9.7493), (-4.3388, 0.0, -9.0097), (-6.2349, 0.0, -7.8183), (-7.8183, 0.0, -6.2349), 
    (-9.0097, 0.0, -4.3388), (-9.7493, 0.0, -2.2252), (-10.0, 0.0, 0.0), (-9.8769, 1.5643, 0.0), (-9.5106, 3.0902, 0.0), (-8.9101, 4.5399, 0.0), 
    (-8.0902, 5.8779, 0.0), (-7.0711, 7.0711, 0.0), (-5.8779, 8.0902, 0.0), (-4.5399, 8.9101, 0.0), (-3.0902, 9.5106, 0.0), (-1.5643, 9.8769, 0.0), 
    (0.0, 10.0, 0.0), (1.5643, 9.8769, 0.0), (3.0902, 9.5106, 0.0), (4.5399, 8.9101, 0.0), (5.8779, 8.0902, 0.0), (7.0711, 7.0711, 0.0), (8.0902, 5.8779, 0.0), 
    (8.9101, 4.5399, 0.0), (9.5106, 3.0902, 0.0), (9.8769, 1.5643, 0.0), (10.0, 0.0, 0.0), (9.8769, -1.5643, 0.0), (9.5106, -3.0902, 0.0), (8.9101, -4.5399, 0.0), 
    (8.0902, -5.8779, 0.0), (7.0711, -7.0711, 0.0), (5.8779, -8.0902, 0.0), (4.5399, -8.9101, 0.0), (3.0902, -9.5106, 0.0), (1.5643, -9.8769, 0.0), 
    (0.0, -10.0, 0.0), (-1.5643, -9.8769, 0.0), (-3.0902, -9.5106, 0.0), (-4.5399, -8.9101, 0.0), (-5.8779, -8.0902, 0.0), (-7.0711, -7.0711, 0.0), 
    (-8.0902, -5.8779, 0.0), (-8.9101, -4.5399, 0.0), (-9.5106, -3.0902, 0.0), (-9.8769, -1.5643, 0.0), (-10.0, 0.0, 0.0)
]


### 15 ###

halfCylinderPoints = [(0.0, 4.0, 12.0), (0.0, -4.0, 12.0), (2.0838, -4.0, 11.8177), (4.1042, -4.0, 11.2763), (6.0, -4.0, 10.3923), (7.7134, -4.0, 9.1925), 
    (9.1925, -4.0, 7.7135), (10.3923, -4.0, 6.0), (11.2763, -4.0, 4.1042), (11.8177, -4.0, 2.0838), (12.0, -4.0, 0.0), (11.8177, -4.0, -2.0838), 
    (11.2763, -4.0, -4.1042), (10.3923, -4.0, -6.0), (9.1925, -4.0, -7.7134), (7.7135, -4.0, -9.1925), (6.0, -4.0, -10.3923), (4.1042, -4.0, -11.2763), 
    (2.0838, -4.0, -11.8177), (0.0, -4.0, -12.0), (0.0, 4.0, -12.0), (2.0838, 4.0, -11.8177), (4.1042, 4.0, -11.2763), (6.0, 4.0, -10.3923), (7.7135, 4.0, -9.1925), 
    (9.1925, 4.0, -7.7134), (10.3923, 4.0, -6.0), (11.2763, 4.0, -4.1042), (11.8177, 4.0, -2.0838), (12.0, 4.0, 0.0), (11.8177, 4.0, 2.0838), (11.2763, 4.0, 4.1042), 
    (10.3923, 4.0, 6.0), (9.1925, 4.0, 7.7135), (7.7134, 4.0, 9.1925), (6.0, 4.0, 10.3923), (4.1042, 4.0, 11.2763), (2.0838, 4.0, 11.8177), (0.0, 4.0, 12.0)
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

skinnyArrowPoints = [(0.0,   0.0,  0.0), (0.0,   0.0, -25.0), (10.0,  0.0, -25.0), (0.0,   0.0, -40.0), (-10.0, 0.0, -25.0), (0.0,   0.0, -25.0)]


### 18 ###

fatArrowPoints = [(5.0, 0.0, 0.0), (5.0, 0.0, -25.0), (10.0, 0.0, -25.0), (0.0, 0.0, -40.0), (-10.0, 0.0, -25.0), (-5.0, 0.0, -25.0), (-5.0, 0.0, 0.0), 
    (5.0, 0.0, 0.0)
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

arrow3DPoints = [(0.0, 0.0, 0.0), (0.0, 25.0, 0.0), (5.0, 25.0, 5.0), (0.0, 36.8664, 0.0), (-5.0, 25.0, -5.0), (0.0, 25.0, 0.0), (-5.0, 25.0, 5.0), 
    (0.0, 36.8664, 0.0), (5.0, 25.0, -5.0), (0.0, 25.0, 0.0)
]


##########- PIN SHAPES -###########
###################################

### 24 ###

skinnyCirclePinPoints = [(0.0, 0.0, 0.0), (0.0, 0.0, 25.0), (0.0, 1.7365, 25.1519), (0.0, 3.4202, 25.6031), (0.0, 5.0, 26.3397), (0.0, 6.4279, 27.3396), 
    (0.0, 7.6604, 28.5721), (0.0, 8.6603, 30.0), (0.0, 9.3969, 31.5798), (0.0, 9.8481, 33.2635), (0.0, 10.0, 35.0), (0.0, 9.8481, 36.7365), (0.0, 9.3969, 38.4202), 
    (0.0, 8.6603, 40.0), (0.0, 7.6604, 41.4279), (0.0, 6.4279, 42.6604), (0.0, 5.0, 43.66), (0.0, 3.4202, 44.3969), (0.0, 1.7365, 44.8481), (0.0, 0.0, 45.0), 
    (0.0, -1.7365, 44.8481), (0.0, -3.4202, 44.3969), (0.0, -5.0, 43.66), (0.0, -6.4279, 42.6604), (0.0, -7.6604, 41.4279), (0.0, -8.6602, 40.0), 
    (0.0, -9.3969, 38.4202), (0.0, -9.8481, 36.7365), (0.0, -10.0, 35.0), (0.0, -9.8481, 33.2635), (0.0, -9.3969, 31.5798), (0.0, -8.6603, 30.0), 
    (0.0, -7.6604, 28.5721), (0.0, -6.4279, 27.3396), (0.0, -5.0, 26.3397), (0.0, -3.4202, 25.6031), (0.0, -1.7365, 25.1519), (0.0, 0.0, 25.0)
]


### 25 ###

fatCirclePinPoints = [(0.0, 0.0, 0.0), (0.0, 5.0, 26.3397), (0.0, 6.4279, 27.3396), (0.0, 7.6604, 28.5721), (0.0, 8.6603, 30.0), (0.0, 9.3969, 31.5798), 
    (0.0, 9.8481, 33.2635), (0.0, 10.0, 35.0), (0.0, 9.8481, 36.7365), (0.0, 9.3969, 38.4202), (0.0, 8.6603, 40.0), (0.0, 7.6604, 41.4279), (0.0, 6.4279, 42.6604), 
    (0.0, 5.0, 43.66), (0.0, 3.4202, 44.3969), (0.0, 1.7365, 44.8481), (0.0, 0.0, 45.0), (0.0, -1.7365, 44.8481), (0.0, -3.4202, 44.3969), (0.0, -5.0, 43.66), 
    (0.0, -6.4279, 42.6604), (0.0, -7.6604, 41.4279), (0.0, -8.6602, 40.0), (0.0, -9.3969, 38.4202), (0.0, -9.8481, 36.7365), (0.0, -10.0, 35.0), 
    (0.0, -9.8481, 33.2635), (0.0, -9.3969, 31.5798), (0.0, -8.6603, 30.0), (0.0, -7.6604, 28.5721), (0.0, -6.4279, 27.3396), (0.0, -5.0, 26.3397), (0.0, 0.0, 0.0)
]


### 26 ###

skinnySquarePinPoints = [( 0.0,  0.0, 0.0), ( 0.0,  0.0, 25.0), ( 0.0, -10.0, 25.0), ( 0.0, -10.0, 45.0), ( 0.0, 10.0, 45.0),
    ( 0.0, 10.0, 25.0), ( 0.0,  0.0, 25.0),
]


### 27 ###

fatSquarePinPoints = [( 0.0,  0.0, 0.0), ( 0.0,  -5.0, 25.0), ( 0.0, -10.0, 25.0), ( 0.0, -10.0, 45.0), ( 0.0, 10.0, 45.0), ( 0.0, 10.0, 25.0),
    ( 0.0,  5.0, 25.0), ( 0.0,  0.0, 0.0),
]


### 28 ###

locatorPinPoints = [(0.0, 0.0, 0.0), (0.0, 0.0, 45.0), (0.0, 0.0, 35.0), (0.0, 10.0, 35.0), (0.0, -10.0, 35.0), (0.0, 0.0, 35.0),
    (-10.0, 0.0, 35.0), (10.0, 0.0, 35.0)
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


###                                                 ###
#######################################################
##################- SHAPE LIBRARY -####################
#######################################################
###                                                 ###



######## RIG DETECTION ########

# Mixamo joints
mixamo_joints = ['Head', 'HeadTop_End', 'Hips', 'LeftArm', 'LeftFoot', 'LeftForeArm', 'LeftHand', 
                 'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandIndex4', 
                 'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftHandMiddle4', 
                 'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandPinky4', 
                 'LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3', 'LeftHandRing4', 
                 'LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3', 'LeftHandThumb4', 
                 'LeftLeg', 'LeftShoulder', 'LeftToeBase', 'LeftToe_End', 'LeftUpLeg', 
                 'Neck', 'RightArm', 'RightFoot', 'RightForeArm', 'RightHand', 
                 'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightHandIndex4', 
                 'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightHandMiddle4', 
                 'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3', 'RightHandPinky4', 
                 'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'RightHandRing4', 
                 'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3', 'RightHandThumb4', 
                 'RightLeg', 'RightShoulder', 'RightToeBase', 'RightToe_End', 'RightUpLeg', 
                 'Spine', 'Spine1', 'Spine2']

# MotionBuilder joints (normalize '_Head' to 'Head')
motionBuilder_joints = ['Hips', 'LeftArm', 'LeftFoot', 'LeftForeArm', 'LeftHand', 
                        'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftHandIndex4',
                        'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftHandMiddle4',
                        'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'LeftHandPinky4',
                        'LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3', 'LeftHandRing4',
                        'LeftHandThumb1', 'LeftHandThumb2', 'LeftHandThumb3', 'LeftHandThumb4',
                        'LeftLeg', 'LeftShoulder', 'LeftToeBase', 'LeftUpLeg', 'Neck', 
                        'RightArm', 'RightFoot', 'RightForeArm', 'RightHand',
                        'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightHandIndex4',
                        'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightHandMiddle4',
                        'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3', 'RightHandPinky4',
                        'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'RightHandRing4',
                        'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3', 'RightHandThumb4',
                        'RightLeg', 'RightShoulder', 'RightToeBase', 'RightUpLeg', 
                        'Spine', 'Spine1', 'Spine2', 'Head']

# Get joints from scene
scene_joints = cmds.ls(type='joint')

scene_set = set(scene_joints)

if scene_set == set(mixamo_joints):
    print("Scene matches Mixamo joints.")
elif scene_set == set(motionBuilder_joints):
    print("Scene matches MotionBuilder joints.")
else:
    print("!!! Scene joints do not match either Mixamo or MotionBuilder sets !!!")


######## SAVING ########

def set_controllers_to_default(*args):
    saved_controllers = DEFAULT_CONTROLLER_DATA.get("controllers", {})

    for ctl, settings in saved_controllers.items():
        if not cmds.objExists(ctl):
            print(f"[DEFAULT] Missing controller: {ctl}")
            continue

        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        if make_circle and settings["radius"] is not None:
            cmds.setAttr(make_circle[0] + ".radius", settings["radius"])

        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", settings["color"])
        cmds.setAttr(shape + ".lineWidth", settings["lineWidth"])


def save_controller_layout(*args):
    file_path = cmds.fileDialog2(
        fileFilter="JSON (*.json)",
        caption="Save Controller Layout",
        dialogStyle=2,
        fileMode=0
    )
    if not file_path:
        return
    file_path = file_path[0]

    controller_data = {"controllers": {}}

    controllers = cmds.ls("*_ctl")

    for ctl in controllers:
        # GET SHAPE
        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        # FIND CONSTRUCTION NODE (where radius lives)
        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        radius = None
        if make_circle:
            radius = cmds.getAttr(make_circle[0] + ".radius")

        # GET COLOR + WIDTH FROM SHAPE
        color = cmds.getAttr(shape + ".overrideColor")
        line_width = cmds.getAttr(shape + ".lineWidth")

        # Save to JSON structure
        controller_data["controllers"][ctl] = {
            "radius": radius,
            "color": color,
            "lineWidth": line_width
        }

    with open(file_path, "w") as f:
        json.dump(controller_data, f, indent=4)

    cmds.inViewMessage(amg="Controller layout <hl>saved</hl>.", pos="topCenter", fade=True)
    
######## IMPORTING ########
    
def load_controller_layout(*args):
    file_path = cmds.fileDialog2(
        fileFilter="JSON (*.json)",
        caption="Load Controller Layout",
        dialogStyle=2,
        fileMode=1
    )
    if not file_path:
        return
    file_path = file_path[0]

    with open(file_path, "r") as f:
        data = json.load(f)

    saved_controllers = data["controllers"]

    for ctl, settings in saved_controllers.items():
        if not cmds.objExists(ctl):
            print(f"[WARNING] Controller not found: {ctl} — skipping")
            continue

        shapes = cmds.listRelatives(ctl, s=True, type="nurbsCurve")
        if not shapes:
            continue
        shape = shapes[0]

        # FIND makeNurbCircle node to set radius
        history = cmds.listHistory(shape)
        make_circle = cmds.ls(history, type="makeNurbCircle")

        if settings["radius"] is not None and make_circle:
            cmds.setAttr(make_circle[0] + ".radius", settings["radius"])

        # Restore color
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", settings["color"])

        # Restore lineWidth
        cmds.setAttr(shape + ".lineWidth", settings["lineWidth"])

    cmds.inViewMessage(amg="Controller layout <hl>loaded</hl>.", pos="topCenter", fade=True)

    
######## LOCAL ROTATION AXIS OPTIONS ########

def enableAllTransAxis(*args):
    jointList = cmds.ls(type = 'joint')
    for i in jointList:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 1)


def disableAllTransAxis(*args):
    jointList = cmds.ls(type = 'joint')
    for i in jointList:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 0)


def selectedShowTransAxis(*args):
    jointSelection = cmds.ls(sl = True, type = 'joint')
    for i in jointSelection:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 1)


def selectedHideTransAxis(*args):
    jointSelection = cmds.ls(sl = True, type = 'joint')
    for i in jointSelection:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 0)


def allChildrenShowTransAxis(*args):
    jointSelection = cmds.ls(sl = True, type = 'joint')
    jointChildren = cmds.listRelatives(jointSelection, ad = True, type = 'joint')
    jointList = jointSelection + jointChildren
    for i in jointList:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 1)


def allChildrenHideTransAxis(*args):
    jointSelection = cmds.ls(sl = True, type = 'joint')
    jointChildren = cmds.listRelatives(jointSelection, ad = True, type = 'joint')
    jointList = jointSelection + jointChildren
    for i in jointList:
        setAxisDisplay = cmds.setAttr(i + '.displayLocalAxis', 0)

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
    
    newController = cmds.circle(n = ctlName + '_CON')
    
    offsetGroup = cmds.group(newController, n = 'OFFSET_' + ctlName)
    
    zeroGroup = cmds.group(offsetGroup, n = 'ZERO_' + ctlName)
    
def MZO(*args):

    sel = cmds.ls(selection=True)

    if not sel:
        cmds.warning("Select Zero group first.")
        return

    dupBranch = cmds.duplicate(sel[0])

    newScaleGrp = cmds.group(dupBranch[0], name='NEW_DUPLICATED_MZO_GROUP_RENAME_NOW')

    cmds.setAttr(newScaleGrp + '.scaleX', -1)

    
    
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

        shapeColor = cmds.getAttr(i + '.overrideColor')
        lineWidth = cmds.getAttr(i + '.lineWidth')

        newController = cmds.curve(d = 1, p = controllerShapes[shapeNumber], n = 'tempName')
        newControllerShape = cmds.listRelatives(newController, s = True)
        
        existingParent = cmds.listRelatives(i, p = True)
        print (existingParent)

        deleteOldShape = cmds.delete(i)
        replaceController = cmds.parent(newControllerShape, sel, s = True, r = True)
        deleteNewShell = cmds.delete(newController)

        enableColor = cmds.setAttr(newControllerShape[0] + '.overrideEnabled', 1)
        recolorShape = cmds.setAttr(newControllerShape[0] + '.overrideColor', shapeColor)
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
        
        shapeColor = cmds.getAttr(i + '.overrideColor')
        lineWidth = cmds.getAttr(i + '.lineWidth')

        newController = cmds.curve(d = 1, p = controllerShapes[shapeNumber], n = 'tempName')
        newControllerShape = cmds.listRelatives(newController, s = True)

        deleteOldShape = cmds.delete(i)
        replaceController = cmds.parent(newControllerShape, parent[0], s = True, r = True)
        deleteNewShell = cmds.delete(newController)

        enableColor = cmds.setAttr(newControllerShape[0] + '.overrideEnabled', 1)
        recolorShape = cmds.setAttr(newControllerShape[0] + '.overrideColor', shapeColor)
        rethickenLine = cmds.setAttr(newControllerShape[0] + '.lineWidth', lineWidth)
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


def get_slider_number(*args):
    return cmds.intField("colorValue", query=True, value=True)
    
def singleSelectColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    
    colorNumber = get_slider_number()
    for i in selShape:
        get_slider_number()
        isOverideEnabled = cmds.getAttr(i + '.overrideEnabled')
        if isOverideEnabled == 0:
            cmds.setAttr(i + '.overrideEnabled', 1)
        else: 
            pass
        cmds.setAttr(i + '.overrideColor', colorNumber)

def allChildrenColor(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    colorNumber = get_slider_number()
    
    for i in selShape:
        get_slider_number()
        isOverideEnabled = cmds.getAttr(i + '.overrideEnabled')
        if isOverideEnabled == 0:
            cmds.setAttr(i + '.overrideEnabled', 1)
        else: 
            pass
        cmds.setAttr(i + '.overrideColor', colorNumber)

maya_index_colors = {
    0: (0.0, 0.0, 0.1),
    1: (0.0, 0.0, 0.0),
    2: (0.3, 0.3, 0.3),
    3: (0.5, 0.5, 0.5),
    4: (0.5, 0.0, 0.0),
    5: (0.0, 0.0, 0.2),
    6: (0.0, 0.0, 1.0),
    7: (0.0, 0.2, 0.0),
    8: (0.1, 0.0, 0.2),
    9: (1.0, 0.0, 1.0),
    10: (0.5, 0.2, 0.0),
    11: (0.2, 0.1, 0.0),
    12: (0.7, 0.2, 0.0),
    13: (1.0, 0.0, 0.0),
    14: (0.0, 1.0, 0.0),
    15: (0.0, 0.2, 0.7),
    16: (1.0, 1.0, 1.0),
    17: (1.0, 1.0, 0.0),
    18: (0.0, 1.0, 1.0),
    19: (0.0, 1.0, 0.5),
    20: (1.0, 0.7, 0.7),
    21: (0.9, 0.7, 0.5),
    22: (1.0, 1.0, 0.5),
    23: (0.0, 0.6, 0.3),
    24: (0.6, 0.4, 0.2),
    25: (0.6, 0.6, 0.2),
    26: (0.4, 0.6, 0.2),
    27: (0.2, 0.6, 0.4),
    28: (0.2, 0.6, 0.6),
    29: (0.2, 0.4, 0.6),
}
        
def set_color_value(val, *args): 
    cmds.intField("colorValue", edit = True, value = val, minValue=0, maxValue=31, ed = False)
    if val in maya_index_colors:
        cmds.intField("colorValue", edit = True, bgc = maya_index_colors[val])
        
        
custom_outliner_colors = {
    0: (1.0, 0.0, 1.0),
    1: (1.0, 1.0, 0.0),
    2: (0.0, 0.0, 1.0),
    3: (1.0, 0.0, 0.0),
    4: (0.3, 0.3, 8.0),
    5: (0.0, 1.0, 0.0),
    6: (0.4, 0.4, 0.1),
    7: (0.0, 1.0, 1.0),
    8: (2.4, 0.6, 0.6),
    9: (0.78, 0.78, 0.78),
}
        
def set_float_color_value(val, *args):
    cmds.colorSliderGrp("outlinerColorValue", edit = True, rgb = custom_outliner_colors[val])
    if val in custom_outliner_colors:
        cmds.colorSliderGrp("outlinerColorValue", edit = True)
    

####### LINE WIDTH OPTIONS ########

def get_width_number(*args):
    return cmds.intField("widthValue", query=True, value=True)
    
def singleSelectWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel, s = True)
    widthNumber = get_width_number()
    for i in selShape:
        get_width_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)

def allChildrenWidth(*args):
    sel = cmds.ls(sl = True)
    selShape = cmds.listRelatives(sel[0], ad = True, type = 'shape')
    widthNumber = get_slider_number()
    for i in selShape:
        get_slider_number()
        cmds.setAttr(i + '.lineWidth', widthNumber)
        
        
####### LOCK ATTRIBUTE OPTIONS ########


trxAttrs = ['.translateX', '.translateY', '.translateZ']
rotAttrs = ['.rotateX', '.rotateY', '.rotateZ']
scaleAttrs = ['.scaleX', '.scaleY', '.scaleZ']
visAttrs = ['.visibility']


####### CONTROLLER BUILDER & ANIMATION KEYFRAME COPYING ########

def fk_controller_builder(*args):
    sel = cmds.ls(selection=True)
    if not sel:
        cmds.error("Select a root joint.")

    obj_list = cmds.listRelatives(sel[0], ad=True, typ='joint')
    obj_list.append(sel[0])  
    obj_list.reverse()       

    joint_ctl_map = {}

    for joint in obj_list:
        
        jntOX = cmds.getAttr(joint + '.jointOrientX')
        jntOY = cmds.getAttr(joint + '.jointOrientY')
        jntOZ = cmds.getAttr(joint + '.jointOrientZ')
        
        
        ctl = cmds.circle(n=joint + '_ctl', r=10, nr=[0, 1, 0])
        ctlshape = cmds.listRelatives(ctl[0], c=True, typ='shape')
        if ctlshape:
            cmds.setAttr(ctlshape[0] + '.overrideEnabled', 1)
            cmds.setAttr(ctlshape[0] + '.overrideColor', 17)

        ctl_grp = cmds.group(ctl, n=joint + '_animOffset')
        
        correction_grp = cmds.group(ctl_grp, n=joint + '_correctionOffset')

        cmds.matchTransform(correction_grp, joint, pos = True, rot = False)
        
        cmds.setAttr(correction_grp + '.rotateX', jntOX)
        cmds.setAttr(correction_grp + '.rotateY', jntOY)
        cmds.setAttr(correction_grp + '.rotateZ', jntOZ)

        parent_joint = cmds.listRelatives(joint, parent=True, type='joint')

        if parent_joint:
            parent_joint = parent_joint[0]
            if parent_joint in joint_ctl_map:
                cmds.parent(correction_grp, joint_ctl_map[parent_joint])

        joint_ctl_map[joint] = ctl[0]
        
        keyTransData = cmds.copyKey(joint, at = 'translate', o = 'keys')
        
        if keyTransData:
            pasteKeyData = cmds.pasteKey(correction_grp)
            
        keyRotData = cmds.copyKey(joint, at = 'rotate', o = 'keys')
        
        if keyRotData:
            pasteKeyData = cmds.pasteKey(ctl_grp)
            
        cmds.setAttr(correction_grp + '.rotateX', jntOX)
        cmds.setAttr(correction_grp + '.rotateY', jntOY)
        cmds.setAttr(correction_grp + '.rotateZ', jntOZ)
        
        cmds.setAttr(ctl_grp + '.translate', lock = True)
        cmds.setAttr(ctl_grp + '.rotate', lock = True)
        cmds.setAttr(ctl_grp + '.scale', lock = True)
        cmds.setAttr(ctl_grp + '.visibility', lock = True)
        
        cmds.setAttr(correction_grp + '.translate', lock = True)
        cmds.setAttr(correction_grp + '.rotate', lock = True)
        cmds.setAttr(correction_grp + '.scale', lock = True)
        cmds.setAttr(correction_grp + '.visibility', lock = True)
        
        cmds.lockNode(ctl)
        cmds.lockNode(ctl_grp)
        cmds.lockNode(correction_grp)
        
        
        cmds.cutKey(joint, cl = True)
        
        cmds.parentConstraint(ctl, joint, mo = True)
        
    ####### MOTION BUILDER OPTIONS #######
        
    set_controllers_to_default()
    
    if scene_set == set(motionBuilder_joints):

        arm_joints = [
        # Left arm
        "LeftShoulder_ctl", "LeftArm_ctl", "LeftForeArm_ctl", "LeftHand_ctl",
        "LeftHandIndex1_ctl", "LeftHandIndex2_ctl", "LeftHandIndex3_ctl", "LeftHandIndex4_ctl",
        "LeftHandMiddle1_ctl", "LeftHandMiddle2_ctl", "LeftHandMiddle3_ctl", "LeftHandMiddle4_ctl",
        "LeftHandPinky1_ctl", "LeftHandPinky2_ctl", "LeftHandPinky3_ctl", "LeftHandPinky4_ctl",
        "LeftHandRing1_ctl", "LeftHandRing2_ctl", "LeftHandRing3_ctl", "LeftHandRing4_ctl",
        "LeftHandThumb1_ctl", "LeftHandThumb2_ctl", "LeftHandThumb3_ctl", "LeftHandThumb4_ctl",
        
        # Right arm
        "RightShoulder_ctl", "RightArm_ctl", "RightForeArm_ctl", "RightHand_ctl",
        "RightHandIndex1_ctl", "RightHandIndex2_ctl", "RightHandIndex3_ctl", "RightHandIndex4_ctl",
        "RightHandMiddle1_ctl", "RightHandMiddle2_ctl", "RightHandMiddle3_ctl", "RightHandMiddle4_ctl",
        "RightHandPinky1_ctl", "RightHandPinky2_ctl", "RightHandPinky3_ctl", "RightHandPinky4_ctl",
        "RightHandRing1_ctl", "RightHandRing2_ctl", "RightHandRing3_ctl", "RightHandRing4_ctl",
        "RightHandThumb1_ctl", "RightHandThumb2_ctl", "RightHandThumb3_ctl", "RightHandThumb4_ctl"
    ]
        for curve in arm_joints:
    # Rotate Y by 90 degrees
            cmds.rotate(90, 90, 0, curve + ".cv[*]", r=True)
    
####### CONTROLLER DECONSTRUCT & ANIMATION KEYFRAME COPYING ########

def fk_controller_deconstructor(*args):
    """
    Deletes FK controllers and restores animation back to joints.
    Assumes naming convention from fk_controller_builder().
    """
    
    controllers = cmds.ls("*_ctl", type="transform")
    
    for ctl in controllers:
        
        if not cmds.objExists(ctl):
            continue
        
        cmds.lockNode(ctl, lock=False)
        
        
        cmds.setAttr(ctl + '.translate', lock = False)
        cmds.setAttr(ctl + '.rotate', lock = False)
        cmds.setAttr(ctl + '.scale', lock = False)
        cmds.setAttr(ctl + '.visibility', lock = False)
        
        # Derive joint name
        joint = ctl.replace("_ctl", "")
        
        if not cmds.objExists(joint):
            continue
        
        anim_grp = joint + "_animOffset"
        
        cmds.lockNode(anim_grp, lock=False)
        
        cmds.setAttr(anim_grp + '.translate', lock=False)
        cmds.setAttr(anim_grp + '.rotate', lock=False)
        cmds.setAttr(anim_grp + '.scale', lock=False)
        cmds.setAttr(anim_grp + '.visibility', lock=False)
            
            
        correction_grp = joint + "_correctionOffset"
        
        cmds.lockNode(correction_grp, lock=False)
        
        cmds.setAttr(correction_grp + '.translate', lock=False)
        cmds.setAttr(correction_grp + '.rotate', lock=False)
        cmds.setAttr(correction_grp + '.scale', lock=False)
        cmds.setAttr(correction_grp + '.visibility', lock=False)
            
        constraints = cmds.listConnections(joint, type="parentConstraint")
        if constraints:
            cmds.delete(constraints)
        
        keyTransData = cmds.copyKey(correction_grp, at = 'translate', o = 'keys')
        
        if keyTransData:
            pasteKeyData = cmds.pasteKey(joint)
            
        keyRotData = cmds.copyKey(anim_grp, at = 'rotate', o = 'keys')
        
        if keyRotData:
            pasteKeyData = cmds.pasteKey(joint)
        
    
    all_joints = cmds.ls(type="joint")    

    root_joints = []

    for jnt in all_joints:
        parent = cmds.listRelatives(jnt, parent=True)

        # If no parent OR parent is not a joint → this is a skeleton root
        if not parent or cmds.nodeType(parent[0]) != "joint":
            root_joints.append(jnt)

    print(root_joints)
    
    root_joint = root_joints[0]  # assuming single root
    correction_root = root_joint + "_correctionOffset"

    
    cmds.delete(correction_root)
    
    
    cmds.inViewMessage(
        amg="Controllers <hl>removed</hl> and animation restored to joints.",
        pos="topCenter",
        fade=True
    )

    
        
######## WINDOW & UI ########

def mixamo_anim_editor():
    
    winName = "Karoly Controlly Editor"
    
    if cmds.workspaceControl(winName, exists=True):
        cmds.deleteUI(winName)
        print('Deleted old Mixamo Editor UI')

    window = cmds.workspaceControl(winName, label = "Karoly Controlly Editor", fl = True, retain = False, ih = 800, w = 320, iw = 320, wp='fixed', rsw = 320)
    
    scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16, w = 320)
    
    #scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=50)
    cmds.columnLayout( adjustableColumn=True )
    #cmds.text( label='Select HIPS joint', align='center', fn = 'boldLabelFont', w = 20, h = 30)
    #cmds.button( label='Build FK Controllers', command = fk_controller_builder, w = 200)
    cmds.separator(st = 'none', h = 10)
    cmds.text( label='LOCAL ROTATION AXIS', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(st = 'none', h = 10)
    
    #####
    
    cmds.rowLayout(numberOfColumns=5)
    
    #cmds.separator(hr = False, h = 23, w = 50, vis = False)
    cmds.button(label="Show All", w = 70, bgc=[0.5, 0.5, 1], command=enableAllTransAxis)
    cmds.separator(hr = False, h = 23, w = 12, st = 'out')
    cmds.button(label="Show Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=selectedShowTransAxis)
    cmds.button(label="Show All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=allChildrenShowTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=5)
    
    #cmds.separator(hr = False, h = 23, w = 50, vis = False)
    cmds.button(label="Hide All", w = 70, bgc=[0.5, 0.5, 1], command=disableAllTransAxis)
    cmds.separator(hr = False, h = 23, w = 12, st = 'out')
    cmds.button(label="Hide Selected", w = 100, bgc=[0.3, 0.8, 0.9], command=selectedHideTransAxis)
    cmds.button(label="Hide All Children", w = 100, bgc=[0.3, 0.8, 0.7], command=allChildrenHideTransAxis)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='OUTLINER SETTINGS', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=4)

    cmds.text( label='Color', align='left', w = 50 )
    cmds.colorSliderGrp('outlinerColorValue', label='', rgb=(0.78, 0.78, 0.78), cl3 = ('left', 'left', 'left'), cw3=(1, 80, 72) )
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = selectedChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenChangeOutlinerColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )    
    
    

    #####
    
    #cmds.setParent( '..' )
    
    #cmds.separator(st = 'none', h = 2)
    
    #cmds.rowLayout(numberOfColumns=5)
    
    #cmds.text( label='Reset Colors', align='left', w = 100)
    #cmds.button(label="Reset All", w = 79, bgc=[0.5, 0.5, 1], command=allSceneResetOutlinerColor)
    #cmds.button(label="Undo Reset", w = 79, bgc=[0.5, 0.6, 1], command=allSceneUndoResetOutlinerColor)
    #cmds.button(label="Selected", w = 70, bgc=[0.3, 0.8, 0.9], command=selectedResetOutlinerColor)
    #cmds.button(label="All Children", w = 70, bgc=[0.3, 0.8, 0.7], command=allChildrenResetOutlinerColors)
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 55)
    
    cmds.button(label='OG', w = 35, bgc=[0.78, 0.78, 0.78], command=lambda x: set_float_color_value(9))
    cmds.button(label='1', w = 35, bgc=[1.0, 1.0, 0.0], command=lambda x: set_float_color_value(1))
    cmds.button(label='3', w = 35, bgc=[0.0, 0.0, 1.0], command=lambda x: set_float_color_value(2))
    cmds.button(label='5', w = 35, bgc=[1.0, 0.0, 0.0], command=lambda x: set_float_color_value(3))
    cmds.button(label='7', w = 35, bgc=[0.0, 1.0, 0.0], command=lambda x: set_float_color_value(5)) 
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 2)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 55)
    
    cmds.button(label='0', w = 35, bgc=[1.0, 0.0, 1.0], command=lambda x: set_float_color_value(0))
    cmds.button(label='2', w = 35, bgc=[0.4, 0.4, 0.1], command=lambda x: set_float_color_value(6))
    cmds.button(label='4', w = 35, bgc=[0.0, 1.0, 1.0], command=lambda x: set_float_color_value(7))
    cmds.button(label='6', w = 35, bgc=[2.4, 0.6, 0.6], command=lambda x: set_float_color_value(8))
    cmds.button(label='8', w = 35, bgc=[0.3, 0.3, 8.0], command=lambda x: set_float_color_value(4)) 
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='CONTROLLER CREATOR', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=2, columnWidth=(1, 49))


    cmds.text( label='Name', align='left', w = 50 )
    cmds.textField("controllerNameField", w = 200, pht = 'Enter Controller Name')
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 43, w = 60, vis = False)
    #cmds.button(label="Create Controller", w = 100, bgc=[0.9, 0.4, 0.3], command=createJustController)
    cmds.button(label="ZO", w = 70, bgc=[0.9, 0.5, 0.3], command=createZeroOffsetController)
    cmds.button(label="MZO", w = 70, bgc=[0.9, 0.6, 0.3], command=MZO)
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='CONTROLLER SETTINGS', align='center', fn = 'boldLabelFont', w = 20, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(st = 'none', h = 10)

    cmds.rowLayout(numberOfColumns=3) 

    cmds.text( label='Scale', align='left', w = 50 )
    cmds.floatSliderGrp("scaleValue", value=1.0, minValue=0.1, maxValue=2, pre = 1, field = True, cw2 = [50, 100]) 
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectScale, w = 40, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenScale, w = 10, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )   
    
    
    #cmds.button(label="Selected", command = singleSelectScale, w = 70, bgc=[0.3, 0.8, 0.9])
    #cmds.button(label="All Children", command = allChildrenScale, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####

    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 10, w = 40, st = 'none')
    cmds.separator(hr = True, h = 1, w = 200, st = 'single')
    cmds.setParent( '..' )
    
    cmds.separator(st='none', h=1)

    cmds.rowLayout(numberOfColumns=4)

    cmds.text(label='Shape', align='left', w=50)

    cmds.optionMenu("shapeMenu", w=158)


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
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 10, w = 40, st = 'none')
    cmds.separator(hr = True, h = 1, w = 200, st = 'single')
    cmds.setParent( '..' )

    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st='none', h=1)
    
    cmds.rowLayout(numberOfColumns=26) 

    cmds.text( label='Orient', align='left', w = 52 )
    
    cmds.columnLayout(adjustableColumn=True, w=52)
    cmds.rowLayout(numberOfColumns=2) 
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', command =  rotateXCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateXclockwise', command = rotateXClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='X:', align='left', w = 10 )
    cmds.intField("XValue", value=0, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.columnLayout(adjustableColumn=True, w=50)
    cmds.rowLayout(numberOfColumns=2) 
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateYcounterclockwise', command =  rotateYCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateYclockwise', command =  rotateYClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='Y:', align='left', w = 10 )
    cmds.intField("YValue", value=0, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.columnLayout(adjustableColumn=True, w=50)
    cmds.rowLayout(numberOfColumns=2) 
    cmds.iconTextButton( style='iconOnly', image1='rotateUVccw.png', label='rotateZcounterclockwise', command =  rotateZCounterClockwise)
    cmds.iconTextButton( style='iconOnly', image1='rotateUVcw.png', label='rotateZclockwise',  command =  rotateZClockwise)
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2) 
    cmds.text( label='Z:', align='left', w = 10 )
    cmds.intField("ZValue", value=0, w = 40)
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectOrient, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenOrient, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )

    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 18, w = 40, st = 'none')
    cmds.separator(hr = True, h = 10, w = 200, st = 'single')


    
    #####
    
    cmds.setParent( '..' )

    cmds.separator(st = 'none', h = 1)

    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Color', align='left', w = 50 )
    
    
    cmds.intField("colorValue", value=17, minValue=0, maxValue=31, ed = False, bgc = [1.0, 1.0, 0.0], w=160) 
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectShape, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenShape, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )   
    #cmds.button(label="Selected", command = singleSelectColor, w = 70, bgc=[0.3, 0.8, 0.9])
    #cmds.button(label="All Children", command = allChildrenColor, w = 70, bgc=[0.3, 0.8, 0.7])
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 17)
    
    cmds.button(label='OG', w = 35, bgc=[0.78, 0.78, 0.78], command=lambda x: set_color_value(0))
    cmds.button(label='1', w = 35, bgc=[1.0, 1.0, 0.0], command=lambda x: set_color_value(17))
    cmds.button(label='3', w = 35, bgc=[0.0, 0.0, 1.0], command=lambda x: set_color_value(6))
    cmds.button(label='5', w = 35, bgc=[1.0, 0.0, 0.0], command=lambda x: set_color_value(13))
    cmds.button(label='7', w = 35, bgc=[0.0, 1.0, 0.0], command=lambda x: set_color_value(14)) 
    
    #cmds.button(label='0', w = 35, bgc=[0.0, 0.0, 0.1], command=lambda x: set_color_value(0))
    #cmds.button(label='1', w = 35, bgc=[0.0, 0.0, 0.0], command=lambda x: set_color_value(1))
    #cmds.button(label='2', w = 35, bgc=[0.3, 0.3, 0.3], command=lambda x: set_color_value(2))
    #cmds.button(label='3', w = 35, bgc=[0.5, 0.5, 0.5], command=lambda x: set_color_value(3))
    #cmds.button(label='4', w = 35, bgc=[0.5, 0.0, 0.0], command=lambda x: set_color_value(4)) 
    #cmds.button(label='5', w = 35, bgc=[0.0, 0.0, 0.2], command=lambda x: set_color_value(5))
    #cmds.button(label='6', w = 35, bgc=[0.0, 0.0, 1.0], command=lambda x: set_color_value(6))
    #cmds.button(label='7', w = 35, bgc=[0.0, 0.2, 0.0], command=lambda x: set_color_value(7))
    #cmds.button(label='8', w = 35, bgc=[0.1, 0.0, 0.2], command=lambda x: set_color_value(8))
    #cmds.button(label='9', w = 35, bgc=[1.0, 0.0, 1.0], command=lambda x: set_color_value(9))
    
    #####
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 1)
    
    cmds.rowLayout(numberOfColumns=11)
    
    cmds.separator(st = 'none', w = 17)
    
    cmds.button(label='0', w = 35, bgc=[1.0, 0.0, 1.0], command=lambda x: set_color_value(9))
    cmds.button(label='2', w = 35, bgc=[0.4, 0.4, 0.1], command=lambda x: set_color_value(25))
    cmds.button(label='4', w = 35, bgc=[0.0, 1.0, 1.0], command=lambda x: set_color_value(18))
    cmds.button(label='6', w = 35, bgc=[2.4, 0.6, 0.6], command=lambda x: set_color_value(20))
    cmds.button(label='8', w = 35, bgc=[0.3, 0.3, 8.0], command=lambda x: set_color_value(29)) 
    
    #cmds.button(label='10', w = 35, bgc=[0.5, 0.2, 0.0], command=lambda x: set_color_value(10))
    #cmds.button(label='11', w = 35, bgc=[0.2, 0.1, 0.0], command=lambda x: set_color_value(11))
    #cmds.button(label='12', w = 35, bgc=[0.7, 0.2, 0.0], command=lambda x: set_color_value(12))
    #cmds.button(label='13', w = 35, bgc=[1.0, 0.0, 0.0], command=lambda x: set_color_value(13))
    #cmds.button(label='14', w = 35, bgc=[0.0, 1.0, 0.0], command=lambda x: set_color_value(14))
    #cmds.button(label='15', w = 35, bgc=[0.0, 0.2, 0.7], command=lambda x: set_color_value(15))
    #cmds.button(label='16', w = 35, bgc=[1.0, 1.0, 1.0], command=lambda x: set_color_value(16))
    #cmds.button(label='17', w = 35, bgc=[1.0, 1.0, 0.0], command=lambda x: set_color_value(17))
    #cmds.button(label='18', w = 35, bgc=[0.0, 1.0, 1.0], command=lambda x: set_color_value(18))
    #cmds.button(label='19', w = 35, bgc=[0.0, 1.0, 0.5], command=lambda x: set_color_value(19))
    
    #####
    
    #cmds.setParent( '..' )
    
    #cmds.separator(st = 'none', h = 1)
    
    #cmds.rowLayout(numberOfColumns=11)
    
    #cmds.separator(st = 'none', w = 17)
    
    #cmds.button(label='20', w = 35, bgc=[1.0, 0.7, 0.7], command=lambda x: set_color_value(20))
    #cmds.button(label='21', w = 35, bgc=[0.9, 0.7, 0.5], command=lambda x: set_color_value(21))
    #cmds.button(label='22', w = 35, bgc=[1.0, 1.0, 0.5], command=lambda x: set_color_value(22))
    #cmds.button(label='23', w = 35, bgc=[0.0, 0.6, 0.3], command=lambda x: set_color_value(23))
    #cmds.button(label='24', w = 35, bgc=[0.6, 0.4, 0.2], command=lambda x: set_color_value(24))
    #cmds.button(label='25', w = 35, bgc=[0.6, 0.6, 0.2], command=lambda x: set_color_value(25))
    #cmds.button(label='26', w = 35, bgc=[0.4, 0.6, 0.2], command=lambda x: set_color_value(26))
    #cmds.button(label='27', w = 35, bgc=[0.2, 0.6, 0.4], command=lambda x: set_color_value(27))
    #cmds.button(label='28', w = 35, bgc=[0.2, 0.6, 0.6], command=lambda x: set_color_value(28))
    #cmds.button(label='29', w = 35, bgc=[0.2, 0.4, 0.6], command=lambda x: set_color_value(29))
    
    
    ###
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 18, w = 40, st = 'none')
    cmds.separator(hr = True, h = 10, w = 200, st = 'single')

    cmds.setParent( '..' )
    
    cmds.separator(st = 'none', h = 11)

    
    cmds.rowLayout(numberOfColumns=4) 

    cmds.text( label='Thickness', align='left', w = 50 )
    cmds.intField("widthValue", value=-1, minValue=-1, maxValue=10, w=160) 
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    
    cmds.button(label="Selected", command = singleSelectWidth, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.separator(st='none', h=3)
    cmds.button(label="All Children", command = allChildrenWidth, w = 70, bgc=[0.3, 0.8, 0.7])
    
    cmds.setParent( '..' )  
    
    #cmds.button(label="Selected", command = singleSelectWidth, w = 70, bgc=[0.3, 0.8, 0.9])
    #cmds.button(label="All Children", command = allChildrenWidth, w = 70, bgc=[0.3, 0.8, 0.7])
    
    
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
    
    cmds.setParent( '..' )
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.text( label='ATTRIBUTE LOCKER', align='center', fn = 'boldLabelFont', w = 290, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(st = 'none', h = 10)
    

    ##############
    
    cmds.rowLayout(numberOfColumns=13) 
    
    cmds.text( label='1', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    
    cmds.separator(hr = False, h = 18, w = 20, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=100)
    cmds.rowLayout(numberOfColumns=3)
    cmds.text(label = 'Translation: ')
    transAttrBox = cmds.checkBox(label = '')
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4) 
    cmds.separator(hr = False, h = 18, w = 10, st = 'none')
    cmds.text(label = 'Rotation: ')
    rotAttrBox = cmds.checkBox(label = '')
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    cmds.columnLayout(adjustableColumn=True, w=100)
    cmds.rowLayout(numberOfColumns=3)
    cmds.separator(hr = False, h = 18, w = 15, st = 'none')
    cmds.text(label = 'Scale: ')
    scaleAttrBox = cmds.checkBox(label = '')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=3)
    cmds.text(label = 'Visibility: ')
    visAttrBox = cmds.checkBox(label = '')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 18, w = 40, st = 'none')
    cmds.separator(hr = True, h = 10, w = 200, st = 'single')
    cmds.setParent( '..' )
    

    
    ##############
    
    cmds.rowLayout(numberOfColumns=13) 
    
    cmds.text( label='2', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    
    cmds.separator(hr = False, h = 18, w = 20, st = 'none')
    
    cmds.columnLayout(adjustableColumn=True, w=70)
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator(hr = False, h = 18, w = 2, st = 'none')
    cmds.text(label = 'Lock: ')
    lockAttrBox = cmds.checkBox(label = '', cc = onLockChanged)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    
    cmds.rowLayout(numberOfColumns=4) 
    cmds.separator(hr = False, h = 18, w = 1, st = 'none')
    cmds.text(label = 'Hide: ')
    hideAttrBox = cmds.checkBox(label = '', cc = onHideChanged)
    cmds.separator(hr = False, h = 18, w = 20, st = 'out')
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    
    cmds.columnLayout(adjustableColumn=True, w=200)
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
    
    cmds.rowLayout(numberOfColumns=2, w=200, columnAlign=(1, 'center'))
    cmds.separator(hr = False, h = 18, w = 40, st = 'none')
    cmds.separator(hr = True, h = 10, w = 200, st = 'single')
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
        
        
            
#    def attrOption(*args):
#        checkLockBox = cmds.checkBox(lockAttrBox, q=True, v=True)
#        checkHideBox = cmds.checkBox(hideAttrBox, q=True, v=True)
#        checkUnlockUnhideBox = cmds.checkBox(unlockUnhideAttrBox, q=True, v=True)
#        checkUnhideBox = cmds.checkBox(unhideAttrBox, q=True, v=True)
        
#        if checkLockBox:
#            print ("Lock is checked")
#        else: 
#            pass
            
#        if checkHideBox:
#            print ("Hide is checked")
#        else:
#            pass
        
#        if checkUnlockUnhideBox:
#            print ("Unlock & Unhide is checked")
#        else:
#            pass
            
#        if checkUnhideBox:
#            print ("Unhide is checked")
#        else:
#            pass
        
    cmds.rowLayout(numberOfColumns=4) 
    cmds.text( label='3', align='center', fn = 'boldLabelFont', w = 25, h = 25, bgc=[0.2, 0.2, 0.2])
    cmds.separator(hr = False, h = 18, w = 35, st = 'none')
    cmds.button(label="Selected", command = singleControllerAttrBoxes, w = 70, bgc=[0.3, 0.8, 0.9])
    cmds.button(label="All Children", command = allChildrenControllerAttrBoxes, w = 70, bgc=[0.3, 0.8, 0.7])
    
    
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
    
    cmds.separator(st = 'in', h = 23)
    
    cmds.separator(st = 'none', h = 10)
    
    cmds.rowLayout(numberOfColumns=3)
    
    cmds.separator(hr = False, h = 18, w = 100, st = 'out')
    
    cmds.text(label = 'GD76 Roman Karoly', align = 'left', w = 150, fn = 'obliqueLabelFont')
    
    cmds.separator(hr = False, h = 18, w = 10, st = 'out')
    
    cmds.setParent( '..' )

    
    cmds.rowLayout(numberOfColumns=3)
    
    cmds.separator(hr = False, h = 18, w = 100, st = 'out')
    
    cmds.text(label = '      Version 1.0', align = 'left', w = 150, fn = 'obliqueLabelFont')
    
    cmds.separator(hr = False, h = 18, w = 10, st = 'out')
    #cmds.dockControl( area='left', content=window )

        
    #cmds.showWindow( window )