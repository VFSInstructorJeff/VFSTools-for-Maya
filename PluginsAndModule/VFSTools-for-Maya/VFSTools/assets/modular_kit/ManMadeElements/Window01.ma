//Maya ASCII 2026 scene
//Name: Window01.ma
//Last modified: Thu, Feb 19, 2026 12:47:30 PM
//Codeset: 1252
requires maya "2026";
requires "stereoCamera" "10.0";
requires "mtoa" "5.5.4.2";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2026";
fileInfo "version" "2026";
fileInfo "cutIdentifier" "202510291147-60ec9eda33";
fileInfo "osv" "Windows 11 Education v2009 (Build: 26200)";
fileInfo "UUID" "EB37F056-4849-7EA5-EC04-DE928CDFC3FD";
fileInfo "license" "education";
createNode transform -n "Window01_grp";
	rename -uid "8DD99BC6-49EA-9D3A-D078-3BB36092D2D0";
createNode transform -n "Window01" -p "Window01_grp";
	rename -uid "F556CD27-4353-D3C6-9138-FA984090F858";
	setAttr ".rp" -type "double3" 0 0 6.103515625e-05 ;
	setAttr ".sp" -type "double3" 0 0 6.103515625e-05 ;
createNode mesh -n "Window01Shape" -p "Window01";
	rename -uid "802015DE-4BFC-E241-D321-D082941FC8F2";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:47]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[48:53]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 6 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "back";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 9 "f[2]" "f[8]" "f[14]" "f[20]" "f[26]" "f[32]" "f[38]" "f[44]" "f[50]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottom";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 9 "f[3]" "f[9]" "f[15]" "f[21]" "f[27]" "f[33]" "f[39]" "f[45]" "f[51]";
	setAttr ".gtag[2].gtagnm" -type "string" "front";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 9 "f[0]" "f[6]" "f[12]" "f[18]" "f[24]" "f[30]" "f[36]" "f[42]" "f[48]";
	setAttr ".gtag[3].gtagnm" -type "string" "left";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 9 "f[5]" "f[11]" "f[17]" "f[23]" "f[29]" "f[35]" "f[41]" "f[47]" "f[53]";
	setAttr ".gtag[4].gtagnm" -type "string" "right";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 9 "f[4]" "f[10]" "f[16]" "f[22]" "f[28]" "f[34]" "f[40]" "f[46]" "f[52]";
	setAttr ".gtag[5].gtagnm" -type "string" "top";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 9 "f[1]" "f[7]" "f[13]" "f[19]" "f[25]" "f[31]" "f[37]" "f[43]" "f[49]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 216 ".uvst[0].uvsp[0:215]" -type "float2" 0.26999998 2.10495281
		 0.23000002 2.10495281 0.23000002 1.89495254 0.26999998 1.89495254 0.22999999 1.89495277
		 0.27000001 1.89495277 0.27000001 2.10495257 0.22999999 2.10495257 0.21000001 3.49995279
		 0 3.49995279 0 0.49995282 0.21000001 0.49995282 0.46000001 0.49995282 0.46000001
		 3.49995279 0.25000003 3.49995279 0.25000003 0.49995282 0.5 3.49995279 0.5 0.49995282
		 0.25000003 3.49995279 0.25000003 0.49995282 0.21000001 3.49995279 0.21000001 0.49995282
		 0.46000001 3.49995279 0.46000001 0.49995282 0.28999996 3.46005726 0.28999996 0.54005748
		 0.31999996 0.54005748 0.31999996 3.46005726 0 3.46005726 0 0.5400576 0.13000001 0.5400576
		 0.13000001 3.46005726 0.13000001 3.46005726 0.13000001 0.5400576 0.15999998 0.54005754
		 0.15999998 3.46005726 0.15999998 3.46005726 0.15999998 0.54005754 0.28999996 0.54005748
		 0.28999996 3.46005726 0.14499997 2.065057516 0.14499997 1.93505752 0.17499997 1.93505752
		 0.17499997 2.065057516 0.14499997 2.065057516 0.14499997 1.93505752 0.175 1.93505752
		 0.175 2.065057516 0.5 3.49995279 0.46000001 3.49995279 0.46000001 0.49995282 0.5
		 0.49995282 0.21000001 3.49995279 0 3.49995279 0 0.49995282 0.21000001 0.49995282
		 0.25000003 3.49995279 0.21000001 3.49995279 0.21000001 0.49995282 0.25000003 0.49995282
		 0.46000001 0.49995282 0.46000001 3.49995279 0.25000003 3.49995279 0.25000003 0.49995282
		 0.26999998 2.10495281 0.23000002 2.10495281 0.23000002 1.89495254 0.26999998 1.89495254
		 0.22999999 1.89495277 0.27000001 1.89495277 0.27000001 2.10495257 0.22999999 2.10495257
		 0.28999996 3.46005726 0.28999996 0.54005748 0.31999996 0.54005748 0.31999996 3.46005726
		 0 3.46005726 0 0.5400576 0.13000001 0.5400576 0.13000001 3.46005726 0.13000001 3.46005726
		 0.13000001 0.5400576 0.15999998 0.54005754 0.15999998 3.46005726 0.15999998 3.46005726
		 0.15999998 0.54005754 0.28999996 0.54005748 0.28999996 3.46005726 0.14499997 2.065057516
		 0.14499997 1.93505752 0.17499997 1.93505752 0.17499997 2.065057516 0.14499997 2.065057516
		 0.14499997 1.93505752 0.175 1.93505752 0.175 2.065057516 0.45999992 0.28888965 0.50000018
		 0.28888965 0.49999994 1.95888948 0.4599998 1.95888948 0.25 0.28888965 0.45999992
		 0.28888965 0.4599998 1.95888948 0.24999996 1.95888948 0.20999986 0.28888965 0.25
		 0.28888965 0.24999996 1.95888948 0.20999977 1.95888948 0.20999977 1.95888948 -1.4901161e-07
		 1.95888925 0 0.28888965 0.20999986 0.28888965 0.13097441 1.22888982 0.090974391 1.22888982
		 0.090974391 1.018889546 0.13097441 1.018889546 0.090974331 1.018889546 0.13097453
		 1.018889546 0.13097453 1.22888982 0.090974331 1.22888982 0.15865201 0.31854236 0.15865219
		 1.92854166 0.12865219 1.92854166 0.12865213 0.31854236 0.12865213 0.31854236 0.12865219
		 1.92854166 -0.0013477914 1.92854166 -0.001347851 0.31854236 0.31865194 0.31854236
		 0.318652 1.92854166 0.28865215 1.92854166 0.28865197 0.31854236 0.28865197 0.31854236
		 0.28865215 1.92854166 0.15865219 1.92854166 0.15865201 0.31854236 0.018652726 1.18853998
		 0.018652726 1.058544278 0.048651867 1.058544278 0.048651867 1.18853998 0.018652786
		 1.18853998 0.018652786 1.058544278 0.048651807 1.058544278 0.048651807 1.18853998
		 0.15865201 0.31854236 0.15865219 1.92854166 0.12865219 1.92854166 0.12865213 0.31854236
		 0.12865213 0.31854236 0.12865219 1.92854166 -0.0013477914 1.92854166 -0.001347851
		 0.31854236 0.31865194 0.31854236 0.318652 1.92854166 0.28865215 1.92854166 0.28865197
		 0.31854236 0.28865197 0.31854236 0.28865215 1.92854166 0.15865219 1.92854166 0.15865201
		 0.31854236 0.018652726 1.18853998 0.018652726 1.058544278 0.048651867 1.058544278
		 0.048651867 1.18853998 0.018652786 1.18853998 0.018652786 1.058544278 0.048651807
		 1.058544278 0.048651807 1.18853998 0.45999992 0.28888965 0.50000018 0.28888965 0.49999994
		 1.95888948 0.4599998 1.95888948 0.25 0.28888965 0.45999992 0.28888965 0.4599998 1.95888948
		 0.24999996 1.95888948 0.20999986 0.28888965 0.25 0.28888965 0.24999996 1.95888948
		 0.20999977 1.95888948 0.20999977 1.95888948 -1.4901161e-07 1.95888925 0 0.28888965
		 0.20999986 0.28888965 0.13097441 1.22888982 0.090974391 1.22888982 0.090974391 1.018889546
		 0.13097441 1.018889546 0.090974331 1.018889546 0.13097453 1.018889546 0.13097453
		 1.22888982 0.090974331 1.22888982 3.85959315 3.29362726 3.8095932 3.29362726 3.8095932
		 0.43362999 3.85959315 0.43362999 2.16211534 3.29362869 0.55211538 3.29362869 0.55211538
		 0.43362856 2.16211534 0.43362856 0.53382397 3.2936306 0.48382401 3.2936306 0.48382401
		 0.43362665 0.53382397 0.43362665 3.78745103 0.43362856 3.78745103 3.29362869 2.17745113
		 3.29362869 2.17745113 0.43362856 3.93471241 0.43666649 3.93471241 2.046666622 3.88471246
		 2.046666622 3.88471246 0.43666649 3.88471246 3.67962217 3.88471246 2.069625378 3.93471241
		 2.069625378 3.93471241 3.67962217;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 72 ".pt[0:71]" -type "float3"  287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 
		-525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 
		-624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 287.50031 -525 -624.99994 
		287.50031 -525 -624.99994;
	setAttr -s 72 ".vt[0:71]"  -287.50030518 525 622.99993896 12.49969482 525 622.99993896
		 -287.50030518 529 622.99993896 12.49969482 529 622.99993896 -287.50030518 529 601.99993896
		 12.49969482 529 601.99993896 -287.50030518 525 601.99993896 12.49969482 525 601.99993896
		 -283.50030518 529 618.99993896 8.49969482 529 618.99993896 -283.50030518 531 618.99993896
		 8.49969482 531 618.99993896 -283.50030518 531 605.99993896 8.49969482 531 605.99993896
		 -283.50030518 529 605.99993896 8.49969482 529 605.99993896 -287.50030518 696 622.99993896
		 12.49969482 696 622.99993896 -287.50030518 700 622.99993896 12.49969482 700 622.99993896
		 -287.50030518 700 601.99993896 12.49969482 700 601.99993896 -287.50030518 696 601.99993896
		 12.49969482 696 601.99993896 -283.50030518 694 618.99993896 8.49969482 694 618.99993896
		 -283.50030518 696 618.99993896 8.49969482 696 618.99993896 -283.50030518 696 605.99993896
		 8.49969482 696 605.99993896 -283.50030518 694 605.99993896 8.49969482 694 605.99993896
		 -287.50030518 696 622.99993896 -287.50030518 529 622.99993896 -283.50030518 696 622.99993896
		 -283.50030518 529 622.99993896 -283.50030518 696 601.99993896 -283.50030518 529 601.99993896
		 -287.50030518 696 601.99993896 -287.50030518 529 601.99993896 -283.50030518 694 618.99993896
		 -283.50030518 531 618.99993896 -281.50030518 694 618.99993896 -281.50030518 531 618.99993896
		 -281.50030518 694 605.99993896 -281.50030518 531 605.99993896 -283.50030518 694 605.99993896
		 -283.50030518 531 605.99993896 6.49969482 694 618.99993896 6.49969482 531 618.99993896
		 8.49969482 694 618.99993896 8.49969482 531 618.99993896 8.49969482 694 605.99993896
		 8.49969482 531 605.99993896 6.49969482 694 605.99993896 6.49969482 531 605.99993896
		 8.49972534 696 622.99993896 8.49972534 529 622.99993896 12.49972534 696 622.99993896
		 12.49972534 529 622.99993896 12.49972534 696 601.99993896 12.49972534 529 601.99993896
		 8.49972534 696 601.99993896 8.49972534 529 601.99993896 -281.50030518 531 610.99993896
		 6.49969482 531 610.99993896 -281.50030518 531 613.99993896 6.49969482 531 613.99993896
		 -281.50030518 694 613.99993896 6.49969482 694 613.99993896 -281.50030518 694 610.99993896
		 6.49969482 694 610.99993896;
	setAttr -s 108 ".ed[0:107]"  0 1 0 0 2 0 1 3 0 2 4 0 4 6 0 5 7 0 6 0 0
		 7 1 0 3 5 0 2 3 0 4 5 0 6 7 0 8 9 0 10 11 0 12 13 0 14 15 0 8 10 0 9 11 0 10 12 0
		 11 13 0 12 14 0 13 15 0 14 8 0 15 9 0 16 17 0 16 18 0 17 19 0 18 20 0 20 22 0 21 23 0
		 22 16 0 23 17 0 19 21 0 18 19 0 20 21 0 22 23 0 24 25 0 26 27 0 28 29 0 30 31 0 24 26 0
		 25 27 0 26 28 0 27 29 0 28 30 0 29 31 0 30 24 0 31 25 0 32 33 0 32 34 0 33 35 0 34 36 0
		 36 38 0 37 39 0 38 32 0 39 33 0 35 37 0 34 35 0 36 37 0 38 39 0 40 41 0 42 43 0 44 45 0
		 46 47 0 40 42 0 41 43 0 42 44 0 43 45 0 44 46 0 45 47 0 46 40 0 47 41 0 48 49 0 50 51 0
		 52 53 0 54 55 0 48 50 0 49 51 0 50 52 0 51 53 0 52 54 0 53 55 0 54 48 0 55 49 0 56 57 0
		 56 58 0 57 59 0 58 60 0 60 62 0 61 63 0 62 56 0 63 57 0 59 61 0 58 59 0 60 61 0 62 63 0
		 64 65 0 64 66 0 65 67 0 66 68 0 67 69 0 68 70 0 69 71 0 70 64 0 71 65 0 66 67 0 68 69 0
		 70 71 0;
	setAttr -s 24 ".n[0:23]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 54 -ch 216 ".fc[0:53]" -type "polyFaces" 
		f 4 -2 0 2 -10
		mu 0 4 16 13 23 17
		f 4 -4 9 8 -11
		mu 0 4 8 9 10 21
		f 4 -5 10 5 -12
		mu 0 4 14 20 11 19
		f 4 -1 -7 11 7
		mu 0 4 12 22 18 15
		f 4 -3 -8 -6 -9
		mu 0 4 0 1 2 3
		f 4 1 3 4 6
		mu 0 4 4 5 6 7
		f 4 12 17 -14 -17
		mu 0 4 24 25 26 27
		f 4 13 19 -15 -19
		mu 0 4 28 29 30 31
		f 4 14 21 -16 -21
		mu 0 4 32 33 34 35
		f 4 15 23 -13 -23
		mu 0 4 36 37 38 39
		f 4 -24 -22 -20 -18
		mu 0 4 40 41 42 43
		f 4 22 16 18 20
		mu 0 4 44 45 46 47
		f 4 -26 24 26 -34
		mu 0 4 48 49 50 51
		f 4 -28 33 32 -35
		mu 0 4 52 53 54 55
		f 4 -29 34 29 -36
		mu 0 4 56 57 58 59
		f 4 -25 -31 35 31
		mu 0 4 60 61 62 63
		f 4 -27 -32 -30 -33
		mu 0 4 64 65 66 67
		f 4 25 27 28 30
		mu 0 4 68 69 70 71
		f 4 36 41 -38 -41
		mu 0 4 72 73 74 75
		f 4 37 43 -39 -43
		mu 0 4 76 77 78 79
		f 4 38 45 -40 -45
		mu 0 4 80 81 82 83
		f 4 39 47 -37 -47
		mu 0 4 84 85 86 87
		f 4 -48 -46 -44 -42
		mu 0 4 88 89 90 91
		f 4 46 40 42 44
		mu 0 4 92 93 94 95
		f 4 -50 48 50 -58
		mu 0 4 96 97 98 99
		f 4 -52 57 56 -59
		mu 0 4 100 101 102 103
		f 4 -53 58 53 -60
		mu 0 4 104 105 106 107
		f 4 55 -49 -55 59
		mu 0 4 108 109 110 111
		f 4 -51 -56 -54 -57
		mu 0 4 112 113 114 115
		f 4 49 51 52 54
		mu 0 4 116 117 118 119
		f 4 60 65 -62 -65
		mu 0 4 120 121 122 123
		f 4 61 67 -63 -67
		mu 0 4 124 125 126 127
		f 4 62 69 -64 -69
		mu 0 4 128 129 130 131
		f 4 63 71 -61 -71
		mu 0 4 132 133 134 135
		f 4 -72 -70 -68 -66
		mu 0 4 136 137 138 139
		f 4 70 64 66 68
		mu 0 4 140 141 142 143
		f 4 72 77 -74 -77
		mu 0 4 144 145 146 147
		f 4 73 79 -75 -79
		mu 0 4 148 149 150 151
		f 4 74 81 -76 -81
		mu 0 4 152 153 154 155
		f 4 75 83 -73 -83
		mu 0 4 156 157 158 159
		f 4 -84 -82 -80 -78
		mu 0 4 160 161 162 163
		f 4 82 76 78 80
		mu 0 4 164 165 166 167
		f 4 -86 84 86 -94
		mu 0 4 168 169 170 171
		f 4 -88 93 92 -95
		mu 0 4 172 173 174 175
		f 4 -89 94 89 -96
		mu 0 4 176 177 178 179
		f 4 91 -85 -91 95
		mu 0 4 180 181 182 183
		f 4 -87 -92 -90 -93
		mu 0 4 184 185 186 187
		f 4 85 87 88 90
		mu 0 4 188 189 190 191
		f 4 -98 96 98 -106
		mu 0 4 192 193 194 195
		f 4 -100 105 100 -107
		mu 0 4 196 197 198 199
		f 4 -102 106 102 -108
		mu 0 4 200 201 202 203
		f 4 -97 -104 107 104
		mu 0 4 204 205 206 207
		f 4 -105 -103 -101 -99
		mu 0 4 208 209 210 211
		f 4 103 97 99 101
		mu 0 4 212 213 214 215;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "UCX_Window01" -p "Window01_grp";
	rename -uid "A08D2F00-4B2C-2137-2DF6-E985BD2808D1";
	setAttr ".rp" -type "double3" 300 1.4210854715202004e-14 0 ;
	setAttr ".sp" -type "double3" 300 1.4210854715202004e-14 0 ;
createNode mesh -n "UCX_Window01Shape" -p "UCX_Window01";
	rename -uid "508E2B12-4AD2-3E06-0FE1-8CA2915C0AE9";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 6 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "back";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[2]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottom";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "f[3]";
	setAttr ".gtag[2].gtagnm" -type "string" "front";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 1 "f[0]";
	setAttr ".gtag[3].gtagnm" -type "string" "left";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "f[5]";
	setAttr ".gtag[4].gtagnm" -type "string" "right";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "f[4]";
	setAttr ".gtag[5].gtagnm" -type "string" "top";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 1 "f[1]";
	setAttr ".pv" -type "double2" 0.5 0.3279646635055542 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" 0.94177514 0.4098824
		 1 0.4098824 1 0.81745631 0.94177514 0.81745631 0.94177514 0 0.99999994 0 0.99999994
		 0.40757412 0.94177514 0.40757412 0.82174498 0.6986981 0.82174498 0 0.87996984 0 0.87996984
		 0.6986981 0.88176006 0.6986981 0.88176006 0 0.93998492 0 0.93998492 0.6986981 0 0.69869828
		 0 0 0.40757397 0 0.40757397 0.69869828 0.41087249 0.69869828 0.41087249 0 0.81844646
		 0 0.81844646 0.69869828;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  125 -100 -625 125 -100 -625 
		125 -100 -625 125 -100 -625 125 -100 -625 125 -100 -625 125 -100 -625 125 -100 -625;
	setAttr -s 8 ".vt[0:7]"  -124.99998474 100 625 175.000015258789 100 625
		 -124.99998474 275 625 175.000015258789 275 625 -124.99998474 275 600 175.000015258789 275 600
		 -124.99998474 100 600 175.000015258789 100 600;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 24 ".n[0:23]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 16 17 18 19
		f 4 1 7 -3 -7
		mu 0 4 8 9 10 11
		f 4 2 9 -4 -9
		mu 0 4 20 21 22 23
		f 4 3 11 -1 -11
		mu 0 4 12 13 14 15
		f 4 -12 -10 -8 -6
		mu 0 4 0 1 2 3
		f 4 10 4 6 8
		mu 0 4 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode groupId -n "groupId317";
	rename -uid "DF58074D-4CE3-6940-2B7C-4C81D238AF4C";
	setAttr ".ihi" 0;
createNode shadingEngine -n "lambert12SG";
	rename -uid "9ACFB45A-44C6-9C30-EB4B-96B12325F9C1";
	setAttr ".ihi" 0;
	setAttr -s 8 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 3 ".gn";
createNode materialInfo -n "materialInfo19";
	rename -uid "13AB109B-441E-AD20-B211-CDAA5502129B";
createNode lambert -n "Misc05_grid";
	rename -uid "F78E2D96-4E3A-1B1A-DD62-349221A94604";
createNode file -n "file11";
	rename -uid "4F44A183-41CE-7902-594F-FBBFBD8CCB5D";
Misc05_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture11";
	rename -uid "A1254828-4BFD-D309-20CB-9E8A0EACFBCA";
createNode groupId -n "groupId318";
	rename -uid "A8F32CA2-4E67-E6F9-FA9F-6798ECB43B2D";
	setAttr ".ihi" 0;
createNode shadingEngine -n "lambert18SG";
	rename -uid "844B0B90-4F2A-784A-7877-C6ADEEBB4FCB";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 3 ".gn";
createNode materialInfo -n "materialInfo27";
	rename -uid "E05EDED6-4A3F-0483-FAB3-A38753DF3EDE";
createNode lambert -n "M_Glass";
	rename -uid "6184EAA9-466D-1A9D-0689-16A2E4ABD40D";
	setAttr ".c" -type "float3" 0 1 1 ;
	setAttr ".it" -type "float3" 0.92258066 0.92258066 0.92258066 ;
createNode groupId -n "groupId319";
	rename -uid "CC2E1119-4AD1-17CC-3256-D4B0BE5C80F8";
	setAttr ".ihi" 0;
createNode displayLayer -n "UCX_GROUP";
	rename -uid "74C6A8D0-42C7-016E-CE93-DA868FD6DCCD";
	setAttr ".v" no;
	setAttr ".ufem" -type "stringArray" 0  ;
	setAttr ".do" 2;
createNode displayLayerManager -n "layerManager";
	rename -uid "5C8521F5-4710-6E4E-B088-74AE359AD88F";
	setAttr ".cdl" 2;
	setAttr -s 5 ".dli[1:4]"  1 2 3 4;
	setAttr -s 5 ".dli";
createNode materialInfo -n "materialInfo24";
	rename -uid "DC7D65CD-4198-DDC6-196D-B8B65B69E240";
createNode shadingEngine -n "lambert17SG";
	rename -uid "D3096CED-4348-1694-945D-CC950640415F";
	setAttr ".ihi" 0;
	setAttr -s 227 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "M_UCX";
	rename -uid "BA3A97EB-4ECF-DC0E-8639-C0B5506060F8";
	setAttr ".c" -type "float3" 1 0 0 ;
	setAttr ".it" -type "float3" 0.68387097 0.68387097 0.68387097 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "708644FF-42B6-1EAB-5FD4-0C8CCB38AB2C";
	setAttr -s 32 ".lnk";
	setAttr -s 32 ".slnk";
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".aoon" yes;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
	setAttr ".rtfm" 1;
select -ne :renderPartition;
	setAttr -s 32 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 27 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 15 ".u";
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
	setAttr -s 15 ".tx";
select -ne :standardSurface1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :openPBR_shader1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :initialShadingGroup;
	setAttr -s 5 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "standardSurface1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHideFaceDataSet;
select -ne :modelPanel4ViewSelectedSet;
	setAttr ".ihi" 0;
connectAttr "groupId317.id" "Window01Shape.iog.og[0].gid";
connectAttr "lambert12SG.mwc" "Window01Shape.iog.og[0].gco";
connectAttr "groupId318.id" "Window01Shape.iog.og[1].gid";
connectAttr "lambert18SG.mwc" "Window01Shape.iog.og[1].gco";
connectAttr "groupId319.id" "Window01Shape.ciog.cog[1].cgid";
connectAttr "UCX_GROUP.di" "UCX_Window01.do";
connectAttr "Misc05_grid.oc" "lambert12SG.ss";
connectAttr "|typeMeshShape7.iog" "lambert12SG.dsm" -na;
connectAttr "typeMeshShape5.iog" "lambert12SG.dsm" -na;
connectAttr "typeMeshShape6.iog" "lambert12SG.dsm" -na;
connectAttr "|typeMeshShape7.iog" "lambert12SG.dsm" -na;
connectAttr "typeMeshShape8.iog" "lambert12SG.dsm" -na;
connectAttr "Window02Shape.iog.og[1]" "lambert12SG.dsm" -na;
connectAttr "Window01Shape.iog.og[0]" "lambert12SG.dsm" -na;
connectAttr "Window01Shape.ciog.cog[1]" "lambert12SG.dsm" -na;
connectAttr "groupId309.msg" "lambert12SG.gn" -na;
connectAttr "groupId317.msg" "lambert12SG.gn" -na;
connectAttr "groupId319.msg" "lambert12SG.gn" -na;
connectAttr "lambert12SG.msg" "materialInfo19.sg";
connectAttr "Misc05_grid.msg" "materialInfo19.m";
connectAttr "file11.msg" "materialInfo19.t" -na;
connectAttr "file11.oc" "Misc05_grid.c";
connectAttr ":defaultColorMgtGlobals.cme" "file11.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file11.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file11.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file11.ws";
connectAttr "place2dTexture11.c" "file11.c";
connectAttr "place2dTexture11.tf" "file11.tf";
connectAttr "place2dTexture11.rf" "file11.rf";
connectAttr "place2dTexture11.mu" "file11.mu";
connectAttr "place2dTexture11.mv" "file11.mv";
connectAttr "place2dTexture11.s" "file11.s";
connectAttr "place2dTexture11.wu" "file11.wu";
connectAttr "place2dTexture11.wv" "file11.wv";
connectAttr "place2dTexture11.re" "file11.re";
connectAttr "place2dTexture11.of" "file11.of";
connectAttr "place2dTexture11.r" "file11.ro";
connectAttr "place2dTexture11.n" "file11.n";
connectAttr "place2dTexture11.vt1" "file11.vt1";
connectAttr "place2dTexture11.vt2" "file11.vt2";
connectAttr "place2dTexture11.vt3" "file11.vt3";
connectAttr "place2dTexture11.vc1" "file11.vc1";
connectAttr "place2dTexture11.o" "file11.uv";
connectAttr "place2dTexture11.ofs" "file11.fs";
connectAttr "M_Glass.oc" "lambert18SG.ss";
connectAttr "Window02Shape.iog.og[0]" "lambert18SG.dsm" -na;
connectAttr "Window02Shape.ciog.cog[1]" "lambert18SG.dsm" -na;
connectAttr "Window01Shape.iog.og[1]" "lambert18SG.dsm" -na;
connectAttr "groupId308.msg" "lambert18SG.gn" -na;
connectAttr "groupId310.msg" "lambert18SG.gn" -na;
connectAttr "groupId318.msg" "lambert18SG.gn" -na;
connectAttr "lambert18SG.msg" "materialInfo27.sg";
connectAttr "M_Glass.msg" "materialInfo27.m";
connectAttr "layerManager.dli[2]" "UCX_GROUP.id";
connectAttr "lambert17SG.msg" "materialInfo24.sg";
connectAttr "M_UCX.msg" "materialInfo24.m";
connectAttr "M_UCX.oc" "lambert17SG.ss";
connectAttr "|UCX_FloorShape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_StairsLanding_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_17Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_18Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_19Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_20Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_21Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_22Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_23Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_24Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_25Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_26Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_27Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_28Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_29Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_30Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_31Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_17Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_18Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_19Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_20Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_21Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_22Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_23Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_24Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_25Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_26Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_27Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_28Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_29Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_30Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_31Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_FloorShape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs_11Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_StairsLanding_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall01_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall04_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall04_Shape4.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall04_Shape5.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall04_Shape6.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall04_Shape7.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_BF02_Floor02_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_17Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_18Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_19Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_20Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_21Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_22Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_23Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_24Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_25Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_26Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_27Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_28Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_29Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_30Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_31Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_StairsLanding_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_17Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_18Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_19Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_20Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_21Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_22Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_23Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_24Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_25Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_26Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_27Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_28Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_29Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_30Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Stairs_31Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_StairsLanding_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_20Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_19Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_18Shape.iog" "lambert17SG.dsm" -na;
connectAttr "|UCX_Wall01_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_15Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_16Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall01_17Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall02_10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall09_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall09_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall09_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Wall10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Floor01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall02_10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall05_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall05_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall05_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Floor01_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Floor01_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Floor01_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Floor01_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall02_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall02_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall02_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall05_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall06_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF02_Wall03_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall01_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_03Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_04Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_05Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_06Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_07Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_08Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_09Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_10Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_11Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_12Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01_13Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01LandingShape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape4.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape5.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape6.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape7.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape8.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_BF01_Wall04_Shape9.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_RailingShape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Window02Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Window01Shape.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_InteriorDoorShape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_InteriorDoorFrame01_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_InteriorDoorFrame01_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_InteriorDoorFrame01_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_ExteriorDoorShape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_ExteriorDoorFrame01_Shape1.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_ExteriorDoorFrame01_Shape2.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_ExteriorDoorFrame01_Shape3.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_ExteriorDoorFrame01_Shape4.iog" "lambert17SG.dsm" -na;
connectAttr "UCX_Stairs01RailingShape1.iog" "lambert17SG.dsm" -na;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert12SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert17SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert18SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert12SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert17SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert18SG.message" ":defaultLightSet.message";
connectAttr "lambert12SG.pa" ":renderPartition.st" -na;
connectAttr "lambert17SG.pa" ":renderPartition.st" -na;
connectAttr "lambert18SG.pa" ":renderPartition.st" -na;
connectAttr "Misc05_grid.msg" ":defaultShaderList1.s" -na;
connectAttr "M_UCX.msg" ":defaultShaderList1.s" -na;
connectAttr "M_Glass.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture11.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file11.msg" ":defaultTextureList1.tx" -na;
// End of Window01.ma
