//Maya ASCII 2026 scene
//Name: Cylinder_200cm.ma
//Last modified: Thu, Feb 19, 2026 01:00:27 PM
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
fileInfo "UUID" "E9FADDE6-4F49-4619-6E4D-0E847B8F57DE";
fileInfo "license" "education";
createNode transform -n "Cylinder_200cm";
	rename -uid "7F2979A8-4D20-6C0E-91FE-099B6FADE704";
createNode mesh -n "Cylinder_200cmShape" -p "Cylinder_200cm";
	rename -uid "CB62B4D1-44FB-74E3-F5E6-24A1C797C869";
	setAttr -k off ".v";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 4 "f[3]" "f[18]" "f[33]" "f[48]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 10 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "bottom";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 4 "f[5:9]" "f[20:24]" "f[35:39]" "f[50:54]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottomRing";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 4 "e[0:4]" "e[28:32]" "e[53:57]" "e[78:82]";
	setAttr ".gtag[2].gtagnm" -type "string" "cylBottomCap";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 5 "vtx[0:5]" "vtx[12]" "vtx[14:18]" "vtx[24:28]" "vtx[34:37]";
	setAttr ".gtag[3].gtagnm" -type "string" "cylBottomRing";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 4 "vtx[0:5]" "vtx[14:18]" "vtx[24:28]" "vtx[34:37]";
	setAttr ".gtag[4].gtagnm" -type "string" "cylSides";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 2 "vtx[0:11]" "vtx[14:41]";
	setAttr ".gtag[5].gtagnm" -type "string" "cylTopCap";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 5 "vtx[6:11]" "vtx[13]" "vtx[19:23]" "vtx[29:33]" "vtx[38:41]";
	setAttr ".gtag[6].gtagnm" -type "string" "cylTopRing";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 4 "vtx[6:11]" "vtx[19:23]" "vtx[29:33]" "vtx[38:41]";
	setAttr ".gtag[7].gtagnm" -type "string" "sides";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 4 "f[0:4]" "f[15:19]" "f[30:34]" "f[45:49]";
	setAttr ".gtag[8].gtagnm" -type "string" "top";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 4 "f[10:14]" "f[25:29]" "f[40:44]" "f[55:59]";
	setAttr ".gtag[9].gtagnm" -type "string" "topRing";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 4 "e[5:9]" "e[33:37]" "e[58:62]" "e[83:87]";
	setAttr ".pv" -type "double2" 2.9963799715042114 0.00047159194946289062 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 98 ".uvst[0].uvsp[0:97]" -type "float2" 1.000000596046 4
		 0.9510569 3.69098282 0.8090176 3.41221523 0.58778518 3.19098282 0.30901766 3.04894352
		 4.7683716e-07 3 4.50123119 -0.99929261 4.80097294 -0.99924517 5.10071754 -0.99919796
		 5.40045834 -0.99915099 5.70020247 -0.99910402 5.99994564 -0.99905658 4.50094128 1.00070738792
		 4.80068493 1.00075483322 5.10042858 1.00080180168 5.40017033 1.00084877014 5.6999135
		 1.00089621544 5.99965668 1.0009431839 -0.3090167 3.048942566 -0.5877853 3.19098186
		 -0.80901676 3.41221428 -0.95105702 3.69098282 -0.99999958 3.99999905 0 3 4.7683716e-07
		 4 0 3.99999905 3.0025193691 -0.99952817 3.30226016 -0.99948096 3.30197144 1.00051879883
		 3.0022292137 1.00047135353 3.60200357 -0.99943376 3.60171461 1.00056600571 3.90174532
		 -0.99938703 3.90145636 1.00061321259 4.20148849 -0.99933946 4.20120049 1.0006608963
		 0.9510569 3.69098282 1.000000596046 4 4.7683716e-07 4 0.8090176 3.41221523 0.58778518
		 3.19098282 0.30901766 3.04894352 4.7683716e-07 3 -0.99999958 3.99999905 -0.95105702
		 3.69098282 0 3.99999905 -0.80901676 3.41221428 -0.5877853 3.19098186 -0.3090167 3.048942566
		 0 3 1.50380611 -0.99976349 1.80354762 -0.99971676 1.80325854 1.00028300285 1.50351715
		 1.00023651123 2.10329056 -0.99967003 2.10300136 1.00033020973 2.40303254 -0.99962234
		 2.40274453 1.00037765503 2.70277619 -0.99957561 2.70248795 1.00042438507 0.9510569
		 3.69098282 1.000000596046 4 4.7683716e-07 4 0.8090176 3.41221523 0.58778518 3.19098282
		 0.30901766 3.04894352 4.7683716e-07 3 -0.99999958 3.99999905 -0.95105702 3.69098282
		 0 3.99999905 -0.80901676 3.41221428 -0.5877853 3.19098186 -0.3090167 3.048942566
		 0 3 0.0050923824 -1 0.30483437 -0.99995327 0.30454588 1.000047683716 0.0048034191
		 1.000000476837 0.60457802 -0.99990559 0.60428953 1.000094413757 0.90432024 -0.99985886
		 0.90403056 1.00014209747 1.20406294 -0.9998107 1.20377386 1.00018882751 0.9510569
		 3.69098282 1.000000596046 4 4.7683716e-07 4 0.8090176 3.41221523 0.58778518 3.19098282
		 0.30901766 3.04894352 4.7683716e-07 3 -0.99999958 3.99999905 -0.95105702 3.69098282
		 0 3.99999905 -0.80901676 3.41221428 -0.5877853 3.19098186 -0.3090167 3.048942566
		 0 3;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 42 ".pt[0:41]" -type "float3"  -650 100 300 -650 100 300 
		-650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 
		100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 
		300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 
		-650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 
		100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 
		300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 -650 100 300 
		-650 100 300 -650 100 300;
	setAttr -s 42 ".vt[0:41]"  650 -100 -200 680.90161133 -100 -204.89434814
		 708.77856445 -100 -219.098297119 730.90161133 -100 -241.22146606 745.10571289 -100 -269.098297119
		 750 -100 -300 650 100 -200 680.90161133 100 -204.89434814 708.77856445 100 -219.098297119
		 730.90161133 100 -241.22146606 745.10571289 100 -269.098297119 750 100 -300 650 -100 -300
		 650 100 -300 550 -100 -300 554.89434814 -100 -269.098388672 569.098266602 -100 -241.22143555
		 591.22143555 -100 -219.098388672 619.098266602 -100 -204.89428711 550 100 -300 554.89434814 100 -269.098388672
		 569.098266602 100 -241.22143555 591.22143555 100 -219.098388672 619.098266602 100 -204.89428711
		 650 -100 -400 619.098388672 -100 -395.10565186 591.22143555 -100 -380.90170288 569.098388672 -100 -358.77853394
		 554.89428711 -100 -330.90170288 650 100 -400 619.098388672 100 -395.10565186 591.22143555 100 -380.90170288
		 569.098388672 100 -358.77853394 554.89428711 100 -330.90170288 745.10565186 -100 -330.90161133
		 730.9017334 -100 -358.77856445 708.77856445 -100 -380.90161133 680.9017334 -100 -395.10571289
		 745.10565186 100 -330.90161133 730.9017334 100 -358.77856445 708.77856445 100 -380.90161133
		 680.9017334 100 -395.10571289;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 11 0 0 6 1 1 7 1 2 8 1 3 9 1 4 10 1 5 11 1 12 0 1 12 1 1 12 2 1 12 3 1
		 12 4 1 12 5 1 6 13 1 7 13 1 8 13 1 9 13 1 10 13 1 11 13 1 14 15 0 15 16 0 16 17 0
		 17 18 0 18 0 0 19 20 0 20 21 0 21 22 0 22 23 0 23 6 0 14 19 1 15 20 1 16 21 1 17 22 1
		 18 23 1 12 14 1 12 15 1 12 16 1 12 17 1 12 18 1 19 13 1 20 13 1 21 13 1 22 13 1 23 13 1
		 24 25 0 25 26 0 26 27 0 27 28 0 28 14 0 29 30 0 30 31 0 31 32 0 32 33 0 33 19 0 24 29 1
		 25 30 1 26 31 1 27 32 1 28 33 1 12 24 1 12 25 1 12 26 1 12 27 1 12 28 1 29 13 1 30 13 1
		 31 13 1 32 13 1 33 13 1 5 34 0 34 35 0 35 36 0 36 37 0 37 24 0 11 38 0 38 39 0 39 40 0
		 40 41 0 41 29 0 34 38 1 35 39 1 36 40 1 37 41 1 12 34 1 12 35 1 12 36 1 12 37 1 38 13 1
		 39 13 1 40 13 1 41 13 1;
	setAttr -s 82 ".n[0:81]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20;
	setAttr -s 60 -ch 200 ".fc[0:59]" -type "polyFaces" 
		f 4 0 11 -6 -11
		mu 0 4 6 7 13 12
		f 4 1 12 -7 -12
		mu 0 4 7 8 14 13
		f 4 2 13 -8 -13
		mu 0 4 8 9 15 14
		f 4 3 14 -9 -14
		mu 0 4 9 10 16 15
		f 4 4 15 -10 -15
		mu 0 4 10 11 17 16
		f 3 -1 -17 17
		mu 0 3 1 0 24
		f 3 -2 -18 18
		mu 0 3 2 1 24
		f 3 -3 -19 19
		mu 0 3 3 2 24
		f 3 -4 -20 20
		mu 0 3 4 3 24
		f 3 -5 -21 21
		mu 0 3 5 4 24
		f 3 5 23 -23
		mu 0 3 22 21 25
		f 3 6 24 -24
		mu 0 3 21 20 25
		f 3 7 25 -25
		mu 0 3 20 19 25
		f 3 8 26 -26
		mu 0 3 19 18 25
		f 3 9 27 -27
		mu 0 3 18 23 25
		f 4 28 39 -34 -39
		mu 0 4 26 27 28 29
		f 4 29 40 -35 -40
		mu 0 4 27 30 31 28
		f 4 30 41 -36 -41
		mu 0 4 30 32 33 31
		f 4 31 42 -37 -42
		mu 0 4 32 34 35 33
		f 4 32 10 -38 -43
		mu 0 4 34 6 12 35
		f 3 -29 -44 44
		mu 0 3 36 37 38
		f 3 -30 -45 45
		mu 0 3 39 36 38
		f 3 -31 -46 46
		mu 0 3 40 39 38
		f 3 -32 -47 47
		mu 0 3 41 40 38
		f 3 -33 -48 16
		mu 0 3 42 41 38
		f 3 33 49 -49
		mu 0 3 43 44 45
		f 3 34 50 -50
		mu 0 3 44 46 45
		f 3 35 51 -51
		mu 0 3 46 47 45
		f 3 36 52 -52
		mu 0 3 47 48 45
		f 3 37 22 -53
		mu 0 3 48 49 45
		f 4 53 64 -59 -64
		mu 0 4 50 51 52 53
		f 4 54 65 -60 -65
		mu 0 4 51 54 55 52
		f 4 55 66 -61 -66
		mu 0 4 54 56 57 55
		f 4 56 67 -62 -67
		mu 0 4 56 58 59 57
		f 4 57 38 -63 -68
		mu 0 4 58 26 29 59
		f 3 -54 -69 69
		mu 0 3 60 61 62
		f 3 -55 -70 70
		mu 0 3 63 60 62
		f 3 -56 -71 71
		mu 0 3 64 63 62
		f 3 -57 -72 72
		mu 0 3 65 64 62
		f 3 -58 -73 43
		mu 0 3 66 65 62
		f 3 58 74 -74
		mu 0 3 67 68 69
		f 3 59 75 -75
		mu 0 3 68 70 69
		f 3 60 76 -76
		mu 0 3 70 71 69
		f 3 61 77 -77
		mu 0 3 71 72 69
		f 3 62 48 -78
		mu 0 3 72 73 69
		f 4 78 88 -84 -16
		mu 0 4 74 75 76 77
		f 4 79 89 -85 -89
		mu 0 4 75 78 79 76
		f 4 80 90 -86 -90
		mu 0 4 78 80 81 79
		f 4 81 91 -87 -91
		mu 0 4 80 82 83 81
		f 4 82 63 -88 -92
		mu 0 4 82 50 53 83
		f 3 -79 -22 92
		mu 0 3 84 85 86
		f 3 -80 -93 93
		mu 0 3 87 84 86
		f 3 -81 -94 94
		mu 0 3 88 87 86
		f 3 -82 -95 95
		mu 0 3 89 88 86
		f 3 -83 -96 68
		mu 0 3 90 89 86
		f 3 83 96 -28
		mu 0 3 91 92 93
		f 3 84 97 -97
		mu 0 3 92 94 93
		f 3 85 98 -98
		mu 0 3 94 95 93
		f 3 86 99 -99
		mu 0 3 95 96 93
		f 3 87 73 -100
		mu 0 3 96 97 93;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 30 
		6 0 
		7 0 
		9 0 
		10 0 
		12 0 
		13 0 
		15 0 
		16 0 
		26 0 
		27 0 
		28 0 
		29 0 
		32 0 
		33 0 
		34 0 
		35 0 
		50 0 
		51 0 
		52 0 
		53 0 
		56 0 
		57 0 
		58 0 
		59 0 
		75 0 
		76 0 
		80 0 
		81 0 
		82 0 
		83 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 168;
createNode groupId -n "groupId101";
	rename -uid "83B87482-49D8-D9B7-592B-E6837C86585B";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "1E8FC790-478B-EA01-CE9E-699889DD1FF4";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "A2219B52-4F18-01AD-663A-2BB9BF22D742";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "93215E0D-40E5-2578-6B34-A2BA1F7303F1";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode standardSurface -n "Floor_grid";
	rename -uid "BD970BAC-45C9-80B5-BDC5-D5AB329CF0D1";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "10DAC5FB-47FE-DF6B-34F7-8AA1C2FF366B";
Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "64D30967-4B25-86E1-14BD-0FBD8ECAAB6D";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A09AE64C-4168-CD38-5685-A6ABCF2C050F";
	setAttr -s 5 ".lnk";
	setAttr -s 5 ".slnk";
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
	setAttr ".rtfm" 1;
select -ne :renderPartition;
	setAttr -s 3 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 7 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
select -ne :standardSurface1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :openPBR_shader1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
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
connectAttr "groupId101.id" "Cylinder_200cmShape.iog.og[1].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Cylinder_200cmShape.iog.og[1].gco"
		;
connectAttr "groupId101.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Cylinder_200cmShape.iog.og[1]" "textureEditorIsolateSelectSet.dsm" 
		-na;
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Cylinder_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "file1.oc" "Floor_grid.bc";
connectAttr ":defaultColorMgtGlobals.cme" "file1.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file1.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file1.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file1.ws";
connectAttr "place2dTexture1.c" "file1.c";
connectAttr "place2dTexture1.tf" "file1.tf";
connectAttr "place2dTexture1.rf" "file1.rf";
connectAttr "place2dTexture1.mu" "file1.mu";
connectAttr "place2dTexture1.mv" "file1.mv";
connectAttr "place2dTexture1.s" "file1.s";
connectAttr "place2dTexture1.wu" "file1.wu";
connectAttr "place2dTexture1.wv" "file1.wv";
connectAttr "place2dTexture1.re" "file1.re";
connectAttr "place2dTexture1.of" "file1.of";
connectAttr "place2dTexture1.r" "file1.ro";
connectAttr "place2dTexture1.n" "file1.n";
connectAttr "place2dTexture1.vt1" "file1.vt1";
connectAttr "place2dTexture1.vt2" "file1.vt2";
connectAttr "place2dTexture1.vt3" "file1.vt3";
connectAttr "place2dTexture1.vc1" "file1.vc1";
connectAttr "place2dTexture1.o" "file1.uv";
connectAttr "place2dTexture1.ofs" "file1.fs";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "standardSurface2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "standardSurface2SG.message" ":defaultLightSet.message";
connectAttr "standardSurface2SG.pa" ":renderPartition.st" -na;
connectAttr "Floor_grid.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file1.msg" ":defaultTextureList1.tx" -na;
// End of Cylinder_200cm.ma
