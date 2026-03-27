//Maya ASCII 2026 scene
//Name: Railing01.ma
//Last modified: Thu, Feb 19, 2026 12:51:44 PM
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
fileInfo "UUID" "3E8B655E-4693-F9E5-BDAB-15BB445AFBD3";
fileInfo "license" "education";
createNode transform -n "Railing01_grp";
	rename -uid "A5C58F00-4BFD-440B-467A-08B5B2DB3C1A";
	setAttr ".t" -type "double3" 525 -425 800 ;
	setAttr ".rp" -type "double3" -525 425 -800 ;
	setAttr ".sp" -type "double3" -525 425 -800 ;
createNode transform -n "Railing01" -p "Railing01_grp";
	rename -uid "058EE30C-4940-52FE-E2F4-32B6B28D101D";
	setAttr ".rp" -type "double3" -530 480.00003051757812 -695 ;
	setAttr ".sp" -type "double3" -530 480.00003051757812 -695 ;
createNode mesh -n "Railing01Shape" -p "Railing01";
	rename -uid "A3EEA4E5-419C-0CE5-835D-20B09AA60426";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:77]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 18 "f[6]" "f[8]" "f[10:12]" "f[14]" "f[16:18]" "f[20]" "f[22:24]" "f[26]" "f[28:30]" "f[32]" "f[34:35]" "f[60]" "f[62]" "f[64:66]" "f[68]" "f[70:72]" "f[74]" "f[76:77]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr -s 6 ".gtag";
	setAttr ".gtag[0].gtagnm" -type "string" "back";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 13 "f[2]" "f[8]" "f[14]" "f[20]" "f[26]" "f[32]" "f[38]" "f[44]" "f[51]" "f[57]" "f[62]" "f[68]" "f[74]";
	setAttr ".gtag[1].gtagnm" -type "string" "bottom";
	setAttr ".gtag[1].gtagcmp" -type "componentList" 13 "f[3]" "f[9]" "f[15]" "f[21]" "f[27]" "f[33]" "f[39]" "f[45]" "f[49]" "f[55]" "f[63]" "f[69]" "f[75]";
	setAttr ".gtag[2].gtagnm" -type "string" "front";
	setAttr ".gtag[2].gtagcmp" -type "componentList" 12 "f[0]" "f[6]" "f[12]" "f[18]" "f[24]" "f[30]" "f[36]" "f[42]" "f[53]" "f[59:60]" "f[66]" "f[72]";
	setAttr ".gtag[3].gtagnm" -type "string" "left";
	setAttr ".gtag[3].gtagcmp" -type "componentList" 13 "f[5]" "f[11]" "f[17]" "f[23]" "f[29]" "f[35]" "f[41]" "f[47]" "f[50]" "f[56]" "f[65]" "f[71]" "f[77]";
	setAttr ".gtag[4].gtagnm" -type "string" "right";
	setAttr ".gtag[4].gtagcmp" -type "componentList" 13 "f[4]" "f[10]" "f[16]" "f[22]" "f[28]" "f[34]" "f[40]" "f[46]" "f[52]" "f[58]" "f[64]" "f[70]" "f[76]";
	setAttr ".gtag[5].gtagnm" -type "string" "top";
	setAttr ".gtag[5].gtagcmp" -type "componentList" 13 "f[1]" "f[7]" "f[13]" "f[19]" "f[25]" "f[31]" "f[37]" "f[43]" "f[48]" "f[54]" "f[61]" "f[67]" "f[73]";
	setAttr ".pv" -type "double2" 0.36541607975959778 0.99838188465903777 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 312 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" -1.67754757 -5.6810677e-08
		 -1.57754719 -1.1827797e-07 -1.57754719 1.060001254 -1.6775471 1.060001135 -1.5681262
		 0.57819963 -1.5681262 0.67819959 -1.66812599 0.67819959 -1.66812599 0.57819963 -1.57754731
		 1.060001135 -1.67754722 1.060001254 -1.67754745 -1.238659e-07 -1.57754755 -1.5739352e-07
		 -1.66812611 0.67819959 -1.66812611 0.57819963 -1.5681262 0.57819963 -1.5681262 0.67819959
		 -1.67754745 -9.5926225e-08 -1.57754755 -1.4062971e-07 -1.57754731 1.060001254 -1.67754745
		 1.060001254 -1.67754745 -1.3969839e-07 -1.57754731 -1.7508864e-07 -1.57754731 1.060001254
		 -1.67754722 1.060001135 0.34736964 0 0.38736963 0 0.38736963 0.85999995 0.34736964
		 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963 0.33947542 0.34736964
		 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964 0 0.38736966 0
		 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542
		 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697
		 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08 0.38736963 0.86000001
		 0.34736961 0.86000001 0.34736964 0 0.38736963 0 0.38736963 0.85999995 0.34736964
		 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963 0.33947542 0.34736964
		 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964 0 0.38736966 0
		 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542
		 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697
		 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08 0.38736963 0.86000001
		 0.34736961 0.86000001 0.34736964 0 0.38736963 0 0.38736963 0.85999995 0.34736964
		 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963 0.33947542 0.34736964
		 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964 0 0.38736966 0
		 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542
		 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697
		 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08 0.38736963 0.86000001
		 0.34736961 0.86000001 0.34736964 0 0.38736963 0 0.38736963 0.85999995 0.34736964
		 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963 0.33947542 0.34736964
		 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964 0 0.38736966 0
		 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542
		 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697
		 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08 0.38736963 0.86000001
		 0.34736961 0.86000001 0.34736964 0 0.38736963 0 0.38736963 0.85999995 0.34736964
		 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963 0.33947542 0.34736964
		 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964 0 0.38736966 0
		 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542
		 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697
		 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08 0.38736963 0.86000001
		 0.34736961 0.86000001 -1.67754757 -5.6810677e-08 -1.57754719 -1.1827797e-07 -1.57754719
		 1.060001254 -1.6775471 1.060001135 -1.5681262 0.57819963 -1.5681262 0.67819959 -1.66812599
		 0.67819959 -1.66812599 0.57819963 -1.57754731 1.060001135 -1.67754722 1.060001254
		 -1.67754745 -1.238659e-07 -1.57754755 -1.5739352e-07 -1.66812611 0.67819959 -1.66812611
		 0.57819963 -1.5681262 0.57819963 -1.5681262 0.67819959 -1.67754745 -9.5926225e-08
		 -1.57754755 -1.4062971e-07 -1.57754731 1.060001254 -1.67754745 1.060001254 -1.67754745
		 -1.3969839e-07 -1.57754731 -1.7508864e-07 -1.57754731 1.060001254 -1.67754722 1.060001135
		 0.32737505 4.4703484e-08 0.40737504 4.4703484e-08 0.40737504 0.86000013 0.32737505
		 0.86000013 0.40737504 0.39000005 0.40737504 0.47000003 0.32737505 0.47000003 0.32737505
		 0.39000005 0.40737504 0.86000001 0.32737505 0.86000001 0.32737505 4.4703484e-08 0.40737504
		 4.4703484e-08 0.32737505 0.47000003 0.32737505 0.39000005 0.40737504 0.39000005 0.40737504
		 0.47000003 0.32737499 -2.9802322e-08 0.40737498 -2.9802322e-08 0.4073751 0.86000001
		 0.32737511 0.86000001 0.32737505 1.0430813e-07 0.40737504 1.0430813e-07 0.40737504
		 0.86000001 0.32737505 0.86000001 0.39556584 0.55380267 0.32056582 0.55380267 0.32056582
		 0.45380268 0.39556584 0.45380268 0.32056582 0.45380268 0.39556581 0.45380268 0.39556581
		 0.55380267 0.32056582 0.55380267 0.40806583 1.94975936 0.30806583 1.94975936 0.30806583
		 0.049759299 0.40806583 0.049759299 0.39556581 0.049759418 0.39556581 1.94975936 0.32056582
		 1.94975936 0.32056582 0.049759418 0.30806583 0.049759269 0.40806583 0.049759269 0.40806583
		 1.94975936 0.30806583 1.94975936 0.32056582 0.049759209 0.39556581 0.049759209 0.39556581
		 1.94975948 0.32056582 1.94975948 0.39276624 0.41294324 0.35276622 0.41294324 0.35276622
		 0.31294322 0.39276624 0.31294322 0.35276628 0.31294328 0.39276624 0.31294328 0.39276624
		 0.41294324 0.35276628 0.41294324 0.42276615 2.048381805 0.32276616 2.048381805 0.32276633
		 -0.051618069 0.42276633 -0.051618069 0.3927663 -0.051618069 0.39276612 2.048381805
		 0.35276616 2.048381805 0.35276634 -0.051618069 0.32276624 -0.051618248 0.42276627
		 -0.051618248 0.42276627 2.048382044 0.32276624 2.048382044 0.39276618 2.048381805
		 0.3527661 2.048381805 0.35276628 -0.051618069 0.39276636 -0.051618069 0.34736964
		 0 0.38736963 0 0.38736963 0.85999995 0.34736964 0.85999995 0.34736964 0.2994754 0.38736963
		 0.2994754 0.38736963 0.33947542 0.34736964 0.33947542 0.38736966 0.85999995 0.34736964
		 0.85999995;
	setAttr ".uvst[0].uvsp[250:311]" 0.34736964 0 0.38736966 0 0.34736967 0.33947542
		 0.34736967 0.29947543 0.38736963 0.29947543 0.38736963 0.33947542 0.34736958 5.9604645e-08
		 0.38736957 5.9604645e-08 0.38736969 0.86000001 0.3473697 0.86000001 0.34736961 -5.9604645e-08
		 0.38736963 -5.9604645e-08 0.38736963 0.86000001 0.34736961 0.86000001 0.34736964
		 0 0.38736963 0 0.38736963 0.85999995 0.34736964 0.85999995 0.34736964 0.2994754 0.38736963
		 0.2994754 0.38736963 0.33947542 0.34736964 0.33947542 0.38736966 0.85999995 0.34736964
		 0.85999995 0.34736964 0 0.38736966 0 0.34736967 0.33947542 0.34736967 0.29947543
		 0.38736963 0.29947543 0.38736963 0.33947542 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08
		 0.38736969 0.86000001 0.3473697 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08
		 0.38736963 0.86000001 0.34736961 0.86000001 0.34736964 0 0.38736963 0 0.38736963
		 0.85999995 0.34736964 0.85999995 0.34736964 0.2994754 0.38736963 0.2994754 0.38736963
		 0.33947542 0.34736964 0.33947542 0.38736966 0.85999995 0.34736964 0.85999995 0.34736964
		 0 0.38736966 0 0.34736967 0.33947542 0.34736967 0.29947543 0.38736963 0.29947543
		 0.38736963 0.33947542 0.34736958 5.9604645e-08 0.38736957 5.9604645e-08 0.38736969
		 0.86000001 0.3473697 0.86000001 0.34736961 -5.9604645e-08 0.38736963 -5.9604645e-08
		 0.38736963 0.86000001 0.34736961 0.86000001;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 104 ".pt[0:103]" -type "float3"  -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 
		-525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800 -525 425 -800;
	setAttr -s 104 ".vt[0:103]"  0 4 10 0 4 0 0 110.000061035156 10 0 110.000061035156 0
		 -10 110.000061035156 10 -10 110.000061035156 0 -10 4 10 -10 4 0 -2 4 30.20001221
		 -2 4 26.20001221 -2 90 30.20001221 -2 90 26.20001221 -6 90 30.20001221 -6 90 26.20001221
		 -6 4 30.20001221 -6 4 26.20001221 -2 4 129.20001221 -2 4 125.20001221 -2 90 129.20001221
		 -2 90 125.20001221 -6 90 129.20001221 -6 90 125.20001221 -6 4 129.20001221 -6 4 125.20001221
		 -2 4 147.40002441 -2 4 143.40002441 -2 90 147.40002441 -2 90 143.40002441 -6 90 147.40002441
		 -6 90 143.40002441 -6 4 147.40002441 -6 4 143.40002441 -2 4 48.40002441 -2 4 44.40002441
		 -2 90 48.40002441 -2 90 44.40002441 -6 90 48.40002441 -6 90 44.40002441 -6 4 48.40002441
		 -6 4 44.40002441 -2 4 66.59997559 -2 4 62.59997559 -2 90 66.59997559 -2 90 62.59997559
		 -6 90 66.59997559 -6 90 62.59997559 -6 4 66.59997559 -6 4 62.59997559 0 4 210 0 4 200
		 0 110.000061035156 210 0 110.000061035156 200 -10 110.000061035156 210 -10 110.000061035156 200
		 -10 4 210 -10 4 200 -1 4 109 -1 4 101 -1 90 109 -1 90 101 -9 90 109 -9 90 101 -9 4 109
		 -9 4 101 0 97.5 200 0 90 200 0 97.5 10 0 90 10 -10 97.5 10 -10 90 10 -10 97.5 200
		 -10 90 200 0 4 210 0 0 210 0 4 0 0 0 0 -10 4 0 -10 0 0 -10 4 210 -10 0 210 -2 4 165.59997559
		 -2 4 161.59997559 -2 90 165.59997559 -2 90 161.59997559 -6 90 165.59997559 -6 90 161.59997559
		 -6 4 165.59997559 -6 4 161.59997559 -2 4 183.80004883 -2 4 179.80004883 -2 90 183.80004883
		 -2 90 179.80004883 -6 90 183.80004883 -6 90 179.80004883 -6 4 183.80004883 -6 4 179.80004883
		 -2 4 84.79998779 -2 4 80.79998779 -2 90 84.79998779 -2 90 80.79998779 -6 90 84.79998779
		 -6 90 80.79998779 -6 4 84.79998779 -6 4 80.79998779;
	setAttr -s 156 ".ed[0:155]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0 8 9 0 10 11 0 12 13 0 14 15 0 8 10 0 9 11 0 10 12 0
		 11 13 0 12 14 0 13 15 0 14 8 0 15 9 0 16 17 0 18 19 0 20 21 0 22 23 0 16 18 0 17 19 0
		 18 20 0 19 21 0 20 22 0 21 23 0 22 16 0 23 17 0 24 25 0 26 27 0 28 29 0 30 31 0 24 26 0
		 25 27 0 26 28 0 27 29 0 28 30 0 29 31 0 30 24 0 31 25 0 32 33 0 34 35 0 36 37 0 38 39 0
		 32 34 0 33 35 0 34 36 0 35 37 0 36 38 0 37 39 0 38 32 0 39 33 0 40 41 0 42 43 0 44 45 0
		 46 47 0 40 42 0 41 43 0 42 44 0 43 45 0 44 46 0 45 47 0 46 40 0 47 41 0 48 49 0 50 51 0
		 52 53 0 54 55 0 48 50 0 49 51 0 50 52 0 51 53 0 52 54 0 53 55 0 54 48 0 55 49 0 56 57 0
		 58 59 0 60 61 0 62 63 0 56 58 0 57 59 0 58 60 0 59 61 0 60 62 0 61 63 0 62 56 0 63 57 0
		 64 66 0 66 68 0 67 69 0 68 70 0 70 64 0 71 65 0 64 65 0 66 67 0 68 69 0 70 71 0 65 67 0
		 69 71 0 72 74 0 74 76 0 75 77 0 76 78 0 78 72 0 79 73 0 72 73 0 74 75 0 76 77 0 78 79 0
		 73 75 0 77 79 0 80 81 0 82 83 0 84 85 0 86 87 0 80 82 0 81 83 0 82 84 0 83 85 0 84 86 0
		 85 87 0 86 80 0 87 81 0 88 89 0 90 91 0 92 93 0 94 95 0 88 90 0 89 91 0 90 92 0 91 93 0
		 92 94 0 93 95 0 94 88 0 95 89 0 96 97 0 98 99 0 100 101 0 102 103 0 96 98 0 97 99 0
		 98 100 0 99 101 0 100 102 0 101 103 0 102 96 0 103 97 0;
	setAttr -s 78 -ch 312 ".fc[0:77]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 2 3
		f 4 1 7 -3 -7
		mu 0 4 4 5 6 7
		f 4 2 9 -4 -9
		mu 0 4 8 9 10 11
		f 4 3 11 -1 -11
		mu 0 4 12 13 14 15
		f 4 -12 -10 -8 -6
		mu 0 4 16 17 18 19
		f 4 10 4 6 8
		mu 0 4 20 21 22 23
		f 4 12 17 -14 -17
		mu 0 4 24 25 26 27
		f 4 13 19 -15 -19
		mu 0 4 28 29 30 31
		f 4 14 21 -16 -21
		mu 0 4 32 33 34 35
		f 4 15 23 -13 -23
		mu 0 4 36 37 38 39
		f 4 -24 -22 -20 -18
		mu 0 4 40 41 42 43
		f 4 22 16 18 20
		mu 0 4 44 45 46 47
		f 4 24 29 -26 -29
		mu 0 4 48 49 50 51
		f 4 25 31 -27 -31
		mu 0 4 52 53 54 55
		f 4 26 33 -28 -33
		mu 0 4 56 57 58 59
		f 4 27 35 -25 -35
		mu 0 4 60 61 62 63
		f 4 -36 -34 -32 -30
		mu 0 4 64 65 66 67
		f 4 34 28 30 32
		mu 0 4 68 69 70 71
		f 4 36 41 -38 -41
		mu 0 4 72 73 74 75
		f 4 37 43 -39 -43
		mu 0 4 76 77 78 79
		f 4 38 45 -40 -45
		mu 0 4 80 81 82 83
		f 4 39 47 -37 -47
		mu 0 4 84 85 86 87
		f 4 -48 -46 -44 -42
		mu 0 4 88 89 90 91
		f 4 46 40 42 44
		mu 0 4 92 93 94 95
		f 4 48 53 -50 -53
		mu 0 4 96 97 98 99
		f 4 49 55 -51 -55
		mu 0 4 100 101 102 103
		f 4 50 57 -52 -57
		mu 0 4 104 105 106 107
		f 4 51 59 -49 -59
		mu 0 4 108 109 110 111
		f 4 -60 -58 -56 -54
		mu 0 4 112 113 114 115
		f 4 58 52 54 56
		mu 0 4 116 117 118 119
		f 4 60 65 -62 -65
		mu 0 4 120 121 122 123
		f 4 61 67 -63 -67
		mu 0 4 124 125 126 127
		f 4 62 69 -64 -69
		mu 0 4 128 129 130 131
		f 4 63 71 -61 -71
		mu 0 4 132 133 134 135
		f 4 -72 -70 -68 -66
		mu 0 4 136 137 138 139
		f 4 70 64 66 68
		mu 0 4 140 141 142 143
		f 4 72 77 -74 -77
		mu 0 4 144 145 146 147
		f 4 73 79 -75 -79
		mu 0 4 148 149 150 151
		f 4 74 81 -76 -81
		mu 0 4 152 153 154 155
		f 4 75 83 -73 -83
		mu 0 4 156 157 158 159
		f 4 -84 -82 -80 -78
		mu 0 4 160 161 162 163
		f 4 82 76 78 80
		mu 0 4 164 165 166 167
		f 4 84 89 -86 -89
		mu 0 4 168 169 170 171
		f 4 85 91 -87 -91
		mu 0 4 172 173 174 175
		f 4 86 93 -88 -93
		mu 0 4 176 177 178 179
		f 4 87 95 -85 -95
		mu 0 4 180 181 182 183
		f 4 -96 -94 -92 -90
		mu 0 4 184 185 186 187
		f 4 94 88 90 92
		mu 0 4 188 189 190 191
		f 4 -105 -98 103 98
		mu 0 4 192 193 194 195
		f 4 -103 -101 105 101
		mu 0 4 196 197 198 199
		f 4 97 99 100 96
		mu 0 4 200 201 202 203
		f 4 -100 104 107 -106
		mu 0 4 204 205 206 207
		f 4 -99 -107 -102 -108
		mu 0 4 208 209 210 211
		f 4 -104 -97 102 106
		mu 0 4 212 213 214 215
		f 4 -117 -110 115 110
		mu 0 4 216 217 218 219
		f 4 -115 -113 117 113
		mu 0 4 220 221 222 223
		f 4 109 111 112 108
		mu 0 4 224 225 226 227
		f 4 -112 116 119 -118
		mu 0 4 228 229 230 231
		f 4 -111 -119 -114 -120
		mu 0 4 232 233 234 235
		f 4 -116 -109 114 118
		mu 0 4 236 237 238 239
		f 4 120 125 -122 -125
		mu 0 4 240 241 242 243
		f 4 121 127 -123 -127
		mu 0 4 244 245 246 247
		f 4 122 129 -124 -129
		mu 0 4 248 249 250 251
		f 4 123 131 -121 -131
		mu 0 4 252 253 254 255
		f 4 -132 -130 -128 -126
		mu 0 4 256 257 258 259
		f 4 130 124 126 128
		mu 0 4 260 261 262 263
		f 4 132 137 -134 -137
		mu 0 4 264 265 266 267
		f 4 133 139 -135 -139
		mu 0 4 268 269 270 271
		f 4 134 141 -136 -141
		mu 0 4 272 273 274 275
		f 4 135 143 -133 -143
		mu 0 4 276 277 278 279
		f 4 -144 -142 -140 -138
		mu 0 4 280 281 282 283
		f 4 142 136 138 140
		mu 0 4 284 285 286 287
		f 4 144 149 -146 -149
		mu 0 4 288 289 290 291
		f 4 145 151 -147 -151
		mu 0 4 292 293 294 295
		f 4 146 153 -148 -153
		mu 0 4 296 297 298 299
		f 4 147 155 -145 -155
		mu 0 4 300 301 302 303
		f 4 -156 -154 -152 -150
		mu 0 4 304 305 306 307
		f 4 154 148 150 152
		mu 0 4 308 309 310 311;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".dfgi" 402;
createNode transform -n "UCX_Railing01" -p "Railing01_grp";
	rename -uid "C7DC5E2D-474A-E644-6E8C-6E9AE9AA0A64";
	setAttr ".t" -type "double3" -325 0 0 ;
	setAttr ".rp" -type "double3" -210 425.00003051757812 -590 ;
	setAttr ".sp" -type "double3" -210 425.00003051757812 -590 ;
createNode mesh -n "UCX_RailingShape1" -p "UCX_Railing01";
	rename -uid "691F44B8-43EB-8633-A565-748FFA488BE0";
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
	rename -uid "26DDA4E6-4B5B-1452-F556-E3A796ECC804";
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
createNode groupId -n "groupId1060";
	rename -uid "DEC83A94-4C70-2CC1-4865-CAA0E730BC9A";
	setAttr ".ihi" 0;
createNode shadingEngine -n "lambert14SG";
	rename -uid "009F844F-437A-6D9E-4F99-5394D180648D";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo21";
	rename -uid "B4496256-49E5-8297-4B6E-1CAF1719E624";
createNode lambert -n "Misc07_grid";
	rename -uid "0A2BA336-4CA9-5CF5-5CC1-5D80B178929A";
createNode file -n "file13";
	rename -uid "383ECF4D-4C16-C45F-E733-0C865D315909";
Misc07_grid.tga";
	setAttr ".cs" -type "string" "sRGB Encoded Rec.709 (sRGB)";
createNode place2dTexture -n "place2dTexture13";
	rename -uid "DA4E6B63-46A1-DADC-C083-DF80721A4FFC";
createNode groupId -n "groupId1061";
	rename -uid "4F020ADE-4C0A-1746-9652-1596410C3300";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "27B45BAF-46F8-5014-22EA-4B8163CF7899";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode groupId -n "groupId1059";
	rename -uid "729700AD-4A13-2DFA-9EDF-D6908E04B2BE";
	setAttr ".ihi" 0;
createNode displayLayer -n "UCX_GROUP";
	rename -uid "9CA1392F-4710-AF2D-3141-49BA94542D42";
	setAttr ".v" no;
	setAttr ".ufem" -type "stringArray" 0  ;
	setAttr ".do" 2;
createNode displayLayerManager -n "layerManager";
	rename -uid "5F88D234-4404-84F3-2F10-1E9750AF686F";
	setAttr -s 2 ".dli[1]"  2;
	setAttr -s 2 ".dli";
createNode polyNormalPerVertex -n "polyNormalPerVertex27";
	rename -uid "8342634A-4FD3-02E8-04DF-85A216989446";
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
	rename -uid "92FCB4CE-4266-FC0B-DA85-25A57E5DCF79";
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
	rename -uid "42ADECDA-43C1-A031-F5FA-2A98473552A1";
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
	rename -uid "D659F49D-4409-5A94-45B8-EC8E1ABA34B1";
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
	rename -uid "50334440-4A5C-C838-24C7-F69D86928519";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:5]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dl" yes;
createNode polyAutoProj -n "polyAutoProj110";
	rename -uid "8D7682FC-48E9-D693-B891-95B6D0AC0221";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:5]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dl" yes;
createNode materialInfo -n "materialInfo24";
	rename -uid "4A660016-415A-5814-4597-D782FBBCEED9";
createNode shadingEngine -n "lambert17SG";
	rename -uid "3B465AD5-46B3-5C80-7CDB-A29C33180EAF";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode lambert -n "M_UCX";
	rename -uid "2507184D-4425-2006-6DB6-C0A13EA4EC97";
	setAttr ".c" -type "float3" 1 0 0 ;
	setAttr ".it" -type "float3" 0.68387097 0.68387097 0.68387097 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "7DFBF705-499B-A4E0-3D55-92A560341539";
	setAttr -s 6 ".lnk";
	setAttr -s 6 ".slnk";
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
	setAttr -s 4 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 8 ".s";
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
connectAttr "groupId1060.id" "Railing01Shape.iog.og[0].gid";
connectAttr "lambert14SG.mwc" "Railing01Shape.iog.og[0].gco";
connectAttr "groupId1061.id" "Railing01Shape.iog.og[1].gid";
connectAttr "textureEditorIsolateSelectSet.mwc" "Railing01Shape.iog.og[1].gco";
connectAttr "groupId1059.id" "Railing01Shape.ciog.cog[0].cgid";
connectAttr "UCX_GROUP.di" "UCX_Railing01.do";
connectAttr "polyNormalPerVertex27.out" "UCX_RailingShape1.i";
connectAttr "polyTweakUV59.uvtk[0]" "UCX_RailingShape1.uvst[0].uvtw";
connectAttr "Misc07_grid.oc" "lambert14SG.ss";
connectAttr "Railing01Shape.ciog.cog[0]" "lambert14SG.dsm" -na;
connectAttr "Railing01Shape.iog.og[0]" "lambert14SG.dsm" -na;
connectAttr "groupId1060.msg" "lambert14SG.gn" -na;
connectAttr "lambert14SG.msg" "materialInfo21.sg";
connectAttr "Misc07_grid.msg" "materialInfo21.m";
connectAttr "file13.msg" "materialInfo21.t" -na;
connectAttr "file13.oc" "Misc07_grid.c";
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
connectAttr "groupId1061.msg" "textureEditorIsolateSelectSet.gn" -na;
connectAttr "Railing01Shape.iog.og[1]" "textureEditorIsolateSelectSet.dsm" -na;
connectAttr "layerManager.dli[1]" "UCX_GROUP.id";
connectAttr "polyTweakUV59.out" "polyNormalPerVertex27.ip";
connectAttr "polyLayoutUV116.out" "polyTweakUV59.ip";
connectAttr "polyLayoutUV115.out" "polyLayoutUV116.ip";
connectAttr "polyAutoProj111.out" "polyLayoutUV115.ip";
connectAttr "polyAutoProj110.out" "polyAutoProj111.ip";
connectAttr "UCX_RailingShape1.wm" "polyAutoProj111.mp";
connectAttr "polySurfaceShape78.o" "polyAutoProj110.ip";
connectAttr "UCX_RailingShape1.wm" "polyAutoProj110.mp";
connectAttr "lambert17SG.msg" "materialInfo24.sg";
connectAttr "M_UCX.msg" "materialInfo24.m";
connectAttr "M_UCX.oc" "lambert17SG.ss";
connectAttr "UCX_RailingShape1.iog" "lambert17SG.dsm" -na;
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
connectAttr "Misc07_grid.msg" ":defaultShaderList1.s" -na;
connectAttr "M_UCX.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture13.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "file13.msg" ":defaultTextureList1.tx" -na;
// End of Railing01.ma
