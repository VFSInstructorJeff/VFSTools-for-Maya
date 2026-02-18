//Maya ASCII 2026 scene
//Name: WindowOpening_Boolean_W300xH175cm.ma
//Last modified: Tue, Feb 17, 2026 05:02:20 PM
//Codeset: 1252
requires maya "2026";
requires "stereoCamera" "10.0";
requires "mtoa" "5.5.4.2";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2026";
fileInfo "version" "2026";
fileInfo "cutIdentifier" "202510291147-60ec9eda33";
fileInfo "osv" "Windows 11 Home v2009 (Build: 26200)";
fileInfo "UUID" "C4BBC4C1-4D8D-2118-E2CC-ED961C0316E1";
createNode transform -n "WindowOpening_Boolean_W300xH175cm";
	rename -uid "599AE336-466D-CBB7-C19F-DF90196B43AC";
	setAttr ".t" -type "double3" -225 -100 -625.00000000000011 ;
	setAttr ".rp" -type "double3" 225 100 625.00000000000011 ;
	setAttr ".sp" -type "double3" 225 100 625.00000000000011 ;
createNode mesh -n "WindowOpening_Boolean_W300xH175cmShape" -p "WindowOpening_Boolean_W300xH175cm";
	rename -uid "866D6332-43BB-F209-4A09-A9AF95BC6C9C";
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
	setAttr ".pv" -type "double2" -1.5 -1.000018835067749 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" -1.1190908 -2.99998665
		 -1.11909103 -1.24998677 -1.8809104 -1.24998724 -1.88091016 -2.99998713 -1.11909473
		 -0.74998713 -1.11909413 1.000011920929 -1.8809166 1.000011920929 -1.88091731 -0.74998713
		 -3.000020027161 -2.99998093 -1.4781952e-05 -2.99998426 -2.6702881e-05 -1.24998403
		 -3.00003194809 -1.24998093 -1.1035871e-05 -1.24997926 -3.000012159348 -1.24998045
		 -3.000015974045 -2.99998546 -1.4798085e-05 -2.99998426 -1.11908317 -1.9999882 -1.11908281
		 1.000011920929 -1.88091683 1.000016689301 -1.88091707 -1.99998343 -1.88090467 -4.5862507e-05
		 -1.88090301 -3.000054359436 -1.11910725 -3.00001168251 -1.11910892 -3.0552787e-06;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  350 0 0 350 0 0 350 0 0 350 
		0 0 350 0 0 350 0 0 350 0 0 350 0 0;
	setAttr -s 8 ".vt[0:7]"  -125 100 575 175 100 575 -125 100 651.18188477
		 175 100 651.18188477 -125 275 651.18188477 175 275 651.18188477 -125 275 575 175 275 575;
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
createNode mesh -n "polySurfaceShape2" -p "WindowOpening_Boolean_W300xH175cm";
	rename -uid "94B407DB-4A50-73BA-3CD6-C3AB881CE325";
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
createNode materialInfo -n "materialInfo10";
	rename -uid "F5A4A4E6-43EB-CBA7-AB8D-C48BBAD948F6";
createNode shadingEngine -n "lambert3SG";
	rename -uid "F5A036E9-4BB8-A192-50EE-2E9E1C06B739";
	setAttr ".ihi" 0;
	setAttr -s 45 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 14 ".gn";
createNode lambert -n "Wall01_grid_512";
	rename -uid "AE3A189D-4F96-2065-6BC4-0A9AADBFC678";
createNode file -n "file2";
	rename -uid "131E93D5-491E-FCE0-51A0-50A6640F57CD";
	setAttr ".ftn" -type "string" "X:/My Drive/[03] CURRICULUM/[XX] ART ASSETS/[3] ENVIRONMENTS/LD_Tools/RaysGridTextures/Shaders/LD_MATS/Wall01_grid_512.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture2";
	rename -uid "B4955959-4D60-C5AD-147E-F69CDCB2E43D";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "8E7BE03F-418C-0914-2F6F-1C9BACC5062E";
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
connectAttr "lambert3SG.msg" "materialInfo10.sg";
connectAttr "Wall01_grid_512.msg" "materialInfo10.m";
connectAttr "file2.msg" "materialInfo10.t" -na;
connectAttr "Wall01_grid_512.oc" "lambert3SG.ss";
connectAttr "|Wall03Shape.iog" "lambert3SG.dsm" -na;
connectAttr "WindowOpening_Boolean_W300xH175cmShape.iog" "lambert3SG.dsm" -na;
connectAttr "|WallShape1.ciog.cog[1]" "lambert3SG.dsm" -na;
connectAttr "|WallShape1.iog" "lambert3SG.dsm" -na;
connectAttr "Wall02Shape.iog" "lambert3SG.dsm" -na;
connectAttr "|Wall10Shape.iog" "lambert3SG.dsm" -na;
connectAttr "Wall11Shape.iog" "lambert3SG.dsm" -na;
connectAttr "|Wall03Shape.iog" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[0]" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[2]" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[3]" "lambert3SG.dsm" -na;
connectAttr "Wall07Shape.iog" "lambert3SG.dsm" -na;
connectAttr "Wall09Shape.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_Wall02Shape.iog" "lambert3SG.dsm" -na;
connectAttr "|WallShape1.ciog.cog[0]" "lambert3SG.dsm" -na;
connectAttr "WallShape2.ciog.cog[0]" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[0]" "lambert3SG.dsm" -na;
connectAttr "|WallShape4.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "WallShape9.ciog.cog[0]" "lambert3SG.dsm" -na;
connectAttr "WallShape9.iog.og[0]" "lambert3SG.dsm" -na;
connectAttr "WallShape9.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "|Wall10Shape.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape2.ciog.cog[1]" "lambert3SG.dsm" -na;
connectAttr "BF01_Wall03Shape.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_Wall06Shape.iog" "lambert3SG.dsm" -na;
connectAttr "|WallShape1.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape2.iog" "lambert3SG.dsm" -na;
connectAttr "WallShape2.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_Wall01Shape.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape2.iog.og[0]" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape2.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape2.ciog.cog[2]" "lambert3SG.dsm" -na;
connectAttr "BF02_Wall04Shape.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape5.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape6.ciog.cog[2]" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape6.iog" "lambert3SG.dsm" -na;
connectAttr "BF02_WallShape3.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape1.ciog.cog[0]" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape4.ciog.cog[0]" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape1.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape4.iog" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape5.iog.og[0]" "lambert3SG.dsm" -na;
connectAttr "BF01_WallShape5.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "DoorOpening_Boolean_W138xH259cmShape.iog" "lambert3SG.dsm" -na;
connectAttr "groupId157.msg" "lambert3SG.gn" -na;
connectAttr "groupId158.msg" "lambert3SG.gn" -na;
connectAttr "groupId159.msg" "lambert3SG.gn" -na;
connectAttr "groupId160.msg" "lambert3SG.gn" -na;
connectAttr "groupId161.msg" "lambert3SG.gn" -na;
connectAttr "groupId188.msg" "lambert3SG.gn" -na;
connectAttr "groupId189.msg" "lambert3SG.gn" -na;
connectAttr "groupId195.msg" "lambert3SG.gn" -na;
connectAttr "groupId196.msg" "lambert3SG.gn" -na;
connectAttr "groupId214.msg" "lambert3SG.gn" -na;
connectAttr "groupId215.msg" "lambert3SG.gn" -na;
connectAttr "groupId216.msg" "lambert3SG.gn" -na;
connectAttr "groupId865.msg" "lambert3SG.gn" -na;
connectAttr "groupId866.msg" "lambert3SG.gn" -na;
connectAttr "file2.oc" "Wall01_grid_512.c";
connectAttr ":defaultColorMgtGlobals.cme" "file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file2.ws";
connectAttr "place2dTexture2.c" "file2.c";
connectAttr "place2dTexture2.tf" "file2.tf";
connectAttr "place2dTexture2.rf" "file2.rf";
connectAttr "place2dTexture2.mu" "file2.mu";
connectAttr "place2dTexture2.mv" "file2.mv";
connectAttr "place2dTexture2.s" "file2.s";
connectAttr "place2dTexture2.wu" "file2.wu";
connectAttr "place2dTexture2.wv" "file2.wv";
connectAttr "place2dTexture2.re" "file2.re";
connectAttr "place2dTexture2.of" "file2.of";
connectAttr "place2dTexture2.r" "file2.ro";
connectAttr "place2dTexture2.n" "file2.n";
connectAttr "place2dTexture2.vt1" "file2.vt1";
connectAttr "place2dTexture2.vt2" "file2.vt2";
connectAttr "place2dTexture2.vt3" "file2.vt3";
connectAttr "place2dTexture2.vc1" "file2.vc1";
connectAttr "place2dTexture2.o" "file2.uv";
connectAttr "place2dTexture2.ofs" "file2.fs";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "Wall01_grid_512.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file2.msg" ":defaultTextureList1.tx" -na;
// End of WindowOpening_Boolean_W300xH175cm.ma
