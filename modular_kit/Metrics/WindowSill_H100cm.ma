//Maya ASCII 2026 scene
//Name: WindowSill_H100cm.ma
//Last modified: Thu, Feb 19, 2026 01:08:10 PM
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
fileInfo "UUID" "F53A257F-447A-2A90-140E-859469A2A575";
fileInfo "license" "education";
createNode transform -n "WindowSill_H100cm";
	rename -uid "BC00AF54-4B97-33F9-598E-AA9AE5D9C3A3";
createNode mesh -n "WindowSill_H100cmShape" -p "WindowSill_H100cm";
	rename -uid "7A263C56-4079-8551-729D-7DA478452F9A";
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
	setAttr ".pv" -type "double2" 0.50000211596488953 -0.49999936717404125 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" 1.000000834465 -0.99999988
		 1.000000476837 -2.2042271e-07 -4.0833049e-07 2.5641444e-07 -4.6566129e-08 -0.9999994
		 3.2883329e-07 -3.1272486e-07 0 -1.000000238419 1.000000953674 -1.000000476837 1.000001311302
		 -5.5114344e-07 -1.1920929e-07 0.99999905 -2.7675957e-09 -7.1525574e-07 1.000000834465
		 -9.5367432e-07 1.000000715256 0.99999881 4.7068015e-06 0.99999964 6.9267244e-06 -1.1920945e-07
		 1.000002384186 -2.2649767e-06 1.000000119209 0.9999975 0 -0.99999994 1.000000596046
		 -0.99999946 1.000002741814 2.8103727e-06 2.196851e-06 2.3385355e-06 0.99999976 -1.3397588e-06
		 4.4703484e-07 -7.8537727e-07 2.0861624e-07 -0.9999997 0.99999952 -1.000000238419;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  450 -425 -648.81812 412.00018 
		-425 -648.81812 450 -425 -625 412.00018 -425 -625 450 -584 -625 412.00018 -584 -625 
		450 -584 -648.81812 412.00018 -584 -648.81812;
	setAttr -s 8 ".vt[0:7]"  -450 425 548.81811523 -312.00018310547 425 548.81811523
		 -450 425 625 -312.00018310547 425 625 -450 684 625 -312.00018310547 684 625 -450 684 548.81811523
		 -312.00018310547 684 548.81811523;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 24 ".n[0:23]" -type "float3"  -4.338735e-30 -1 -4.8849813e-15
		 -4.338735e-30 -1 -4.8849813e-15 -4.338735e-30 -1 -4.8849813e-15 -4.338735e-30 -1
		 -4.8849813e-15 8.8817842e-16 -4.8849813e-15 1 8.8817842e-16 -4.8849813e-15 1 8.8817842e-16
		 -4.8849813e-15 1 8.8817842e-16 -4.8849813e-15 1 4.338735e-30 1 4.8849813e-15 4.338735e-30
		 1 4.8849813e-15 4.338735e-30 1 4.8849813e-15 4.338735e-30 1 4.8849813e-15 -8.8817842e-16
		 4.8849813e-15 -1 -8.8817842e-16 4.8849813e-15 -1 -8.8817842e-16 4.8849813e-15 -1
		 -8.8817842e-16 4.8849813e-15 -1 1 6.5081025e-30 -8.8817842e-16 1 6.5081025e-30 -8.8817842e-16
		 1 6.5081025e-30 -8.8817842e-16 1 6.5081025e-30 -8.8817842e-16 -1 -6.5081025e-30 8.8817842e-16
		 -1 -6.5081025e-30 8.8817842e-16 -1 -6.5081025e-30 8.8817842e-16 -1 -6.5081025e-30
		 8.8817842e-16;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 8 9 10 11
		f 4 1 7 -3 -7
		mu 0 4 16 17 18 19
		f 4 2 9 -4 -9
		mu 0 4 12 13 14 15
		f 4 3 11 -1 -11
		mu 0 4 20 21 22 23
		f 4 -12 -10 -8 -6
		mu 0 4 0 1 2 3
		f 4 10 4 6 8
		mu 0 4 4 5 6 7;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode mesh -n "polySurfaceShape2" -p "WindowSill_H100cm";
	rename -uid "78D4419F-4095-4C5B-0078-CB885AE47028";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" -0.83348227 -0.49819374
		 1.16651773 -0.49819374 1.16651773 1.50180626 -0.83348227 1.50180626 -0.16651756 -0.49819359
		 1.83348238 -0.49819359 1.83348238 1.50180626 -0.16651756 1.50180626 -0.49999997 -0.83348227
		 1.49999976 -0.83348227 1.49999976 1.16651773 -0.49999997 1.16651773 -0.16651756 -0.83348227
		 1.83348238 -0.83348227 1.83348238 1.16651773 -0.16651756 1.16651773 -0.49999997 -0.49819359
		 1.49999988 -0.49819359 1.49999988 1.50180626 -0.49999997 1.50180626 -0.83348227 -0.83348227
		 1.16651773 -0.83348227 1.16651773 1.16651762 -0.83348227 1.16651762;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -50 -50 50 50 -50 50 -50 50 50 50 50 50 -50 50 -50
		 50 50 -50 -50 -50 -50 50 -50 -50;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
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
createNode materialInfo -n "materialInfo18";
	rename -uid "A858838F-462B-3886-9195-EBA3587750EB";
createNode shadingEngine -n "lambert11SG";
	rename -uid "976D5036-40D7-E241-9232-48BDD0CD8A3A";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "Misc04_grid";
	rename -uid "B6321B6E-4062-26C5-DE45-869FC8180BD7";
createNode file -n "file10";
	rename -uid "F2DF0C04-431A-858D-6AAC-85908F065777";
	setAttr ".ftn" -type "string" "G:/My Drive/[03] CURRICULUM/[XX] ART ASSETS/[3] ENVIRONMENTS/LD_Tools/RaysGridTextures/Shaders/LD_MATS/Misc04_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture10";
	rename -uid "AA52AE62-4820-5F6A-DF85-C5A2E6057140";
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
connectAttr "lambert11SG.msg" "materialInfo18.sg";
connectAttr "Misc04_grid.msg" "materialInfo18.m";
connectAttr "file10.msg" "materialInfo18.t" -na;
connectAttr "Misc04_grid.oc" "lambert11SG.ss";
connectAttr "FalseCeiling_H325cmShape.iog" "lambert11SG.dsm" -na;
connectAttr "WindowSill_H100cmShape.iog" "lambert11SG.dsm" -na;
connectAttr "HallwayMinimum_W200cmShape.iog" "lambert11SG.dsm" -na;
connectAttr "BuildingFloor_H400cmShape.iog" "lambert11SG.dsm" -na;
connectAttr "file10.oc" "Misc04_grid.c";
connectAttr ":defaultColorMgtGlobals.cme" "file10.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file10.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file10.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file10.ws";
connectAttr "place2dTexture10.c" "file10.c";
connectAttr "place2dTexture10.tf" "file10.tf";
connectAttr "place2dTexture10.rf" "file10.rf";
connectAttr "place2dTexture10.mu" "file10.mu";
connectAttr "place2dTexture10.mv" "file10.mv";
connectAttr "place2dTexture10.s" "file10.s";
connectAttr "place2dTexture10.wu" "file10.wu";
connectAttr "place2dTexture10.wv" "file10.wv";
connectAttr "place2dTexture10.re" "file10.re";
connectAttr "place2dTexture10.of" "file10.of";
connectAttr "place2dTexture10.r" "file10.ro";
connectAttr "place2dTexture10.n" "file10.n";
connectAttr "place2dTexture10.vt1" "file10.vt1";
connectAttr "place2dTexture10.vt2" "file10.vt2";
connectAttr "place2dTexture10.vt3" "file10.vt3";
connectAttr "place2dTexture10.vc1" "file10.vc1";
connectAttr "place2dTexture10.o" "file10.uv";
connectAttr "place2dTexture10.ofs" "file10.fs";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert11SG.message" ":defaultLightSet.message";
connectAttr "lambert11SG.pa" ":renderPartition.st" -na;
connectAttr "Misc04_grid.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture10.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file10.msg" ":defaultTextureList1.tx" -na;
// End of WindowSill_H100cm.ma
