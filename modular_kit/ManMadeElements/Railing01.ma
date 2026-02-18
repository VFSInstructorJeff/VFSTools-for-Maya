//Maya ASCII 2026 scene
//Name: Railing01.ma
//Last modified: Tue, Feb 17, 2026 04:45:22 PM
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
fileInfo "UUID" "60EC350A-469E-9205-28A3-D1B539F7C438";
createNode transform -n "Railing01_grp";
	rename -uid "F4103DC9-43C1-6C28-A541-4BBF98E261FF";
	setAttr ".t" -type "double3" 525 -425 800 ;
	setAttr ".rp" -type "double3" -525 425 -800 ;
	setAttr ".sp" -type "double3" -525 425 -800 ;
createNode transform -n "Railing01" -p "Railing01_grp";
	rename -uid "0C7EC08B-42E8-F934-BCB7-F8BBAB05820D";
	setAttr ".rp" -type "double3" -525 425 -590 ;
	setAttr ".sp" -type "double3" -525 425 -590 ;
createNode mesh -n "Railing01Shape" -p "Railing01";
	rename -uid "8D7E338B-4315-052F-9ECE-1498B1CA373A";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:77]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 6 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "back";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 13 "f[3]" "f[8]" "f[15]" "f[20]" "f[26]" "f[32]" "f[38]" "f[44]" "f[50]" "f[56]" "f[62]" "f[68]" "f[74]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottom";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 13 "f[1]" "f[9]" "f[13]" "f[21]" "f[27]" "f[33]" "f[39]" "f[45]" "f[51]" "f[57]" "f[63]" "f[69]" "f[75]";
	setAttr ".gtag[2].gtagnm" -type "string" "front";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 11 "f[5:6]" "f[17:18]" "f[24]" "f[30]" "f[36]" "f[42]" "f[48]" "f[54]" "f[60]" "f[66]" "f[72]";
	setAttr ".gtag[3].gtagnm" -type "string" "left";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 13 "f[2]" "f[11]" "f[14]" "f[23]" "f[29]" "f[35]" "f[41]" "f[47]" "f[53]" "f[59]" "f[65]" "f[71]" "f[77]";
	setAttr ".gtag[4].gtagnm" -type "string" "right";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 13 "f[4]" "f[10]" "f[16]" "f[22]" "f[28]" "f[34]" "f[40]" "f[46]" "f[52]" "f[58]" "f[64]" "f[70]" "f[76]";
	setAttr ".gtag[5].gtagnm" -type "string" "top";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 13 "f[0]" "f[7]" "f[12]" "f[19]" "f[25]" "f[31]" "f[37]" "f[43]" "f[49]" "f[55]" "f[61]" "f[67]" "f[73]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 246 ".uvst[0].uvsp[0:245]" -type "float2" 0.13499992 2.000000238419
		 1.7316867e-07 2.000000715256 0.27500004 1.99999988 0.17499985 2 0.31500015 2.000000238419
		 0.25266242 -0.43468687 0.29266194 -0.43468529 0.29266194 -0.33468542 0.25266242 -0.33468702
		 0.33689612 -0.43468463 0.37689748 -0.4346855 0.37689748 -0.33468574 0.33689612 -0.33468488
		 2.3318151e-07 -0.099999592 0.13499993 -0.099999756 0.17499991 -0.09999989 0.27500004
		 -0.10000011 0.31499976 -0.099999852 0 0 0.040000014 3.7252903e-09 0.040000014 0.8599999
		 0 0.8599999 0.27604604 0.18321413 0.27604604 0.14321414 0.31604606 0.14321414 0.31604606
		 0.18321413 0.12000002 0.85999984 0.080000028 0.8599999 0.080000028 1.1175871e-08
		 0.12000003 5.9604645e-08 0.32093817 0.18321413 0.32093817 0.14321414 0.36093816 0.14321414
		 0.36093816 0.18321413 0.16000004 1.0430813e-07 0.16000001 0.85999978 0.1 1.89999986
		 7.4505806e-08 1.90000272 0.27500001 1.89999986 0.17499997 1.89999986 0.35000017 1.90000105
		 0.25266248 -0.43468571 0.32766247 -0.43468571 0.32766247 -0.33468571 0.25266248 -0.33468571
		 0.33689734 -0.43468466 0.41189727 -0.43468466 0.41189727 -0.33468476 0.33689734 -0.33468476
		 0 0 0.099999994 0 0.17499998 0 0.27499998 0 0.35000002 0 0.20000003 1.7881393e-07
		 0.29999998 1.7881393e-07 0.30000013 1.0600003 0.20000033 1.060000062 0.52712286 0.23702475
		 0.52712286 0.13702455 0.62712288 0.13702455 0.62712294 0.23702475 0.10000029 1.060000062
		 3.8743019e-07 1.060000181 0 0 0.099999964 1.1920929e-07 0.52351892 0.13044423 0.52351886
		 0.030444264 0.62351888 0.030444384 0.62351888 0.13044435 0.29999998 1.7881393e-07
		 0.39999995 1.7881393e-07 0.4000001 1.059999943 0.30000013 1.0600003 0.099999964 1.1920929e-07
		 0.20000003 1.7881393e-07 0.20000033 1.060000062 0.10000029 1.060000062 0.16000004
		 -1.2894472e-08 0.24000008 4.6710174e-08 0.24000002 0.85999972 0.16000007 0.85999978
		 0.53526402 0.19392896 0.53526402 0.11392892 0.615264 0.11392892 0.615264 0.19392896
		 0.080000073 0.85999978 2.9802322e-08 0.85999978 0 0 0.080000028 5.3157411e-08 0.70120198
		 0.19392893 0.62120199 0.19392893 0.62120199 0.11392887 0.70120198 0.11392887 0.32000008
		 4.6710174e-08 0.32000002 0.85999972 0 0 0.040000014 3.7252903e-09 0.040000014 0.8599999
		 0 0.8599999 0.27604604 0.18321413 0.27604604 0.14321414 0.31604606 0.14321414 0.31604606
		 0.18321413 0.12000002 0.85999984 0.080000028 0.8599999 0.080000028 1.1175871e-08
		 0.12000003 5.9604645e-08 0.32093817 0.18321413 0.32093817 0.14321414 0.36093816 0.14321414
		 0.36093816 0.18321413 0.16000004 1.0430813e-07 0.16000001 0.85999978 0 0 0.040000014
		 3.7252903e-09 0.040000014 0.8599999 0 0.8599999 0.27604604 0.18321413 0.27604604
		 0.14321414 0.31604606 0.14321414 0.31604606 0.18321413 0.12000002 0.85999984 0.080000028
		 0.8599999 0.080000028 1.1175871e-08 0.12000003 5.9604645e-08 0.32093817 0.18321413
		 0.32093817 0.14321414 0.36093816 0.14321414 0.36093816 0.18321413 0.16000004 1.0430813e-07
		 0.16000001 0.85999978 0 0 0.040000014 3.7252903e-09 0.040000014 0.8599999 0 0.8599999
		 0.27604604 0.18321413 0.27604604 0.14321414 0.31604606 0.14321414 0.31604606 0.18321413
		 0.12000002 0.85999984 0.080000028 0.8599999 0.080000028 1.1175871e-08 0.12000003
		 5.9604645e-08 0.32093817 0.18321413 0.32093817 0.14321414 0.36093816 0.14321414 0.36093816
		 0.18321413 0.16000004 1.0430813e-07 0.16000001 0.85999978 0 0 0.040000014 3.7252903e-09
		 0.040000014 0.8599999 0 0.8599999 0.27604604 0.18321413 0.27604604 0.14321414 0.31604606
		 0.14321414 0.31604606 0.18321413 0.12000002 0.85999984 0.080000028 0.8599999 0.080000028
		 1.1175871e-08 0.12000003 5.9604645e-08 0.32093817 0.18321413 0.32093817 0.14321414
		 0.36093816 0.14321414 0.36093816 0.18321413 0.16000004 1.0430813e-07 0.16000001 0.85999978
		 0 0 0.040000014 3.7252903e-09 0.040000014 0.8599999 0 0.8599999 0.27604604 0.18321413
		 0.27604604 0.14321414 0.31604606 0.14321414 0.31604606 0.18321413 0.12000002 0.85999984
		 0.080000028 0.8599999 0.080000028 1.1175871e-08 0.12000003 5.9604645e-08 0.32093817
		 0.18321413 0.32093817 0.14321414 0.36093816 0.14321414 0.36093816 0.18321413 0.16000004
		 1.0430813e-07 0.16000001 0.85999978 0 0 0.040000014 3.7252903e-09 0.040000014 0.8599999
		 0 0.8599999 0.27604604 0.18321413 0.27604604 0.14321414 0.31604606 0.14321414 0.31604606
		 0.18321413 0.12000002 0.85999984 0.080000028 0.8599999 0.080000028 1.1175871e-08
		 0.12000003 5.9604645e-08 0.32093817 0.18321413 0.32093817 0.14321414 0.36093816 0.14321414
		 0.36093816 0.18321413 0.16000004 1.0430813e-07 0.16000001 0.85999978 0 0 0.040000014
		 3.7252903e-09 0.040000014 0.8599999 0 0.8599999 0.27604604 0.18321413 0.27604604
		 0.14321414 0.31604606 0.14321414 0.31604606 0.18321413 0.12000002 0.85999984 0.080000028
		 0.8599999 0.080000028 1.1175871e-08 0.12000003 5.9604645e-08 0.32093817 0.18321413
		 0.32093817 0.14321414 0.36093816 0.14321414 0.36093816 0.18321413 0.16000004 1.0430813e-07
		 0.16000001 0.85999978 0.20000003 1.7881393e-07 0.29999998 1.7881393e-07 0.30000013
		 1.0600003 0.20000033 1.060000062 0.52712286 0.23702475 0.52712286 0.13702455 0.62712288
		 0.13702455 0.62712294 0.23702475 0.10000029 1.060000062 3.8743019e-07 1.060000181
		 0 0 0.099999964 1.1920929e-07 0.52351892 0.13044423 0.52351886 0.030444264 0.62351888
		 0.030444384 0.62351888 0.13044435 0.29999998 1.7881393e-07 0.39999995 1.7881393e-07
		 0.4000001 1.059999943 0.30000013 1.0600003 0.099999964 1.1920929e-07 0.20000003 1.7881393e-07
		 0.20000033 1.060000062 0.10000029 1.060000062;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 104 ".pt[0:103]" -type "float3"  -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0 -325 
		3.2699452e-06 0 -325 3.2699452e-06 0 -325 3.2699452e-06 0;
	setAttr -s 104 ".vt[0:103]"  -200 429 -590 -200 425 -590 -200 429 -800
		 -200 425 -800 -210 429 -800 -210 425 -800 -210 429 -590 -210 425 -590 -202 429 -616.19995117
		 -202 429 -620.19995117 -202 515 -616.19995117 -202 515 -620.19995117 -206 515 -616.19995117
		 -206 515 -620.19995117 -206 429 -616.19995117 -206 429 -620.19995117 -200 522.5 -600
		 -200 515 -600 -200 522.5 -790 -200 515 -790 -210 522.5 -790 -210 515 -790 -210 522.5 -600
		 -210 515 -600 -200 429 -590 -200 429 -600 -200 535.000061035156 -590 -200 535.000061035156 -600
		 -210 535.000061035156 -590 -210 535.000061035156 -600 -210 429 -590 -210 429 -600
		 -201 429 -691 -201 429 -699 -201 515 -691 -201 515 -699 -209 515 -691 -209 515 -699
		 -209 429 -691 -209 429 -699 -202 429 -634.40002441 -202 429 -638.40002441 -202 515 -634.40002441
		 -202 515 -638.40002441 -206 515 -634.40002441 -206 515 -638.40002441 -206 429 -634.40002441
		 -206 429 -638.40002441 -202 429 -652.59997559 -202 429 -656.59997559 -202 515 -652.59997559
		 -202 515 -656.59997559 -206 515 -652.59997559 -206 515 -656.59997559 -206 429 -652.59997559
		 -206 429 -656.59997559 -202 429 -670.79998779 -202 429 -674.79998779 -202 515 -670.79998779
		 -202 515 -674.79998779 -206 515 -670.79998779 -206 515 -674.79998779 -206 429 -670.79998779
		 -206 429 -674.79998779 -202 429 -715.20001221 -202 429 -719.20001221 -202 515 -715.20001221
		 -202 515 -719.20001221 -206 515 -715.20001221 -206 515 -719.20001221 -206 429 -715.20001221
		 -206 429 -719.20001221 -202 429 -733.40002441 -202 429 -737.40002441 -202 515 -733.40002441
		 -202 515 -737.40002441 -206 515 -733.40002441 -206 515 -737.40002441 -206 429 -733.40002441
		 -206 429 -737.40002441 -202 429 -751.59997559 -202 429 -755.59997559 -202 515 -751.59997559
		 -202 515 -755.59997559 -206 515 -751.59997559 -206 515 -755.59997559 -206 429 -751.59997559
		 -206 429 -755.59997559 -202 429 -769.79998779 -202 429 -773.79998779 -202 515 -769.79998779
		 -202 515 -773.79998779 -206 515 -769.79998779 -206 515 -773.79998779 -206 429 -769.79998779
		 -206 429 -773.79998779 -200 429 -790 -200 429 -800 -200 535.000061035156 -790 -200 535.000061035156 -800
		 -210 535.000061035156 -790 -210 535.000061035156 -800 -210 429 -790 -210 429 -800;
	setAttr -s 156 ".ed[0:155]"  0 2 0 2 4 0 3 5 0 4 6 0 6 0 0 7 1 0 0 1 0
		 2 3 0 4 5 0 6 7 0 1 3 0 5 7 0 8 9 0 10 11 0 12 13 0 14 15 0 8 10 0 9 11 0 10 12 0
		 11 13 0 12 14 0 13 15 0 14 8 0 15 9 0 16 18 0 18 20 0 19 21 0 20 22 0 22 16 0 23 17 0
		 16 17 0 18 19 0 20 21 0 22 23 0 17 19 0 21 23 0 24 25 0 26 27 0 28 29 0 30 31 0 24 26 0
		 25 27 0 26 28 0 27 29 0 28 30 0 29 31 0 30 24 0 31 25 0 32 33 0 34 35 0 36 37 0 38 39 0
		 32 34 0 33 35 0 34 36 0 35 37 0 36 38 0 37 39 0 38 32 0 39 33 0 40 41 0 42 43 0 44 45 0
		 46 47 0 40 42 0 41 43 0 42 44 0 43 45 0 44 46 0 45 47 0 46 40 0 47 41 0 48 49 0 50 51 0
		 52 53 0 54 55 0 48 50 0 49 51 0 50 52 0 51 53 0 52 54 0 53 55 0 54 48 0 55 49 0 56 57 0
		 58 59 0 60 61 0 62 63 0 56 58 0 57 59 0 58 60 0 59 61 0 60 62 0 61 63 0 62 56 0 63 57 0
		 64 65 0 66 67 0 68 69 0 70 71 0 64 66 0 65 67 0 66 68 0 67 69 0 68 70 0 69 71 0 70 64 0
		 71 65 0 72 73 0 74 75 0 76 77 0 78 79 0 72 74 0 73 75 0 74 76 0 75 77 0 76 78 0 77 79 0
		 78 72 0 79 73 0 80 81 0 82 83 0 84 85 0 86 87 0 80 82 0 81 83 0 82 84 0 83 85 0 84 86 0
		 85 87 0 86 80 0 87 81 0 88 89 0 90 91 0 92 93 0 94 95 0 88 90 0 89 91 0 90 92 0 91 93 0
		 92 94 0 93 95 0 94 88 0 95 89 0 96 97 0 98 99 0 100 101 0 102 103 0 96 98 0 97 99 0
		 98 100 0 99 101 0 100 102 0 101 103 0 102 96 0 103 97 0;
	setAttr -s 78 -ch 312 ".fc[0:77]" -type "polyFaces" 
		f 4 -9 -2 7 2
		mu 0 4 5 6 7 8
		f 4 -7 -5 9 5
		mu 0 4 9 10 11 12
		f 4 1 3 4 0
		mu 0 4 13 14 0 1
		f 4 -4 8 11 -10
		mu 0 4 0 14 15 3
		f 4 -3 -11 -6 -12
		mu 0 4 15 16 2 3
		f 4 -8 -1 6 10
		mu 0 4 16 17 4 2
		f 4 12 17 -14 -17
		mu 0 4 18 19 20 21
		f 4 13 19 -15 -19
		mu 0 4 22 23 24 25
		f 4 14 21 -16 -21
		mu 0 4 26 27 28 29
		f 4 15 23 -13 -23
		mu 0 4 30 31 32 33
		f 4 -24 -22 -20 -18
		mu 0 4 19 28 27 20
		f 4 22 16 18 20
		mu 0 4 29 34 35 26
		f 4 -33 -26 31 26
		mu 0 4 41 42 43 44
		f 4 -31 -29 33 29
		mu 0 4 45 46 47 48
		f 4 25 27 28 24
		mu 0 4 49 50 36 37
		f 4 -28 32 35 -34
		mu 0 4 36 50 51 39
		f 4 -27 -35 -30 -36
		mu 0 4 51 52 38 39
		f 4 -32 -25 30 34
		mu 0 4 52 53 40 38
		f 4 36 41 -38 -41
		mu 0 4 54 55 56 57
		f 4 37 43 -39 -43
		mu 0 4 58 59 60 61
		f 4 38 45 -40 -45
		mu 0 4 62 63 64 65
		f 4 39 47 -37 -47
		mu 0 4 66 67 68 69
		f 4 -48 -46 -44 -42
		mu 0 4 70 71 72 73
		f 4 46 40 42 44
		mu 0 4 74 75 76 77
		f 4 48 53 -50 -53
		mu 0 4 78 79 80 81
		f 4 49 55 -51 -55
		mu 0 4 82 83 84 85
		f 4 50 57 -52 -57
		mu 0 4 86 87 88 89
		f 4 51 59 -49 -59
		mu 0 4 90 91 92 93
		f 4 -60 -58 -56 -54
		mu 0 4 79 94 95 80
		f 4 58 52 54 56
		mu 0 4 89 78 81 86
		f 4 60 65 -62 -65
		mu 0 4 96 97 98 99
		f 4 61 67 -63 -67
		mu 0 4 100 101 102 103
		f 4 62 69 -64 -69
		mu 0 4 104 105 106 107
		f 4 63 71 -61 -71
		mu 0 4 108 109 110 111
		f 4 -72 -70 -68 -66
		mu 0 4 97 106 105 98
		f 4 70 64 66 68
		mu 0 4 107 112 113 104
		f 4 72 77 -74 -77
		mu 0 4 114 115 116 117
		f 4 73 79 -75 -79
		mu 0 4 118 119 120 121
		f 4 74 81 -76 -81
		mu 0 4 122 123 124 125
		f 4 75 83 -73 -83
		mu 0 4 126 127 128 129
		f 4 -84 -82 -80 -78
		mu 0 4 115 124 123 116
		f 4 82 76 78 80
		mu 0 4 125 130 131 122
		f 4 84 89 -86 -89
		mu 0 4 132 133 134 135
		f 4 85 91 -87 -91
		mu 0 4 136 137 138 139
		f 4 86 93 -88 -93
		mu 0 4 140 141 142 143
		f 4 87 95 -85 -95
		mu 0 4 144 145 146 147
		f 4 -96 -94 -92 -90
		mu 0 4 133 142 141 134
		f 4 94 88 90 92
		mu 0 4 143 148 149 140
		f 4 96 101 -98 -101
		mu 0 4 150 151 152 153
		f 4 97 103 -99 -103
		mu 0 4 154 155 156 157
		f 4 98 105 -100 -105
		mu 0 4 158 159 160 161
		f 4 99 107 -97 -107
		mu 0 4 162 163 164 165
		f 4 -108 -106 -104 -102
		mu 0 4 151 160 159 152
		f 4 106 100 102 104
		mu 0 4 161 166 167 158
		f 4 108 113 -110 -113
		mu 0 4 168 169 170 171
		f 4 109 115 -111 -115
		mu 0 4 172 173 174 175
		f 4 110 117 -112 -117
		mu 0 4 176 177 178 179
		f 4 111 119 -109 -119
		mu 0 4 180 181 182 183
		f 4 -120 -118 -116 -114
		mu 0 4 169 178 177 170
		f 4 118 112 114 116
		mu 0 4 179 184 185 176
		f 4 120 125 -122 -125
		mu 0 4 186 187 188 189
		f 4 121 127 -123 -127
		mu 0 4 190 191 192 193
		f 4 122 129 -124 -129
		mu 0 4 194 195 196 197
		f 4 123 131 -121 -131
		mu 0 4 198 199 200 201
		f 4 -132 -130 -128 -126
		mu 0 4 187 196 195 188
		f 4 130 124 126 128
		mu 0 4 197 202 203 194
		f 4 132 137 -134 -137
		mu 0 4 204 205 206 207
		f 4 133 139 -135 -139
		mu 0 4 208 209 210 211
		f 4 134 141 -136 -141
		mu 0 4 212 213 214 215
		f 4 135 143 -133 -143
		mu 0 4 216 217 218 219
		f 4 -144 -142 -140 -138
		mu 0 4 205 214 213 206
		f 4 142 136 138 140
		mu 0 4 215 220 221 212
		f 4 144 149 -146 -149
		mu 0 4 222 223 224 225
		f 4 145 151 -147 -151
		mu 0 4 226 227 228 229
		f 4 146 153 -148 -153
		mu 0 4 230 231 232 233
		f 4 147 155 -145 -155
		mu 0 4 234 235 236 237
		f 4 -156 -154 -152 -150
		mu 0 4 238 239 240 241
		f 4 154 148 150 152
		mu 0 4 242 243 244 245;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "UCX_Railing01" -p "Railing01_grp";
	rename -uid "7AD60E95-4662-28E5-A5D1-B4B99CC48885";
	setAttr ".t" -type "double3" -325 0 0 ;
	setAttr ".rp" -type "double3" -210 425.00003051757812 -590 ;
	setAttr ".sp" -type "double3" -210 425.00003051757812 -590 ;
createNode mesh -n "UCX_RailingShape1" -p "UCX_Railing01";
	rename -uid "0B3201D9-4FE1-2E9D-A289-E6BB35761889";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 1.121063908003137 0.49999940395355225 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 6 ".pt[2:7]" -type "float3"  0 70.740509 0 0 70.740509 
		0 0 70.740509 -183.24048 0 70.740509 -183.24048 0 0 -183.24048 0 0 -183.24048;
createNode mesh -n "polySurfaceShape78" -p "UCX_Railing01";
	rename -uid "19539D60-4142-4075-F18A-E2BA35E859B8";
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
	setAttr ".pv" -type "double2" 0.49999374151229858 0.37499374896287918 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.46843272
		 6.2496874e-06 0.375 0.25 0.44233352 0.27609333 0.375 0.5 0.4684265 0.5 0.375 0.75
		 0.4684265 0.75 0.375 1 0.46842808 0.99998748 0.87498748 1.249875e-05 0.87498748 0.2499875
		 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -209.5 425.50003 -590.5 -200.5 
		425.50003 -590.5 -209.5 451.25949 -590.5 -200.5 451.25949 -590.5 -209.5 451.25949 
		-616.25952 -200.5 451.25949 -616.25952 -209.5 425.50003 -616.25952 -200.5 425.50003 
		-616.25952;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode groupId -n "groupId230";
	rename -uid "428464ED-4022-3ED2-5433-248434480FB7";
	setAttr ".ihi" 0;
createNode shadingEngine -n "lambert14SG";
	rename -uid "0BFD0DCD-4797-CAFD-AD09-549CC99C1E44";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 12 ".gn";
createNode materialInfo -n "materialInfo21";
	rename -uid "51645286-4898-68F8-1BF9-868CAEE2168C";
createNode lambert -n "Misc07_grid_512";
	rename -uid "BDAFDDAA-4C94-BAD1-BA30-56998A65A2FF";
createNode file -n "file13";
	rename -uid "72B2BCC0-4F5F-5DD7-54ED-3EA812B1E729";
	setAttr ".ftn" -type "string" "X:/My Drive/[03] CURRICULUM/[XX] ART ASSETS/[3] ENVIRONMENTS/LD_Tools/RaysGridTextures/Shaders/LD_MATS/Misc07_grid_512.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture13";
	rename -uid "30FDF79A-478D-5A1A-8706-F092EA92E26F";
createNode displayLayer -n "UCX_GROUP";
	rename -uid "74C6A8D0-42C7-016E-CE93-DA868FD6DCCD";
	setAttr ".v" no;
	setAttr ".ufem" -type "stringArray" 0  ;
	setAttr ".do" 2;
createNode displayLayerManager -n "layerManager";
	rename -uid "CB5B3832-4DAC-9435-2579-4F9E04ADD755";
	setAttr ".cdl" 2;
	setAttr -s 5 ".dli[1:4]"  1 2 3 4;
	setAttr -s 5 ".dli";
createNode polyNormalPerVertex -n "polyNormalPerVertex27";
	rename -uid "F9C6F185-4E6B-A78F-44C3-5AB17D148CB3";
	setAttr ".uopa" yes;
	setAttr -s 8 ".vn";
	setAttr ".vn[0].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[1].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[2].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[3].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[4].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[5].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[6].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
	setAttr ".vn[7].nxyz" -type "float3" 1e+20 1e+20 1e+20 ;
createNode polyTweakUV -n "polyTweakUV59";
	rename -uid "A558557A-4A41-6727-69DC-B7A95FB47BB9";
	setAttr ".uopa" yes;
	setAttr -s 24 ".uvtk[0:23]" -type "float2" -0.37991187 -0.0012878776
		 -0.37991208 -3.41501737 0.93718034 -3.41501784 0.93718058 -0.0012883565 0.062856749
		 2.91372991 0.062856823 -0.5 1.37994981 -0.5 1.37994969 2.91372991 2.5134138e-08 0.50128287
		 -0.00048148786 0.50128287 -0.00048183053 3.9150157 -3.1662071e-07 3.9150157 0.00051535858
		 -2.91373444 3.4113247e-05 -2.91373444 3.4362078e-05 0.5 0.00051541626 0.5 0.13325638
		 0.0012873411 0.13277531 0.0012873411 0.13277461 1.31837487 0.13325596 1.31837487
		 0.51267552 -1.31708634 0.51219398 -1.31708634 0.51219511 4.5857223e-06 0.51267648
		 4.5857246e-06;
createNode polyLayoutUV -n "polyLayoutUV116";
	rename -uid "D73659B9-401B-7955-7C70-CD83E93A222E";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:5]";
	setAttr ".fr" no;
	setAttr ".l" 0;
	setAttr ".ps" 0.20000000298023224;
	setAttr ".sc" 0;
	setAttr ".dl" yes;
	setAttr ".rbf" 3;
	setAttr ".lm" 1;
createNode polyLayoutUV -n "polyLayoutUV115";
	rename -uid "9B68B3AD-49E9-52B0-14C7-7F9CE5219CDF";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[*]";
	setAttr ".fr" no;
	setAttr ".l" 0;
	setAttr ".ps" 0.20000000298023224;
	setAttr ".sc" 0;
	setAttr ".dl" yes;
	setAttr ".rbf" 3;
	setAttr ".lm" 1;
createNode polyAutoProj -n "polyAutoProj111";
	rename -uid "01F5D5B2-4D14-47DD-68AD-F19ECC717943";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:5]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dl" yes;
createNode polyAutoProj -n "polyAutoProj110";
	rename -uid "5A19732E-4DE9-BE1D-7006-58A018457749";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:5]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dl" yes;
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
connectAttr "groupId230.id" "Railing01Shape.iog.og[0].gid";
connectAttr "lambert14SG.mwc" "Railing01Shape.iog.og[0].gco";
connectAttr "UCX_GROUP.di" "UCX_Railing01.do";
connectAttr "polyNormalPerVertex27.out" "UCX_RailingShape1.i";
connectAttr "polyTweakUV59.uvtk[0]" "UCX_RailingShape1.uvst[0].uvtw";
connectAttr "Misc07_grid_512.oc" "lambert14SG.ss";
connectAttr "Railing01Shape.iog.og[0]" "lambert14SG.dsm" -na;
connectAttr "InteriorDoorFrame01Shape.iog" "lambert14SG.dsm" -na;
connectAttr "Stairs01Railing01Shape.ciog.cog[0]" "lambert14SG.dsm" -na;
connectAttr "Stairs01Railing01Shape.iog.og[0]" "lambert14SG.dsm" -na;
connectAttr "groupId230.msg" "lambert14SG.gn" -na;
connectAttr "groupId898.msg" "lambert14SG.gn" -na;
connectAttr "groupId902.msg" "lambert14SG.gn" -na;
connectAttr "groupId903.msg" "lambert14SG.gn" -na;
connectAttr "groupId904.msg" "lambert14SG.gn" -na;
connectAttr "groupId905.msg" "lambert14SG.gn" -na;
connectAttr "groupId906.msg" "lambert14SG.gn" -na;
connectAttr "groupId907.msg" "lambert14SG.gn" -na;
connectAttr "groupId908.msg" "lambert14SG.gn" -na;
connectAttr "groupId1008.msg" "lambert14SG.gn" -na;
connectAttr "groupId1010.msg" "lambert14SG.gn" -na;
connectAttr "groupId1014.msg" "lambert14SG.gn" -na;
connectAttr "lambert14SG.msg" "materialInfo21.sg";
connectAttr "Misc07_grid_512.msg" "materialInfo21.m";
connectAttr "file13.msg" "materialInfo21.t" -na;
connectAttr "file13.oc" "Misc07_grid_512.c";
connectAttr ":defaultColorMgtGlobals.cme" "file13.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file13.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file13.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file13.ws";
connectAttr "place2dTexture13.c" "file13.c";
connectAttr "place2dTexture13.tf" "file13.tf";
connectAttr "place2dTexture13.rf" "file13.rf";
connectAttr "place2dTexture13.mu" "file13.mu";
connectAttr "place2dTexture13.mv" "file13.mv";
connectAttr "place2dTexture13.s" "file13.s";
connectAttr "place2dTexture13.wu" "file13.wu";
connectAttr "place2dTexture13.wv" "file13.wv";
connectAttr "place2dTexture13.re" "file13.re";
connectAttr "place2dTexture13.of" "file13.of";
connectAttr "place2dTexture13.r" "file13.ro";
connectAttr "place2dTexture13.n" "file13.n";
connectAttr "place2dTexture13.vt1" "file13.vt1";
connectAttr "place2dTexture13.vt2" "file13.vt2";
connectAttr "place2dTexture13.vt3" "file13.vt3";
connectAttr "place2dTexture13.vc1" "file13.vc1";
connectAttr "place2dTexture13.o" "file13.uv";
connectAttr "place2dTexture13.ofs" "file13.fs";
connectAttr "layerManager.dli[2]" "UCX_GROUP.id";
connectAttr "polyTweakUV59.out" "polyNormalPerVertex27.ip";
connectAttr "polyLayoutUV116.out" "polyTweakUV59.ip";
connectAttr "polyLayoutUV115.out" "polyLayoutUV116.ip";
connectAttr "polyAutoProj111.out" "polyLayoutUV115.ip";
connectAttr "polyAutoProj110.out" "polyAutoProj111.ip";
connectAttr "UCX_RailingShape1.wm" "polyAutoProj111.mp";
connectAttr "|Railing01_grp|UCX_Railing01|polySurfaceShape78.o" "polyAutoProj110.ip"
		;
connectAttr "UCX_RailingShape1.wm" "polyAutoProj110.mp";
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
relationship "link" ":lightLinker1" "lambert14SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert17SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert14SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert17SG.message" ":defaultLightSet.message";
connectAttr "lambert14SG.pa" ":renderPartition.st" -na;
connectAttr "lambert17SG.pa" ":renderPartition.st" -na;
connectAttr "Misc07_grid_512.msg" ":defaultShaderList1.s" -na;
connectAttr "M_UCX.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture13.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file13.msg" ":defaultTextureList1.tx" -na;
// End of Railing01.ma
