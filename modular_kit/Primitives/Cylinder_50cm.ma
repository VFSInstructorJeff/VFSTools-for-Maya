//Maya ASCII 2026 scene
//Name: Cylinder_50cm.ma
//Last modified: Thu, Feb 19, 2026 12:58:42 PM
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
fileInfo "UUID" "6D48A80A-40AA-C92C-1596-22977DC56C9D";
fileInfo "license" "education";
createNode transform -n "Cylinder_50cm";
	rename -uid "26C9B245-4A9B-1EDD-52A7-FFBBC2BD910D";
createNode mesh -n "Cylinder_50cmShape" -p "Cylinder_50cm";
	rename -uid "F4E3052D-48EC-CF91-A8DB-DAAA2D84ACDD";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 10 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "bottom";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[20:39]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottomRing";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 1 "e[0:19]";
	setAttr ".gtag[2].gtagnm" -type "string" "cylBottomCap";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 2 "vtx[0:19]" "vtx[40]";
	setAttr ".gtag[3].gtagnm" -type "string" "cylBottomRing";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 1 "vtx[0:19]";
	setAttr ".gtag[4].gtagnm" -type "string" "cylSides";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 1 "vtx[0:39]";
	setAttr ".gtag[5].gtagnm" -type "string" "cylTopCap";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 2 "vtx[20:39]" "vtx[41]";
	setAttr ".gtag[6].gtagnm" -type "string" "cylTopRing";
	setAttr ".gtag[6].gtagcmp" -type "componentList" 1 "vtx[20:39]";
	setAttr ".gtag[7].gtagnm" -type "string" "sides";
	setAttr ".gtag[7].gtagcmp" -type "componentList" 1 "f[0:19]";
	setAttr ".gtag[8].gtagnm" -type "string" "top";
	setAttr ".gtag[8].gtagcmp" -type "componentList" 1 "f[40:59]";
	setAttr ".gtag[9].gtagnm" -type "string" "topRing";
	setAttr ".gtag[9].gtagcmp" -type "componentList" 1 "e[20:39]";
	setAttr ".pv" -type "double2" -0.0015114769339561462 1.4000001549720764 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 86 ".uvst[0].uvsp[0:85]" -type "float2" -0.078765817 1.16223574
		 -0.14845784 1.19774556 -0.20376582 1.25305367 -0.23927553 1.3227458 -0.25151142 1.4000001
		 -0.23927565 1.47725415 -0.20376582 1.54694629 -0.14845784 1.60225415 -0.078765698
		 1.6377641 -0.0015115259 1.6500001 0.075742774 1.63776422 0.14543478 1.60225415 0.20074277
		 1.54694641 0.23625271 1.47725439 0.24848847 1.4000001 0.23625259 1.3227458 0.20074277
		 1.2530539 0.14543466 1.1977458 0.075742774 1.16223598 -0.0015115259 1.1500001 0.075109065
		 -0.00026857853 -0.58083254 -2.5585294e-05 -0.50642937 -3.8400292e-05 -0.43202594
		 -5.1155686e-05 -0.35762316 -6.3970685e-05 -0.28321981 -7.6726079e-05 -0.2088166 -8.9541078e-05
		 -0.1344136 -0.00010229647 -0.080746047 -0.00011511147 -0.0012841015 -0.00012792647
		 0.075109027 -0.00014068186 0.13141547 -0.00015343726 0.20513813 -0.00016625226 0.27886114
		 -0.00017900765 0.3525835 -0.00019182265 0.42630619 -0.00020457804 0.50002927 -0.00021739304
		 0.57375181 -0.00023020804 0.64747429 -0.00024296343 -0.0012839437 -0.00025570393
		 -0.65515798 0.49998724 -0.58075458 0.49997437 -0.50635141 0.49996161 -0.43194833
		 0.49994886 -0.35754523 0.4999361 -0.28314209 0.49992335 -0.20873915 0.49991047 -0.13433594
		 0.49989772 -0.080746047 0.49988496 -0.0012841015 0.49987209 0.075109042 0.49985945
		 0.13149261 0.49984658 0.20521504 0.4998337 0.27893817 0.49982107 0.35266054 0.49980819
		 0.42638344 0.49979544 0.50010633 0.49978268 0.57382894 0.49976981 -0.080745935 0.49975711
		 -0.0012839437 0.4997443 -0.078765817 1.16223574 -0.14845796 1.19774568 -0.20376582
		 1.25305378 -0.23927589 1.3227458 -0.25151154 1.39999986 -0.23927565 1.47725415 -0.20376582
		 1.54694641 -0.14845796 1.60225427 -0.078765936 1.63776433 -0.0015115259 1.65000021
		 0.075742655 1.63776422 0.14543478 1.60225427 0.20074277 1.54694641 0.23625271 1.47725439
		 0.24848859 1.39999986 0.23625271 1.32274556 0.20074277 1.25305367 0.14543478 1.19774556
		 0.075742655 1.1622355 -0.0015116452 1.1500001 -0.0015115259 1.4000001 -0.0015116452
		 1.39999986 -0.080745935 -0.00024294853 0.64755148 0.49975705 -0.65523559 -1.28299e-05
		 0.075109065 0.49973148;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 42 ".pt[0:41]" -type "float3"  -600 25 0 -600 25 0 -600 
		25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 
		0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 
		-600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 
		25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 
		0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0 -600 25 0;
	setAttr -s 42 ".vt[0:41]"  623.77642822 -25 -7.72542953 620.22546387 -25 -14.69464016
		 614.69464111 -25 -20.22543716 607.72540283 -25 -23.77642632 600 -25 -25.000011444092
		 592.27459717 -25 -23.77642441 585.30535889 -25 -20.22543335 579.77459717 -25 -14.69463539
		 576.22357178 -25 -7.72542667 575 -25 0 576.22357178 -25 7.72542667 579.77459717 -25 14.69463444
		 585.30535889 -25 20.22542763 592.27459717 -25 23.77641678 600 -25 25.000003814697
		 607.72540283 -25 23.77641487 614.69464111 -25 20.22542572 620.22540283 -25 14.69463253
		 623.77642822 -25 7.72542524 625 -25 0 623.77642822 25 -7.72542953 620.22546387 25 -14.69464016
		 614.69464111 25 -20.22543716 607.72540283 25 -23.77642632 600 25 -25.000011444092
		 592.27459717 25 -23.77642441 585.30535889 25 -20.22543335 579.77459717 25 -14.69463539
		 576.22357178 25 -7.72542667 575 25 0 576.22357178 25 7.72542667 579.77459717 25 14.69463444
		 585.30535889 25 20.22542763 592.27459717 25 23.77641678 600 25 25.000003814697 607.72540283 25 23.77641487
		 614.69464111 25 20.22542572 620.22540283 25 14.69463253 623.77642822 25 7.72542524
		 625 25 0 600 -25 0 600 25 0;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 26 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 20 0
		 0 20 1 1 21 1 2 22 1 3 23 1 4 24 1 5 25 1 6 26 1 7 27 1 8 28 1 9 29 1 10 30 1 11 31 1
		 12 32 1 13 33 1 14 34 1 15 35 1 16 36 1 17 37 1 18 38 1 19 39 1 40 0 1 40 1 1 40 2 1
		 40 3 1 40 4 1 40 5 1 40 6 1 40 7 1 40 8 1 40 9 1 40 10 1 40 11 1 40 12 1 40 13 1
		 40 14 1 40 15 1 40 16 1 40 17 1 40 18 1 40 19 1 20 41 1 21 41 1 22 41 1 23 41 1 24 41 1
		 25 41 1 26 41 1 27 41 1 28 41 1 29 41 1 30 41 1 31 41 1 32 41 1 33 41 1 34 41 1 35 41 1
		 36 41 1 37 41 1 38 41 1 39 41 1;
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
		f 4 0 41 -21 -41
		mu 0 4 84 21 41 40
		f 4 1 42 -22 -42
		mu 0 4 21 22 42 41
		f 4 2 43 -23 -43
		mu 0 4 22 23 43 42
		f 4 3 44 -24 -44
		mu 0 4 23 24 44 43
		f 4 4 45 -25 -45
		mu 0 4 24 25 45 44
		f 4 5 46 -26 -46
		mu 0 4 25 26 46 45
		f 4 6 47 -27 -47
		mu 0 4 26 27 47 46
		f 4 7 48 -28 -48
		mu 0 4 27 28 48 47
		f 4 8 49 -29 -49
		mu 0 4 28 29 49 48
		f 4 9 50 -30 -50
		mu 0 4 29 30 50 49
		f 4 10 51 -31 -51
		mu 0 4 30 31 51 50
		f 4 11 52 -32 -52
		mu 0 4 31 32 52 51
		f 4 12 53 -33 -53
		mu 0 4 32 33 53 52
		f 4 13 54 -34 -54
		mu 0 4 33 34 54 53
		f 4 14 55 -35 -55
		mu 0 4 34 35 55 54
		f 4 15 56 -36 -56
		mu 0 4 35 36 56 55
		f 4 16 57 -37 -57
		mu 0 4 36 37 57 56
		f 4 17 58 -38 -58
		mu 0 4 37 38 83 57
		f 4 18 59 -39 -59
		mu 0 4 82 39 59 58
		f 4 19 40 -40 -60
		mu 0 4 39 20 85 59
		f 3 -1 -61 61
		mu 0 3 1 0 80
		f 3 -2 -62 62
		mu 0 3 2 1 80
		f 3 -3 -63 63
		mu 0 3 3 2 80
		f 3 -4 -64 64
		mu 0 3 4 3 80
		f 3 -5 -65 65
		mu 0 3 5 4 80
		f 3 -6 -66 66
		mu 0 3 6 5 80
		f 3 -7 -67 67
		mu 0 3 7 6 80
		f 3 -8 -68 68
		mu 0 3 8 7 80
		f 3 -9 -69 69
		mu 0 3 9 8 80
		f 3 -10 -70 70
		mu 0 3 10 9 80
		f 3 -11 -71 71
		mu 0 3 11 10 80
		f 3 -12 -72 72
		mu 0 3 12 11 80
		f 3 -13 -73 73
		mu 0 3 13 12 80
		f 3 -14 -74 74
		mu 0 3 14 13 80
		f 3 -15 -75 75
		mu 0 3 15 14 80
		f 3 -16 -76 76
		mu 0 3 16 15 80
		f 3 -17 -77 77
		mu 0 3 17 16 80
		f 3 -18 -78 78
		mu 0 3 18 17 80
		f 3 -19 -79 79
		mu 0 3 19 18 80
		f 3 -20 -80 60
		mu 0 3 0 19 80
		f 3 20 81 -81
		mu 0 3 78 77 81
		f 3 21 82 -82
		mu 0 3 77 76 81
		f 3 22 83 -83
		mu 0 3 76 75 81
		f 3 23 84 -84
		mu 0 3 75 74 81
		f 3 24 85 -85
		mu 0 3 74 73 81
		f 3 25 86 -86
		mu 0 3 73 72 81
		f 3 26 87 -87
		mu 0 3 72 71 81
		f 3 27 88 -88
		mu 0 3 71 70 81
		f 3 28 89 -89
		mu 0 3 70 69 81
		f 3 29 90 -90
		mu 0 3 69 68 81
		f 3 30 91 -91
		mu 0 3 68 67 81
		f 3 31 92 -92
		mu 0 3 67 66 81
		f 3 32 93 -93
		mu 0 3 66 65 81
		f 3 33 94 -94
		mu 0 3 65 64 81
		f 3 34 95 -95
		mu 0 3 64 63 81
		f 3 35 96 -96
		mu 0 3 63 62 81
		f 3 36 97 -97
		mu 0 3 62 61 81
		f 3 37 98 -98
		mu 0 3 61 60 81
		f 3 38 99 -99
		mu 0 3 60 79 81
		f 3 39 80 -100
		mu 0 3 79 78 81;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 4 
		20 0 
		39 0 
		40 0 
		59 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode materialInfo -n "materialInfo2";
	rename -uid "2C0CF6AD-4A03-5ED1-1DD6-EF85E1D12F82";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "A38F5FF6-4159-F1A0-B110-3483D4FB2A7C";
	setAttr ".ihi" 0;
	setAttr -s 113 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
createNode standardSurface -n "Floor_grid";
	rename -uid "63142EDA-46BE-7199-01B9-00888BAFB2B6";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "9D3E9B89-4A13-0729-43F3-0A8EA4BA652A";
Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "A038A168-46D5-CDBF-23A0-97B788DBD080";
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
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Torus_50cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Torus_100cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Torus_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Torus_400cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Sphere_50cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cylinder_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cylinder_100cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cone_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cone_50cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cube_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cylinder_400cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cone_100cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Sphere_100cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cube_400cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cube_50cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cube_100cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Sphere_400cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cylinder_50cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Sphere_200cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Cone_400cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|FloorShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|BF02_FloorShape2.ciog.cog[0]" "standardSurface2SG.dsm" -na;
connectAttr "|BF02_FloorShape2.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|StairsLanding_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_32Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_18Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_19Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_20Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_21Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_22Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_23Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_24Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_25Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_26Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_27Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_28Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_29Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_30Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_31Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_32Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_18Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_19Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_20Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_21Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_22Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_23Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_24Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_25Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_26Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_27Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_28Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_29Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_30Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_31Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|FloorShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_02Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_03Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_04Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_05Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_06Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_07Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_08Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_09Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_10Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs_11Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|StairsLanding_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|BF02_FloorShape2.iog" "standardSurface2SG.dsm" -na;
connectAttr "|BF02_FloorShape2.ciog.cog[1]" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_32Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_18Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_19Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_20Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_21Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_22Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_23Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_24Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_25Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_26Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_27Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_28Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_29Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_30Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_31Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|StairsLanding_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_32Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_18Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_19Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_20Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_21Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_22Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_23Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_24Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_25Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_26Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_27Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_28Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_29Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_30Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|Stairs_31Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "|StairsLanding_01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "BF01_Floor01Shape.iog" "standardSurface2SG.dsm" -na;
connectAttr "BF02_FloorShape1.iog" "standardSurface2SG.dsm" -na;
connectAttr "BF02_FloorShape1.ciog.cog[1]" "standardSurface2SG.dsm" -na;
connectAttr "Stairs01LandingShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "Stairs01Shape1.ciog.cog[0]" "standardSurface2SG.dsm" -na;
connectAttr "Stairs01Shape1.iog.og[0]" "standardSurface2SG.dsm" -na;
connectAttr "StairSecondFloor_Boolean_W525xH200cmShape.iog" "standardSurface2SG.dsm"
		 -na;
connectAttr "Cube_25cmShape.iog" "standardSurface2SG.dsm" -na;
connectAttr "groupId162.msg" "standardSurface2SG.gn" -na;
connectAttr "groupId895.msg" "standardSurface2SG.gn" -na;
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
// End of Cylinder_50cm.ma
