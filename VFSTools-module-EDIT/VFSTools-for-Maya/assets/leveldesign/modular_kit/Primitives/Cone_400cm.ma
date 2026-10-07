//Maya ASCII 2026 scene
//Name: Cone_400cm.ma
//Last modified: Thu, Feb 19, 2026 01:03:39 PM
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
fileInfo "UUID" "CEAB831D-4099-16A1-3485-4F87037EC296";
fileInfo "license" "education";
createNode transform -n "Cone_400cm";
	rename -uid "5E1A7F52-48E0-FE6D-2513-DDB71CF72E92";
createNode mesh -n "Cone_400cmShape" -p "Cone_400cm";
	rename -uid "D8872413-45A5-F060-6E1B-2CA119DE6D3C";
	setAttr -k off ".v";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 4 "f[2]" "f[12]" "f[22]" "f[32]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "sides";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[0:39]";
	setAttr ".pv" -type "double2" -0.75044757127761841 0.99999868869781494 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 88 ".uvst[0].uvsp[0:87]" -type "float2" -0.63010585 -3 0
		 -3 0 1 -1.78671074 -2.99999857 -1.20864296 -2.99999857 -1.50089514 0.99999821 -1.37634861
		 -3.000005722046 -0.83421367 -3.000005722046 -1.37634861 1.000004768372 -1.19388604
		 -2.99999976 -0.61866868 -2.99999976 -0.61866868 0.99999917 0 -3 0.61991382 -3 0 0.99999261
		 0 5 0 3.000001907349 0.61803436 3.097887039 1.17556906 3.38197517 1.61803246 3.82443333
		 1.90211105 4.38196754 1.99999809 5 -0.63010585 -3 0 -3 0 1 -1.78671074 -2.99999857
		 -1.20864296 -2.99999857 -1.50089514 0.99999821 -1.37634861 -3.000005722046 -0.83421367
		 -3.000005722046 -1.37634861 1.000004768372 -1.19388604 -2.99999976 -0.61866868 -2.99999976
		 -0.61866868 0.99999917 0 -3 0.61991382 -3 0 0.99999261 0 3.000001907349 0.61803436
		 3.097887039 0 5 1.17556906 3.38197517 1.61803246 3.82443333 1.90211105 4.38196754
		 1.99999809 5 -0.63010585 -3 0 -3 0 1 -1.78671074 -2.99999857 -1.20864296 -2.99999857
		 -1.50089514 0.99999821 -1.37634861 -3.000005722046 -0.83421367 -3.000005722046 -1.37634861
		 1.000004768372 -1.19388604 -2.99999976 -0.61866868 -2.99999976 -0.61866868 0.99999917
		 0 -3 0.61991382 -3 0 0.99999261 0 3.000001907349 0.61803436 3.097887039 0 5 1.17556906
		 3.38197517 1.61803246 3.82443333 1.90211105 4.38196754 1.99999809 5 -0.63010585 -3
		 0 -3 0 1 -1.78671074 -2.99999857 -1.20864296 -2.99999857 -1.50089514 0.99999821 -1.37634861
		 -3.000005722046 -0.83421367 -3.000005722046 -1.37634861 1.000004768372 -1.19388604
		 -2.99999976 -0.61866868 -2.99999976 -0.61866868 0.99999917 0 -3 0.61991382 -3 0 0.99999261
		 0 3.000001907349 0.61803436 3.097887039 0 5 1.17556906 3.38197517 1.61803246 3.82443333
		 1.90211105 4.38196754 1.99999809 5;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".pt[0:21]" -type "float3"  -1050 199.99997 650 -1050 
		200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 
		200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 
		200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 200 650 -1050 
		200 650 -1050 200 650 -1050 200 650;
	setAttr -s 22 ".vt[0:21]"  1050 200 -650 1250 -200 -650 1050 -200 -650
		 1111.8034668 -200 -840.21142578 1050 -200 -850 1211.8034668 -200 -767.55712891 1167.55712891 -200 -811.80322266
		 1240.21130371 -200 -711.80322266 850 -200 -650 988.19659424 -200 -459.78857422 1050 -200 -450
		 888.19659424 -200 -532.44287109 932.44293213 -200 -488.19677734 859.78869629 -200 -588.19677734
		 859.78857422 -200 -711.80340576 932.44287109 -200 -811.80340576 888.19677734 -200 -767.55706787
		 988.19677734 -200 -840.21130371 1240.21142578 -200 -588.19659424 1167.55712891 -200 -488.19659424
		 1211.80322266 -200 -532.44293213 1111.80322266 -200 -459.78866577;
	setAttr -s 60 ".ed[0:59]"  1 0 1 1 2 1 3 4 0 3 0 1 4 0 1 5 6 0 5 0 1
		 6 0 1 7 5 0 7 0 1 6 3 0 1 7 0 3 2 1 4 2 1 5 2 1 6 2 1 7 2 1 8 0 1 8 2 1 9 10 0 9 0 1
		 10 0 1 11 12 0 11 0 1 12 0 1 13 11 0 13 0 1 12 9 0 8 13 0 9 2 1 10 2 1 11 2 1 12 2 1
		 13 2 1 14 8 0 14 0 1 15 16 0 15 0 1 16 0 1 17 15 0 17 0 1 16 14 0 4 17 0 14 2 1 15 2 1
		 16 2 1 17 2 1 18 1 0 18 0 1 19 20 0 19 0 1 20 0 1 21 19 0 21 0 1 20 18 0 10 21 0
		 18 2 1 19 2 1 20 2 1 21 2 1;
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
		f 3 19 21 -21
		mu 0 3 22 23 24
		f 3 22 24 -24
		mu 0 3 25 26 27
		f 3 25 23 -27
		mu 0 3 28 29 30
		f 3 27 20 -25
		mu 0 3 31 32 33
		f 3 28 26 -18
		mu 0 3 34 35 36
		f 3 -20 29 -31
		mu 0 3 37 38 39
		f 3 -23 31 -33
		mu 0 3 40 41 39
		f 3 -26 33 -32
		mu 0 3 41 42 39
		f 3 -28 32 -30
		mu 0 3 38 40 39
		f 3 -29 18 -34
		mu 0 3 42 43 39
		f 3 34 17 -36
		mu 0 3 44 45 46
		f 3 36 38 -38
		mu 0 3 47 48 49
		f 3 39 37 -41
		mu 0 3 50 51 52
		f 3 41 35 -39
		mu 0 3 53 54 55
		f 3 42 40 -5
		mu 0 3 56 57 58
		f 3 -35 43 -19
		mu 0 3 59 60 61
		f 3 -37 44 -46
		mu 0 3 62 63 61
		f 3 -40 46 -45
		mu 0 3 63 64 61
		f 3 -42 45 -44
		mu 0 3 60 62 61
		f 3 -43 13 -47
		mu 0 3 64 65 61
		f 3 47 0 -49
		mu 0 3 66 67 68
		f 3 49 51 -51
		mu 0 3 69 70 71
		f 3 52 50 -54
		mu 0 3 72 73 74
		f 3 54 48 -52
		mu 0 3 75 76 77
		f 3 55 53 -22
		mu 0 3 78 79 80
		f 3 -48 56 -2
		mu 0 3 81 82 83
		f 3 -50 57 -59
		mu 0 3 84 85 83
		f 3 -53 59 -58
		mu 0 3 85 86 83
		f 3 -55 58 -57
		mu 0 3 82 84 83
		f 3 -56 30 -60
		mu 0 3 86 87 83;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 221;
createNode groupId -n "groupId47";
	rename -uid "4046E6D8-47AB-FBF6-54D2-C98BC42D9850";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "3388F02D-47F3-B8C0-A1CF-3F871EBA078C";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "BEFE008D-428C-C33C-E6F8-34ABFBFAD0CF";
createNode shadingEngine -n "standardSurface2SG";
	rename -uid "C0F33043-4B82-0F74-3E29-02AB749EB8AB";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode standardSurface -n "Floor_grid";
	rename -uid "A0A2E6BC-4639-6C4B-1412-C7BD36424D14";
	setAttr ".sr" 1;
createNode file -n "file1";
	rename -uid "8357BF3D-4D49-E622-C1DF-5BB54B479739";
Floor_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "4AECBA54-4DAD-F1F2-C85D-91B5A7D94E59";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "416EA0F3-4D40-D933-822C-029BCB9D4B5B";
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
connectAttr "groupId47.id" "Cone_400cmShape.iog.og[1].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Cone_400cmShape.iog.og[1].gco";
connectAttr "groupId47.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Cone_400cmShape.iog.og[1]" "textureEditorIsolateSelectSet.dsm" -na;
connectAttr "standardSurface2SG.msg" "materialInfo2.sg";
connectAttr "Floor_grid.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr "Floor_grid.oc" "standardSurface2SG.ss";
connectAttr "Cone_400cmShape.iog" "standardSurface2SG.dsm" -na;
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
// End of Cone_400cm.ma
