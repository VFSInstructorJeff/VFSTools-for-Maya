//Maya ASCII 2026 scene
//Name: Cube_50cm.ma
//Last modified: Thu, Feb 19, 2026 12:56:35 PM
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
fileInfo "UUID" "A0AF4548-42EB-A331-E1EF-9294C3314AC7";
fileInfo "license" "education";
createNode transform -n "Cube_50cm";
	rename -uid "AC732113-4DA4-FECD-6DF4-EFBD6CD6C09D";
createNode mesh -n "Cube_50cmShape" -p "Cube_50cm";
	rename -uid "52E3B8FE-438D-7381-9620-52BC7FE9C646";
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
	setAttr ".pv" -type "double2" 0.25 0.25000017881393433 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 24 ".uvst[0].uvsp[0:23]" -type "float2" 8.9406967e-08 0.5
		 0 7.4505806e-08 0.49999994 0 0.5 0.49999994 0 0.50000024 0 0 0.5 0 0.5 0.50000024
		 0.5 1.7881393e-07 0.5 0.50000018 0 0.50000018 0 1.7881393e-07 0.50000006 1.7881393e-07
		 0.49999982 0.50000012 -5.9604645e-08 0.50000018 -5.9604645e-08 1.937151e-07 2.9802322e-08
		 0.50000024 0 1.1920929e-07 0.5 3.4272671e-07 0.5 0.50000024 0.5 2.3841858e-07 0.5
		 0.50000012 0 0.49999988 0 2.3841858e-07;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  158.38879 25 -25 158.38879 
		25 -25 158.38879 25 -25 158.38879 25 -25 158.38879 25 -25 158.38879 25 -25 158.38879 
		25 -25 158.38879 25 -25;
	setAttr -s 8 ".vt[0:7]"  -158.38879395 -25 25 -108.38879395 -25 25
		 -158.38879395 25 25 -108.38879395 25 25 -158.38879395 25 -25 -108.38879395 25 -25
		 -158.38879395 -25 -25 -108.38879395 -25 -25;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 24 ".n[0:23]" -type "float3"  0 0 1 0 0 1 0 0 1 0 0 1 0 1
		 0 0 1 0 0 1 0 0 1 0 0 0 -1 0 0 -1 0 0 -1 0 0 -1 0 -1 0 0 -1 0 0 -1 0 0 -1 0 1 0 0
		 1 0 0 1 0 0 1 0 0 -1 0 0 -1 0 0 -1 0 0 -1 0 0;
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
	setAttr ".ftn" -type "string" "G:/My Drive/[03] CURRICULUM/[XX] ART ASSETS/[3] ENVIRONMENTS/LD_Tools/RaysGridTextures/Shaders/LD_MATS/Floor_grid.tga";
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
// End of Cube_50cm.ma
