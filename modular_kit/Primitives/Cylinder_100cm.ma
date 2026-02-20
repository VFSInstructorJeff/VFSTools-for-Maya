//Maya ASCII 2026 scene
//Name: Cylinder_100cm.ma
//Last modified: Thu, Feb 19, 2026 12:59:56 PM
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
fileInfo "UUID" "FEC9DBDE-4BCD-95F7-7C67-34883C3B5A7D";
fileInfo "license" "education";
createNode transform -n "Cylinder_100cm";
	rename -uid "1279D215-424F-D8B7-C67D-768FE3AD143D";
createNode mesh -n "Cylinder_100cmShape" -p "Cylinder_100cm";
	rename -uid "D3D9A000-42AF-A2BE-5588-10B44EA3F39C";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 4 "f[0]" "f[15]" "f[30]" "f[45]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 10 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "bottom";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 4 "f[5:9]" "f[20:24]" "f[35:39]" "f[50:54]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottomRing";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 4 "e[0:4]" "e[28:32]" "e[56:60]" "e[78:82]";
	setAttr ".gtag[2].gtagnm" -type "string" "cylBottomCap";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 5 "vtx[0:5]" "vtx[12]" "vtx[14:19]" "vtx[26:29]" "vtx[34:37]";
	setAttr ".gtag[3].gtagnm" -type "string" "cylBottomRing";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 4 "vtx[0:5]" "vtx[14:19]" "vtx[26:29]" "vtx[34:37]";
	setAttr ".gtag[4].gtagnm" -type "string" "cylSides";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 2 "vtx[0:11]" "vtx[14:41]";
	setAttr ".gtag[5].gtagnm" -type "string" "cylTopCap";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 5 "vtx[6:11]" "vtx[13]" "vtx[20:25]" "vtx[30:33]" "vtx[38:41]";
	setAttr ".gtag[6].gtagnm" -type "string" "cylTopRing";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 4 "vtx[6:11]" "vtx[20:25]" "vtx[30:33]" "vtx[38:41]";
	setAttr ".gtag[7].gtagnm" -type "string" "sides";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 4 "f[0:4]" "f[15:19]" "f[30:34]" "f[45:49]";
	setAttr ".gtag[8].gtagnm" -type "string" "top";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 4 "f[10:14]" "f[25:29]" "f[40:44]" "f[55:59]";
	setAttr ".gtag[9].gtagnm" -type "string" "topRing";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 4 "e[5:9]" "e[33:37]" "e[61:65]" "e[83:87]";
	setAttr ".pv" -type "double2" 0.54016019403934479 0.50016605854034424 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 122 ".uvst[0].uvsp[0:121]" -type "float2" 0.50081903 3 0.47634724
		 2.84549141 0.40532759 2.70610762 0.29471138 2.59549141 0.1553276 2.52447176 0.00081900402
		 2.5 -3.5762787e-07 0.00012779236 0.14744508 0.00010228157 0.29836065 0.00020444393
		 0.44839618 0.00017881393 0.63192421 0.00015330315 0.0012741685 0 0.00015377998 1.00012779236
		 0.15421462 1.00023007393 0.29836065 1.00020456314 0.44839618 1.00017881393 -0.15764982
		 1.000025629997 0.0012741685 1 -0.15368958 2.52447128 -0.29307386 2.59549093 -0.40368959
		 2.70610714 -0.47470972 2.84549141 -0.49918103 2.99999952 0.00081876561 2.5 0.00081900402
		 3 0.00081876561 2.99999952 -0.15764982 2.5510788e-05 0.63192421 1.00015330315 0.15406013
		 0.00023007393 0.14744508 1.00010228157 -3.5762787e-07 0.00012779236 0.14744508 0.00010228157
		 0.14744508 1.00010228157 0.00015377998 1.00012779236 0.15406013 0.00023007393 0.29836065
		 0.00020444393 0.29836065 1.00020456314 0.15421462 1.00023007393 0.44839618 0.00017881393
		 0.44839618 1.00017881393 0.63192421 0.00015330315 0.63192421 1.00015330315 -0.15764982
		 2.5510788e-05 0.0012741685 0 0.0012741685 1 -0.15764982 1.000025629997 0.47634724
		 2.84549141 0.50081903 3 0.00081900402 3 0.40532759 2.70610762 0.29471138 2.59549141
		 0.1553276 2.52447176 0.00081900402 2.5 -0.49918103 2.99999952 -0.47470972 2.84549141
		 0.00081876561 2.99999952 -0.40368959 2.70610714 -0.29307386 2.59549093 -0.15368958
		 2.52447128 0.00081876561 2.5 -3.5762787e-07 0.00012779236 0.14744508 0.00010228157
		 0.14744508 1.00010228157 0.00015377998 1.00012779236 0.15406013 0.00023007393 0.29836065
		 0.00020444393 0.29836065 1.00020456314 0.15421462 1.00023007393 0.44839618 0.00017881393
		 0.44839618 1.00017881393 0.63192421 0.00015330315 0.63192421 1.00015330315 -0.15764982
		 2.5510788e-05 0.0012741685 0 0.0012741685 1 -0.15764982 1.000025629997 0.47634724
		 2.84549141 0.50081903 3 0.00081900402 3 0.40532759 2.70610762 0.29471138 2.59549141
		 0.1553276 2.52447176 0.00081900402 2.5 -0.49918103 2.99999952 -0.47470972 2.84549141
		 0.00081876561 2.99999952 -0.40368959 2.70610714 -0.29307386 2.59549093 -0.15368958
		 2.52447128 0.00081876561 2.5 -3.5762787e-07 0.00012779236 0.14744508 0.00010228157
		 0.14744508 1.00010228157 0.00015377998 1.00012779236 0.15406013 0.00023007393 0.29836065
		 0.00020444393 0.29836065 1.00020456314 0.15421462 1.00023007393 0.44839618 0.00017881393
		 0.44839618 1.00017881393 0.63192421 0.00015330315 0.63192421 1.00015330315 -0.15764982
		 2.5510788e-05 0.0012741685 0 0.0012741685 1 -0.15764982 1.000025629997 0.47634724
		 2.84549141 0.50081903 3 0.00081900402 3 0.40532759 2.70610762 0.29471138 2.59549141
		 0.1553276 2.52447176 0.00081900402 2.5 -0.49918103 2.99999952 -0.47470972 2.84549141
		 0.00081876561 2.99999952 -0.40368959 2.70610714 -0.29307386 2.59549093 -0.15368958
		 2.52447128 0.00081876561 2.5 0.29836065 0.00020444393 0.29836065 1.00020456314;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 42 ".pt[0:41]" -type "float3"  -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100 -650 
		50 100 -650 50 100 -650 50 100 -650 50 100 -650 50 100;
	setAttr -s 42 ".vt[0:41]"  650 -50 -50 665.45080566 -50 -52.44717407
		 679.38928223 -50 -59.54914856 690.45080566 -50 -70.61073303 697.55285645 -50 -84.54914856
		 700 -50 -100 650 50 -50 665.45080566 50 -52.44717407 679.38928223 50 -59.54914856
		 690.45080566 50 -70.61073303 697.55285645 50 -84.54914856 700 50 -100 650 -50 -100
		 650 50 -100 650 -50 -150 634.54919434 -50 -147.55282593 620.61071777 -50 -140.45083618
		 609.54919434 -50 -129.38926697 602.44714355 -50 -115.45085144 600 -50 -100 650 50 -150
		 634.54919434 50 -147.55282593 620.61071777 50 -140.45083618 609.54919434 50 -129.38926697
		 602.44714355 50 -115.45085144 600 50 -100 697.55285645 -50 -115.45080566 690.4508667 -50 -129.38928223
		 679.38928223 -50 -140.45082092 665.4508667 -50 -147.5528717 697.55285645 50 -115.45080566
		 690.4508667 50 -129.38928223 679.38928223 50 -140.45082092 665.4508667 50 -147.5528717
		 602.44714355 -50 -84.54919434 609.5491333 -50 -70.61071777 620.61071777 -50 -59.54919434
		 634.5491333 -50 -52.44714355 602.44714355 50 -84.54919434 609.5491333 50 -70.61071777
		 620.61071777 50 -59.54919434 634.5491333 50 -52.44714355;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 6 7 0 7 8 0
		 8 9 0 9 10 0 10 11 0 0 6 1 1 7 1 2 8 1 3 9 1 4 10 1 5 11 1 12 0 1 12 1 1 12 2 1 12 3 1
		 12 4 1 12 5 1 6 13 1 7 13 1 8 13 1 9 13 1 10 13 1 11 13 1 14 15 0 15 16 0 16 17 0
		 17 18 0 18 19 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 14 20 1 15 21 1 16 22 1 17 23 1
		 18 24 1 19 25 1 12 14 1 12 15 1 12 16 1 12 17 1 12 18 1 12 19 1 20 13 1 21 13 1 22 13 1
		 23 13 1 24 13 1 25 13 1 5 26 0 26 27 0 27 28 0 28 29 0 29 14 0 11 30 0 30 31 0 31 32 0
		 32 33 0 33 20 0 26 30 1 27 31 1 28 32 1 29 33 1 12 26 1 12 27 1 12 28 1 12 29 1 30 13 1
		 31 13 1 32 13 1 33 13 1 19 34 0 34 35 0 35 36 0 36 37 0 37 0 0 25 38 0 38 39 0 39 40 0
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
		mu 0 4 28 8 121 13
		f 4 2 13 -8 -13
		mu 0 4 120 9 15 14
		f 4 3 14 -9 -14
		mu 0 4 9 10 27 15
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
		f 4 28 39 -34 -39
		mu 0 4 30 31 32 33
		f 4 29 40 -35 -40
		mu 0 4 34 35 36 37
		f 4 30 41 -36 -41
		mu 0 4 35 38 39 36
		f 4 31 42 -37 -42
		mu 0 4 38 40 41 39
		f 4 32 43 -38 -43
		mu 0 4 42 43 44 45
		f 3 -29 -45 45
		mu 0 3 46 47 48
		f 3 -30 -46 46
		mu 0 3 49 46 48
		f 3 -31 -47 47
		mu 0 3 50 49 48
		f 3 -32 -48 48
		mu 0 3 51 50 48
		f 3 -33 -49 49
		mu 0 3 52 51 48
		f 3 33 51 -51
		mu 0 3 53 54 55
		f 3 34 52 -52
		mu 0 3 54 56 55
		f 3 35 53 -53
		mu 0 3 56 57 55
		f 3 36 54 -54
		mu 0 3 57 58 55
		f 3 37 55 -55
		mu 0 3 58 59 55
		f 4 56 66 -62 -16
		mu 0 4 60 61 62 63
		f 4 57 67 -63 -67
		mu 0 4 64 65 66 67
		f 4 58 68 -64 -68
		mu 0 4 65 68 69 66
		f 4 59 69 -65 -69
		mu 0 4 68 70 71 69
		f 4 60 38 -66 -70
		mu 0 4 72 73 74 75
		f 3 -57 -22 70
		mu 0 3 76 77 78
		f 3 -58 -71 71
		mu 0 3 79 76 78
		f 3 -59 -72 72
		mu 0 3 80 79 78
		f 3 -60 -73 73
		mu 0 3 81 80 78
		f 3 -61 -74 44
		mu 0 3 82 81 78
		f 3 61 74 -28
		mu 0 3 83 84 85
		f 3 62 75 -75
		mu 0 3 84 86 85
		f 3 63 76 -76
		mu 0 3 86 87 85
		f 3 64 77 -77
		mu 0 3 87 88 85
		f 3 65 50 -78
		mu 0 3 88 89 85
		f 4 78 88 -84 -44
		mu 0 4 90 91 92 93
		f 4 79 89 -85 -89
		mu 0 4 94 95 96 97
		f 4 80 90 -86 -90
		mu 0 4 95 98 99 96
		f 4 81 91 -87 -91
		mu 0 4 98 100 101 99
		f 4 82 10 -88 -92
		mu 0 4 102 103 104 105
		f 3 -79 -50 92
		mu 0 3 106 107 108
		f 3 -80 -93 93
		mu 0 3 109 106 108
		f 3 -81 -94 94
		mu 0 3 110 109 108
		f 3 -82 -95 95
		mu 0 3 111 110 108
		f 3 -83 -96 16
		mu 0 3 112 111 108
		f 3 83 96 -56
		mu 0 3 113 114 115
		f 3 84 97 -97
		mu 0 3 114 116 115
		f 3 85 98 -98
		mu 0 3 116 117 115
		f 3 86 99 -99
		mu 0 3 117 118 115
		f 3 87 22 -100
		mu 0 3 118 119 115;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 101;
createNode groupId -n "groupId100";
	rename -uid "572E05A8-4C1F-0261-760F-D587008824C2";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "C5D0B962-4B55-1B71-30E8-1196645431B9";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "3F2B2C76-4014-4B14-4C8E-988A83E15BB7";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "C0858DA2-4FDA-24FE-27F2-C1AB346067D3";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode standardSurface -n "Floor_grid";
	rename -uid "927156C0-4E3B-1103-8F44-B098ECD34C41";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "05E21DD6-476A-9396-B605-8E9E38CF1D1B";
	setAttr ".ftn" -type "string" "G:/My Drive/[03] CURRICULUM/[XX] ART ASSETS/[3] ENVIRONMENTS/LD_Tools/RaysGridTextures/Shaders/LD_MATS/Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "15CC1084-4466-A1BC-4531-0093EC156352";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "2DBE7767-4C32-B839-3E8F-4C9268597AA6";
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
connectAttr "groupId100.id" "Cylinder_100cmShape.iog.og[0].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Cylinder_100cmShape.iog.og[0].gco"
		;
connectAttr "groupId100.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Cylinder_100cmShape.iog.og[0]" "textureEditorIsolateSelectSet.dsm" 
		-na;
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Cylinder_100cmShape.iog" "standardSurface2SG.dsm" -na;
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
// End of Cylinder_100cm.ma
