//Maya ASCII 2026 scene
//Name: Cone_200cm.ma
//Last modified: Thu, Feb 19, 2026 01:03:09 PM
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
fileInfo "UUID" "DE31B961-42AE-6B4B-98BC-8A82B5EA4A35";
fileInfo "license" "education";
createNode transform -n "Cone_200cm";
	rename -uid "55A5E472-41BC-93E7-2E48-2F855F2951DA";
createNode mesh -n "Cone_200cmShape" -p "Cone_200cm";
	rename -uid "2AE2D590-4BBA-4096-5CE6-9B8FF9EF3443";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:39]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 4 "f[0]" "f[10]" "f[20]" "f[30]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "sides";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[0:39]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 88 ".uvst[0].uvsp[0:87]" -type "float2" -0.31505293 -1 0
		 -1 0 1 -0.89335537 -0.99999928 -0.60432148 -0.99999928 -0.75044757 0.99999911 -0.89928532
		 -1.000002861023 -0.67682475 -1.000002861023 -0.89928532 1.000002384186 -0.59839153
		 -0.99999988 -0.29919481 -0.99999988 -0.29919481 0.99999958 0 -1 0.30995691 -1 0 0.9999963
		 2.9802322e-08 3 2.9802322e-08 2.000000953674 0.30901721 2.04894352 0.58778453 2.19098759
		 0.80901623 2.41221666 0.95105553 2.69098377 0.99999905 3 -0.31505293 -1 0 -1 0 1
		 -0.89335537 -0.99999928 -0.60432148 -0.99999928 -0.75044757 0.99999911 -0.89928532
		 -1.000002861023 -0.67682475 -1.000002861023 -0.89928532 1.000002384186 -0.59839153
		 -0.99999988 -0.29919481 -0.99999988 -0.29919481 0.99999958 0 -1 0.30995691 -1 0 0.9999963
		 2.9802322e-08 2.000000953674 0.30901721 2.04894352 2.9802322e-08 3 0.58778453 2.19098759
		 0.80901623 2.41221666 0.95105553 2.69098377 0.99999905 3 -0.31505293 -1 0 -1 0 1
		 -0.89335537 -0.99999928 -0.60432148 -0.99999928 -0.75044757 0.99999911 -0.89928532
		 -1.000002861023 -0.67682475 -1.000002861023 -0.89928532 1.000002384186 -0.59839153
		 -0.99999988 -0.29919481 -0.99999988 -0.29919481 0.99999958 0 -1 0.30995691 -1 0 0.9999963
		 2.9802322e-08 2.000000953674 0.30901721 2.04894352 2.9802322e-08 3 0.58778453 2.19098759
		 0.80901623 2.41221666 0.95105553 2.69098377 0.99999905 3 -0.31505293 -1 0 -1 0 1
		 -0.89335537 -0.99999928 -0.60432148 -0.99999928 -0.75044757 0.99999911 -0.89928532
		 -1.000002861023 -0.67682475 -1.000002861023 -0.89928532 1.000002384186 -0.59839153
		 -0.99999988 -0.29919481 -0.99999988 -0.29919481 0.99999958 0 -1 0.30995691 -1 0 0.9999963
		 2.9802322e-08 2.000000953674 0.30901721 2.04894352 2.9802322e-08 3 0.58778453 2.19098759
		 0.80901623 2.41221666 0.95105553 2.69098377 0.99999905 3;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".pt[0:21]" -type "float3"  -1000 100 300 -1000 100 300 
		-1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 
		-1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 
		-1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 -1000 100 300 
		-1000 100 300 -1000 100 300;
	setAttr -s 22 ".vt[0:21]"  1000 100 -300 1000 -100 -199.99998474 1000 -100 -300
		 1095.10571289 -100 -269.098297119 1100 -100 -300 1058.77856445 -100 -219.098297119
		 1080.90161133 -100 -241.22146606 1030.90161133 -100 -204.89433289 1030.9017334 -100 -395.10571289
		 1000 -100 -400 1080.9017334 -100 -358.77856445 1058.77856445 -100 -380.90161133 1095.10571289 -100 -330.90161133
		 900 -100 -300 969.098266602 -100 -204.89428711 919.098266602 -100 -241.22143555 941.22143555 -100 -219.098388672
		 904.89434814 -100 -269.098388672 904.89428711 -100 -330.90170288 941.22143555 -100 -380.90170288
		 919.098388672 -100 -358.77853394 969.098388672 -100 -395.10565186;
	setAttr -s 60 ".ed[0:59]"  1 0 1 1 2 1 3 4 0 3 0 1 4 0 1 5 6 0 5 0 1
		 6 0 1 7 5 0 7 0 1 6 3 0 1 7 0 3 2 1 4 2 1 5 2 1 6 2 1 7 2 1 8 9 0 8 0 1 9 0 1 10 11 0
		 10 0 1 11 0 1 12 10 0 12 0 1 11 8 0 4 12 0 8 2 1 9 2 1 10 2 1 11 2 1 12 2 1 13 0 1
		 13 2 1 14 1 0 14 0 1 15 16 0 15 0 1 16 0 1 17 15 0 17 0 1 16 14 0 13 17 0 14 2 1
		 15 2 1 16 2 1 17 2 1 18 13 0 18 0 1 19 20 0 19 0 1 20 0 1 21 19 0 21 0 1 20 18 0
		 9 21 0 18 2 1 19 2 1 20 2 1 21 2 1;
	setAttr -s 42 ".n[0:41]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 40 -ch 120 ".fc[0:39]" -type "polyFaces" 
		f 3 2 4 -4
		mu 0 3 0 1 2
		f 3 5 7 -7
		mu 0 3 3 4 5
		f 3 8 6 -10
		mu 0 3 6 7 8
		f 3 10 3 -8
		mu 0 3 9 10 11
		f 3 11 9 -1
		mu 0 3 12 13 14
		f 3 -3 12 -14
		mu 0 3 16 17 15
		f 3 -6 14 -16
		mu 0 3 18 19 15
		f 3 -9 16 -15
		mu 0 3 19 20 15
		f 3 -11 15 -13
		mu 0 3 17 18 15
		f 3 -12 1 -17
		mu 0 3 20 21 15
		f 3 17 19 -19
		mu 0 3 22 23 24
		f 3 20 22 -22
		mu 0 3 25 26 27
		f 3 23 21 -25
		mu 0 3 28 29 30
		f 3 25 18 -23
		mu 0 3 31 32 33
		f 3 26 24 -5
		mu 0 3 34 35 36
		f 3 -18 27 -29
		mu 0 3 37 38 39
		f 3 -21 29 -31
		mu 0 3 40 41 39
		f 3 -24 31 -30
		mu 0 3 41 42 39
		f 3 -26 30 -28
		mu 0 3 38 40 39
		f 3 -27 13 -32
		mu 0 3 42 43 39
		f 3 34 0 -36
		mu 0 3 44 45 46
		f 3 36 38 -38
		mu 0 3 47 48 49
		f 3 39 37 -41
		mu 0 3 50 51 52
		f 3 41 35 -39
		mu 0 3 53 54 55
		f 3 42 40 -33
		mu 0 3 56 57 58
		f 3 -35 43 -2
		mu 0 3 59 60 61
		f 3 -37 44 -46
		mu 0 3 62 63 61
		f 3 -40 46 -45
		mu 0 3 63 64 61
		f 3 -42 45 -44
		mu 0 3 60 62 61
		f 3 -43 33 -47
		mu 0 3 64 65 61
		f 3 47 32 -49
		mu 0 3 66 67 68
		f 3 49 51 -51
		mu 0 3 69 70 71
		f 3 52 50 -54
		mu 0 3 72 73 74
		f 3 54 48 -52
		mu 0 3 75 76 77
		f 3 55 53 -20
		mu 0 3 78 79 80
		f 3 -48 56 -34
		mu 0 3 81 82 83
		f 3 -50 57 -59
		mu 0 3 84 85 83
		f 3 -53 59 -58
		mu 0 3 85 86 83
		f 3 -55 58 -57
		mu 0 3 82 84 83
		f 3 -56 28 -60
		mu 0 3 86 87 83;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 202;
createNode groupId -n "groupId28";
	rename -uid "289FB25E-4873-4BF0-9891-6583C65C8BB2";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "6FC1FE70-429E-D505-ADBA-49AB489CDB1E";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "FE3B8BE7-410F-2690-50E9-75AE73F459E3";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "28E20853-4D22-6C23-1A5F-4E957B7E56CF";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode standardSurface -n "Floor_grid";
	rename -uid "7DC731D9-4DC5-CEA0-D0E7-EDBCD2288A6B";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "4CBED53C-4592-35A8-92AB-54923749166F";
Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "A7F199BA-4D5A-A687-2442-F5B644037819";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "3E32E456-450B-19DD-C48B-1797C9151A87";
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
connectAttr "groupId28.id" "Cone_200cmShape.iog.og[1].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Cone_200cmShape.iog.og[1].gco";
connectAttr "groupId28.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Cone_200cmShape.iog.og[1]" "textureEditorIsolateSelectSet.dsm" -na;
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Cone_200cmShape.iog" "standardSurface2SG.dsm" -na;
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
// End of Cone_200cm.ma
