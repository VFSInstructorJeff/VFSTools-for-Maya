//Maya ASCII 2026 scene
//Name: Cylinder_400cm.ma
//Last modified: Thu, Feb 19, 2026 01:00:56 PM
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
fileInfo "UUID" "00134E57-4D57-E73D-3EE9-B186BE76E613";
fileInfo "license" "education";
createNode transform -n "Cylinder_400cm";
	rename -uid "F6AA1E45-4FF1-A654-FF28-BAA177D10312";
createNode mesh -n "Cylinder_400cmShape" -p "Cylinder_400cm";
	rename -uid "9705B36F-4C9E-DD8E-3D39-0799E93E7014";
	setAttr -k off ".v";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 4 "f[1]" "f[16]" "f[31]" "f[46]";
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
	setAttr ".pv" -type "double2" 0.88196632266044617 1.9995913505554199 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 128 ".uvst[0].uvsp[0:127]" -type "float2" 2.000000238419 7
		 1.90211272 6.38196564 1.61803412 5.82443047 1.1755693 5.38196564 0.61803436 5.097887039
		 -2.9802322e-08 5 -0.00061655045 -3.00030612946 0.61754596 -3.00040817261 1.1592356
		 -3 1.86780286 -3.00010204315 2.38116837 -3.0002040863 0.004481554 -3.00081729889
		 0 0.99969351 0.63199693 1.0001026392 1.17342603 1.000000596046 1.82771361 0.99989772
		 -0.61723572 0.99928486 0.004481554 0.99918234 -0.61803436 5.097885132 -1.17557168
		 5.38196373 -1.6180346 5.82442856 -1.90211511 6.38196564 -2.000000238419 6.99999809
		 -9.8347664e-07 5 -2.9802322e-08 7 -9.8347664e-07 6.99999809 -0.61723572 -3.00071525574
		 2.38116837 0.99979556 0.61718857 -2.999897 0.61754596 0.99959147 1.82771361 -3.00010204315
		 1.86780286 0.9998976 -0.00061655045 -3.00030612946 0.61754596 -3.00040817261 0.61754596
		 0.99959147 0 0.99969351 0.61718857 -2.999897 1.1592356 -3 1.17342603 1.000000596046
		 0.63199693 1.0001026392 1.86780286 -3.00010204315 1.86780286 0.9998976 1.82771361
		 -3.00010204315 2.38116837 -3.0002040863 2.38116837 0.99979556 1.82771361 0.99989772
		 -0.61723572 -3.00071525574 0.004481554 -3.00081729889 0.004481554 0.99918234 -0.61723572
		 0.99928486 1.90211272 6.38196564 2.000000238419 7 -2.9802322e-08 7 1.61803412 5.82443047
		 1.1755693 5.38196564 0.61803436 5.097887039 -2.9802322e-08 5 -2.000000238419 6.99999809
		 -1.90211511 6.38196564 -9.8347664e-07 6.99999809 -1.6180346 5.82442856 -1.17557168
		 5.38196373 -0.61803436 5.097885132 -9.8347664e-07 5 -0.00061655045 -3.00030612946
		 0.61754596 -3.00040817261 0.61754596 0.99959147 0 0.99969351 0.61718857 -2.999897
		 1.1592356 -3 1.17342603 1.000000596046 0.63199693 1.0001026392 1.86780286 -3.00010204315
		 1.86780286 0.9998976 1.82771361 -3.00010204315 2.38116837 -3.0002040863 2.38116837
		 0.99979556 1.82771361 0.99989772 -0.61723572 -3.00071525574 0.004481554 -3.00081729889
		 0.004481554 0.99918234 -0.61723572 0.99928486 1.90211272 6.38196564 2.000000238419
		 7 -2.9802322e-08 7 1.61803412 5.82443047 1.1755693 5.38196564 0.61803436 5.097887039
		 -2.9802322e-08 5 -2.000000238419 6.99999809 -1.90211511 6.38196564 -9.8347664e-07
		 6.99999809 -1.6180346 5.82442856 -1.17557168 5.38196373 -0.61803436 5.097885132 -9.8347664e-07
		 5 -0.00061655045 -3.00030612946 0.61754596 -3.00040817261 0.61754596 0.99959147 0
		 0.99969351 0.61718857 -2.999897 1.1592356 -3 1.17342603 1.000000596046 0.63199693
		 1.0001026392 1.86780286 -3.00010204315 1.86780286 0.9998976 1.82771361 -3.00010204315
		 2.38116837 -3.0002040863 2.38116837 0.99979556 1.82771361 0.99989772 -0.61723572
		 -3.00071525574 0.004481554 -3.00081729889 0.004481554 0.99918234 -0.61723572 0.99928486
		 1.90211272 6.38196564 2.000000238419 7 -2.9802322e-08 7 1.61803412 5.82443047 1.1755693
		 5.38196564 0.61803436 5.097887039 -2.9802322e-08 5 -2.000000238419 6.99999809 -1.90211511
		 6.38196564 -9.8347664e-07 6.99999809 -1.6180346 5.82442856 -1.17557168 5.38196373
		 -0.61803436 5.097885132 -9.8347664e-07 5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 42 ".pt[0:41]" -type "float3"  -600 200 650 -600 200 650 
		-600 200 650 -600 200 650 -600 200 650 -600 200 650 -600 200.00003 650 -600 200.00003 
		650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650 -600 
		200 650 -600 200.00003 650 -600 200 650 -600 200 650 -600 200 650 -600 200 650 -600 
		200 650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650 
		-600 200.00003 650 -600 200 650 -600 200 650 -600 200 650 -600 200 650 -600 200 650 
		-600 200.00003 650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650 -600 
		200.00003 650 -600 200 650 -600 200 650 -600 200 650 -600 200 650 -600 200.00003 
		650 -600 200.00003 650 -600 200.00003 650 -600 200.00003 650;
	setAttr -s 42 ".vt[0:41]"  800 -200 -650 790.21130371 -200 -711.80322266
		 761.80340576 -200 -767.55712891 717.55706787 -200 -811.80322266 661.80340576 -200 -840.21142578
		 600 -200 -850 800 199.99993896 -650 790.21130371 199.99993896 -711.80322266 761.80340576 199.99993896 -767.55712891
		 717.55706787 199.99993896 -811.80322266 661.80340576 199.99993896 -840.21142578 600 199.99993896 -850
		 600 -200 -650 600 199.99993896 -650 538.19677734 -200 -840.21130371 482.44287109 -200 -811.80340576
		 438.19677734 -200 -767.55706787 409.78857422 -200 -711.80340576 400 -200 -650 538.19677734 199.99993896 -840.21130371
		 482.44287109 199.99993896 -811.80340576 438.19677734 199.99993896 -767.55706787 409.78857422 199.99993896 -711.80340576
		 400 199.99993896 -650 409.78869629 -200 -588.19677734 438.19659424 -200 -532.44287109
		 482.44293213 -200 -488.19677734 538.19659424 -200 -459.78857422 600 -200 -450 409.78869629 199.99993896 -588.19677734
		 438.19659424 199.99993896 -532.44287109 482.44293213 199.99993896 -488.19677734 538.19659424 199.99993896 -459.78857422
		 600 199.99993896 -450 661.80322266 -200 -459.78869629 717.55712891 -200 -488.19659424
		 761.80322266 -200 -532.44293213 790.21142578 -200 -588.19659424 661.80322266 199.99993896 -459.78869629
		 717.55712891 199.99993896 -488.19659424 761.80322266 199.99993896 -532.44293213 790.21142578 199.99993896 -588.19659424;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 11 0 0 6 1 1 7 1 2 8 1 3 9 1 4 10 1 5 11 1 12 0 1 12 1 1 12 2 1 12 3 1
		 12 4 1 12 5 1 6 13 1 7 13 1 8 13 1 9 13 1 10 13 1 11 13 1 5 14 0 14 15 0 15 16 0
		 16 17 0 17 18 0 11 19 0 19 20 0 20 21 0 21 22 0 22 23 0 14 19 1 15 20 1 16 21 1 17 22 1
		 18 23 1 12 14 1 12 15 1 12 16 1 12 17 1 12 18 1 19 13 1 20 13 1 21 13 1 22 13 1 23 13 1
		 18 24 0 24 25 0 25 26 0 26 27 0 27 28 0 23 29 0 29 30 0 30 31 0 31 32 0 32 33 0 24 29 1
		 25 30 1 26 31 1 27 32 1 28 33 1 12 24 1 12 25 1 12 26 1 12 27 1 12 28 1 29 13 1 30 13 1
		 31 13 1 32 13 1 33 13 1 28 34 0 34 35 0 35 36 0 36 37 0 37 0 0 33 38 0 38 39 0 39 40 0
		 40 41 0 41 6 0 34 38 1 35 39 1 36 40 1 37 41 1 12 34 1 12 35 1 12 36 1 12 37 1 38 13 1
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
		mu 0 4 6 7 29 12
		f 4 1 12 -7 -12
		mu 0 4 28 8 14 13
		f 4 2 13 -8 -13
		mu 0 4 8 9 31 14
		f 4 3 14 -9 -14
		mu 0 4 30 10 27 15
		f 4 4 15 -10 -15
		mu 0 4 26 11 17 16
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
		f 4 28 38 -34 -16
		mu 0 4 32 33 34 35
		f 4 29 39 -35 -39
		mu 0 4 36 37 38 39
		f 4 30 40 -36 -40
		mu 0 4 37 40 41 38
		f 4 31 41 -37 -41
		mu 0 4 42 43 44 45
		f 4 32 42 -38 -42
		mu 0 4 46 47 48 49
		f 3 -29 -22 43
		mu 0 3 50 51 52
		f 3 -30 -44 44
		mu 0 3 53 50 52
		f 3 -31 -45 45
		mu 0 3 54 53 52
		f 3 -32 -46 46
		mu 0 3 55 54 52
		f 3 -33 -47 47
		mu 0 3 56 55 52
		f 3 33 48 -28
		mu 0 3 57 58 59
		f 3 34 49 -49
		mu 0 3 58 60 59
		f 3 35 50 -50
		mu 0 3 60 61 59
		f 3 36 51 -51
		mu 0 3 61 62 59
		f 3 37 52 -52
		mu 0 3 62 63 59
		f 4 53 63 -59 -43
		mu 0 4 64 65 66 67
		f 4 54 64 -60 -64
		mu 0 4 68 69 70 71
		f 4 55 65 -61 -65
		mu 0 4 69 72 73 70
		f 4 56 66 -62 -66
		mu 0 4 74 75 76 77
		f 4 57 67 -63 -67
		mu 0 4 78 79 80 81
		f 3 -54 -48 68
		mu 0 3 82 83 84
		f 3 -55 -69 69
		mu 0 3 85 82 84
		f 3 -56 -70 70
		mu 0 3 86 85 84
		f 3 -57 -71 71
		mu 0 3 87 86 84
		f 3 -58 -72 72
		mu 0 3 88 87 84
		f 3 58 73 -53
		mu 0 3 89 90 91
		f 3 59 74 -74
		mu 0 3 90 92 91
		f 3 60 75 -75
		mu 0 3 92 93 91
		f 3 61 76 -76
		mu 0 3 93 94 91
		f 3 62 77 -77
		mu 0 3 94 95 91
		f 4 78 88 -84 -68
		mu 0 4 96 97 98 99
		f 4 79 89 -85 -89
		mu 0 4 100 101 102 103
		f 4 80 90 -86 -90
		mu 0 4 101 104 105 102
		f 4 81 91 -87 -91
		mu 0 4 106 107 108 109
		f 4 82 10 -88 -92
		mu 0 4 110 111 112 113
		f 3 -79 -73 92
		mu 0 3 114 115 116
		f 3 -80 -93 93
		mu 0 3 117 114 116
		f 3 -81 -94 94
		mu 0 3 118 117 116
		f 3 -82 -95 95
		mu 0 3 119 118 116
		f 3 -83 -96 16
		mu 0 3 120 119 116
		f 3 83 96 -78
		mu 0 3 121 122 123
		f 3 84 97 -97
		mu 0 3 122 124 123
		f 3 85 98 -98
		mu 0 3 124 125 123
		f 3 86 99 -99
		mu 0 3 125 126 123
		f 3 87 22 -100
		mu 0 3 126 127 123;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 197;
createNode groupId -n "groupId53";
	rename -uid "492DB223-4A95-8539-8F36-D0A7DAE9C000";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "3C97D3B1-453E-32BE-DD6E-4B858A2DE7A6";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "40521FAD-433C-53A9-80DC-978953AB3B59";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "350A3951-475F-F6ED-7F87-60989263EE01";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode standardSurface -n "Floor_grid";
	rename -uid "FF9B2E2C-419F-74B4-074C-8BB1A9175330";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "00B73D8A-4B80-686C-A0BC-358F8B1F0BBF";
Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "D13EC3A7-4C9D-424C-1E11-3980D84CBD45";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "223BCDE1-4659-9135-E8AC-97B3705A28E4";
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
connectAttr "groupId53.id" "Cylinder_400cmShape.iog.og[1].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Cylinder_400cmShape.iog.og[1].gco"
		;
connectAttr "groupId53.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Cylinder_400cmShape.iog.og[1]" "textureEditorIsolateSelectSet.dsm" 
		-na;
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Cylinder_400cmShape.iog" "standardSurface2SG.dsm" -na;
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
// End of Cylinder_400cm.ma
