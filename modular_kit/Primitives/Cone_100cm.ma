//Maya ASCII 2026 scene
//Name: Cone_100cm.ma
//Last modified: Thu, Feb 19, 2026 01:02:01 PM
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
fileInfo "UUID" "3D3CB130-4C8C-D298-B0F1-96886CAA89DC";
fileInfo "license" "education";
createNode transform -n "Cone_100cm";
	rename -uid "780B458F-4A71-978F-0873-68BE285B4CAE";
createNode mesh -n "Cone_100cmShape" -p "Cone_100cm";
	rename -uid "5DCA0E62-4419-E1B1-8165-BA919F228E0E";
	setAttr -k off ".v";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:39]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "sides";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[0:39]";
	setAttr ".pv" -type "double2" 0.28480333089828491 -7.152557373046875e-07 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 84 ".uvst[0].uvsp[0:83]" -type "float2" 0.28480333 -7.1525574e-07
		 0.20963581 1.000001311302 0.14091897 -7.1525574e-07 0.28480333 -7.1525574e-07 0.42932022
		 -7.1525574e-07 0.35710317 0.99999917 -0.14959741 0 0 0 0 1 -0.44667768 3.5762787e-07
		 -0.30216074 3.5762787e-07 -0.37376505 0.99999952 0 0 0.14091897 0 1.1920929e-07 1.000000596046
		 -0.5941596 -1.3113022e-06 -0.44964266 -1.3113022e-06 -0.50027859 1.000001192093 -0.29919577
		 5.9604645e-08 -0.14959741 5.9604645e-08 -0.20981644 0.99999976 0.43228495 -2.2649765e-06
		 0.57680261 -2.2649765e-06 0.49467486 1.000000596046 -0.14959741 0 0 0 0 0.99999797
		 0 0 0.14091897 0 0 0.99999815 -0.2938925 1.59549379 -0.15450859 1.52447176 0 2 0
		 1.50000048 -0.40450811 1.70610833 0.15450859 1.52447176 -0.47552776 1.84549165 0.29389226
		 1.59549379 -0.49999952 2 0.40450811 1.70610833 0.47552776 1.84549189 0.49999952 2
		 0.14091897 -7.1525574e-07 0.28480333 -7.1525574e-07 0.20963581 1.000001311302 0.28480333
		 -7.1525574e-07 0.42932022 -7.1525574e-07 0.35710317 0.99999917 -0.14959741 0 0 0
		 0 1 -0.44667768 3.5762787e-07 -0.30216074 3.5762787e-07 -0.37376505 0.99999952 0
		 0 0.14091897 0 1.1920929e-07 1.000000596046 -0.5941596 -1.3113022e-06 -0.44964266
		 -1.3113022e-06 -0.50027859 1.000001192093 -0.29919577 5.9604645e-08 -0.14959741 5.9604645e-08
		 -0.20981644 0.99999976 0.43228495 -2.2649765e-06 0.57680261 -2.2649765e-06 0.49467486
		 1.000000596046 -0.14959741 0 0 0 0 0.99999797 0 0 0.14091897 0 0 0.99999815 -0.2938925
		 1.59549379 -0.15450859 1.52447176 0 2 -0.40450811 1.70610833 0 1.50000048 0.15450859
		 1.52447176 0.29389226 1.59549379 0.40450811 1.70610833 0.47552776 1.84549189 -0.47552776
		 1.84549165 -0.49999952 2 0.49999952 2;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".pt[0:21]" -type "float3"  -1023.7764 25 7.7254257 -1020.2254 
		25 14.694633 -1000 75 0 -1014.6946 25 20.225426 -1023.7764 25 -7.7254333 -1025 25 
		0 -1014.6946 25 -20.225433 -1020.2254 25 -14.694633 -1007.7254 25 -23.776413 -1000 
		25 -25 -1000 25 25.000008 -1007.7254 25 23.776413 -1000 25 0 -976.22357 25 -7.7254333 
		-979.7746 25 -14.694633 -985.30536 25 -20.225433 -976.22357 25 7.7254257 -975 25 
		0 -985.30536 25 20.225426 -979.7746 25 14.694633 -992.2746 25 23.776421 -992.2746 
		25 -23.776413;
	setAttr -s 22 ".vt[0:21]"  976.22357178 -25 7.72542477 979.77459717 -25 14.69463158
		 1000 25 -2.9558578e-12 985.30535889 -25 20.22542572 976.22357178 -25 -7.72542667
		 975 -25 -8.493721e-07 985.30535889 -25 -20.22542763 979.77459717 -25 -14.69463348
		 992.27459717 -25 -23.77641678 1000 -25 -25.000003814697 1000 -25 25.000003814697
		 992.27459717 -25 23.77641487 1000 -25 -2.9558578e-12 1023.77642822 -25 -7.72542477
		 1020.22540283 -25 -14.69463158 1014.69464111 -25 -20.22542572 1023.77642822 -25 7.72542667
		 1025 -25 8.4936619e-07 1014.69464111 -25 20.22542763 1020.22540283 -25 14.69463348
		 1007.72540283 -25 23.77641678 1007.72540283 -25 -23.77641487;
	setAttr -s 60 ".ed[0:59]"  0 1 0 0 2 1 1 2 1 1 3 0 3 2 1 4 5 0 4 2 1
		 5 2 1 6 7 0 6 2 1 7 2 1 5 0 0 8 6 0 8 2 1 7 4 0 9 2 1 10 2 1 3 11 0 11 2 1 11 10 0
		 9 8 0 0 12 1 1 12 1 3 12 1 4 12 1 5 12 1 6 12 1 7 12 1 8 12 1 9 12 1 10 12 1 11 12 1
		 13 14 0 13 2 1 14 2 1 14 15 0 15 2 1 16 17 0 16 2 1 17 2 1 18 19 0 18 2 1 19 2 1
		 17 13 0 20 18 0 20 2 1 19 16 0 15 21 0 21 2 1 21 9 0 10 20 0 13 12 1 14 12 1 15 12 1
		 16 12 1 17 12 1 18 12 1 19 12 1 20 12 1 21 12 1;
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
		f 3 0 2 -2
		mu 0 3 2 0 1
		f 3 3 4 -3
		mu 0 3 3 4 5
		f 3 5 7 -7
		mu 0 3 6 7 8
		f 3 8 10 -10
		mu 0 3 9 10 11
		f 3 11 1 -8
		mu 0 3 12 13 14
		f 3 12 9 -14
		mu 0 3 15 16 17
		f 3 14 6 -11
		mu 0 3 18 19 20
		f 3 17 18 -5
		mu 0 3 21 22 23
		f 3 19 16 -19
		mu 0 3 24 25 26
		f 3 20 13 -16
		mu 0 3 27 28 29
		f 3 -1 21 -23
		mu 0 3 30 31 32
		f 3 -4 22 -24
		mu 0 3 34 30 32
		f 3 -6 24 -26
		mu 0 3 33 35 32
		f 3 -9 26 -28
		mu 0 3 37 39 32
		f 3 -12 25 -22
		mu 0 3 31 33 32
		f 3 -13 28 -27
		mu 0 3 39 40 32
		f 3 -15 27 -25
		mu 0 3 35 37 32
		f 3 -18 23 -32
		mu 0 3 36 34 32
		f 3 -20 31 -31
		mu 0 3 38 36 32
		f 3 -21 29 -29
		mu 0 3 40 41 32
		f 3 32 34 -34
		mu 0 3 42 43 44
		f 3 35 36 -35
		mu 0 3 45 46 47
		f 3 37 39 -39
		mu 0 3 48 49 50
		f 3 40 42 -42
		mu 0 3 51 52 53
		f 3 43 33 -40
		mu 0 3 54 55 56
		f 3 44 41 -46
		mu 0 3 57 58 59
		f 3 46 38 -43
		mu 0 3 60 61 62
		f 3 47 48 -37
		mu 0 3 63 64 65
		f 3 49 15 -49
		mu 0 3 66 67 68
		f 3 50 45 -17
		mu 0 3 69 70 71
		f 3 -33 51 -53
		mu 0 3 72 73 74
		f 3 -36 52 -54
		mu 0 3 75 72 74
		f 3 -38 54 -56
		mu 0 3 76 77 74
		f 3 -41 56 -58
		mu 0 3 78 79 74
		f 3 -44 55 -52
		mu 0 3 73 76 74
		f 3 -45 58 -57
		mu 0 3 79 80 74
		f 3 -47 57 -55
		mu 0 3 77 78 74
		f 3 -48 53 -60
		mu 0 3 81 75 74
		f 3 -50 59 -30
		mu 0 3 82 81 74
		f 3 -51 30 -59
		mu 0 3 80 83 74;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode mesh -n "polySurfaceShape5" -p "Cone_100cm";
	rename -uid "12A69C56-496B-FDA5-8C5B-C58E351A8E10";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:39]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "sides";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "f[0:39]";
	setAttr ".pv" -type "double2" -0.99999997019767761 0.50000044703483582 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 84 ".uvst[0].uvsp[0:83]" -type "float2" -0.85759836 -5.9604645e-08
		 -0.89907265 0.50000095 -0.92985737 -5.9604645e-08 -0.8575983 -5.9604645e-08 -0.78533989
		 -5.9604645e-08 -0.82595307 0.49999988 -1.075856686 2.9802322e-07 -1 2.9802322e-07
		 -1 0.5000003 -1.22333884 4.61936e-07 -1.15108037 4.61936e-07 -1.19857943 0.50000006
		 -1 2.9802322e-07 -0.93133962 2.9802322e-07 -0.99999994 0.5000006 -1.2970798 -3.5762787e-07
		 -1.22482133 -3.5762787e-07 -1.25688577 0.50000089 -1.14959788 3.2782555e-07 -1.077338934
		 3.2782555e-07 -1.11537063 0.50000018 -0.78385752 -8.3446503e-07 -0.71159869 -8.3446503e-07
		 -0.75 0.5000006 -0.71011627 4.0233135e-07 -0.63785779 4.0233135e-07 -0.67847127 0.4999994
		 -1.37082076 7.4505806e-07 -1.29856217 7.4505806e-07 -1.34003639 0.49999982 -0.14845777
		 1.19774699 -0.07876581 1.16223598 -0.0015115142 1.4000001 -0.0015115142 1.15000033
		 -0.20376557 1.25305426 0.075742781 1.16223598 -0.2392754 1.32274592 0.14543462 1.19774699
		 -0.25151128 1.4000001 0.20074254 1.25305426 0.23625237 1.32274604 0.24848825 1.4000001
		 -0.92985737 -5.9604645e-08 -0.85759836 -5.9604645e-08 -0.89907265 0.50000095 -0.8575983
		 -5.9604645e-08 -0.78533989 -5.9604645e-08 -0.82595307 0.49999988 -1.075856686 2.9802322e-07
		 -1 2.9802322e-07 -1 0.5000003 -1.22333884 4.61936e-07 -1.15108037 4.61936e-07 -1.19857943
		 0.50000006 -1 2.9802322e-07 -0.93133962 2.9802322e-07 -0.99999994 0.5000006 -1.2970798
		 -3.5762787e-07 -1.22482133 -3.5762787e-07 -1.25688577 0.50000089 -1.14959788 3.2782555e-07
		 -1.077338934 3.2782555e-07 -1.11537063 0.50000018 -0.78385752 -8.3446503e-07 -0.71159869
		 -8.3446503e-07 -0.75 0.5000006 -0.71011627 4.0233135e-07 -0.63785779 4.0233135e-07
		 -0.67847127 0.4999994 -1.37082076 7.4505806e-07 -1.29856217 7.4505806e-07 -1.34003639
		 0.49999982 -0.14845777 1.19774699 -0.07876581 1.16223598 -0.0015115142 1.4000001
		 -0.20376557 1.25305426 -0.0015115142 1.15000033 0.075742781 1.16223598 0.14543462
		 1.19774699 0.20074254 1.25305426 0.23625237 1.32274604 -0.2392754 1.32274592 -0.25151128
		 1.4000001 0.24848825 1.4000001;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".vt[0:21]"  976.22357178 -25 7.72542477 979.77459717 -25 14.69463158
		 1000 25 -2.9558578e-12 985.30535889 -25 20.22542572 976.22357178 -25 -7.72542667
		 975 -25 -8.493721e-07 985.30535889 -25 -20.22542763 979.77459717 -25 -14.69463348
		 992.27459717 -25 -23.77641678 1000 -25 -25.000003814697 1000 -25 25.000003814697
		 992.27459717 -25 23.77641487 1000 -25 -2.9558578e-12 1023.77642822 -25 -7.72542477
		 1020.22540283 -25 -14.69463158 1014.69464111 -25 -20.22542572 1023.77642822 -25 7.72542667
		 1025 -25 8.4936619e-07 1014.69464111 -25 20.22542763 1020.22540283 -25 14.69463348
		 1007.72540283 -25 23.77641678 1007.72540283 -25 -23.77641487;
	setAttr -s 60 ".ed[0:59]"  0 1 0 0 2 1 1 2 1 1 3 0 3 2 1 4 5 0 4 2 1
		 5 2 1 6 7 0 6 2 1 7 2 1 5 0 0 8 6 0 8 2 1 7 4 0 9 2 0 10 2 0 3 11 0 11 2 1 11 10 0
		 9 8 0 0 12 1 1 12 1 3 12 1 4 12 1 5 12 1 6 12 1 7 12 1 8 12 1 9 12 0 10 12 0 11 12 1
		 13 14 0 13 2 1 14 2 1 14 15 0 15 2 1 16 17 0 16 2 1 17 2 1 18 19 0 18 2 1 19 2 1
		 17 13 0 20 18 0 20 2 1 19 16 0 15 21 0 21 2 1 21 9 0 10 20 0 13 12 1 14 12 1 15 12 1
		 16 12 1 17 12 1 18 12 1 19 12 1 20 12 1 21 12 1;
	setAttr -s 48 ".n[0:47]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20;
	setAttr -s 40 -ch 120 ".fc[0:39]" -type "polyFaces" 
		f 3 0 2 -2
		mu 0 3 2 0 1
		f 3 3 4 -3
		mu 0 3 3 4 5
		f 3 5 7 -7
		mu 0 3 6 7 8
		f 3 8 10 -10
		mu 0 3 9 10 11
		f 3 11 1 -8
		mu 0 3 12 13 14
		f 3 12 9 -14
		mu 0 3 15 16 17
		f 3 14 6 -11
		mu 0 3 18 19 20
		f 3 17 18 -5
		mu 0 3 21 22 23
		f 3 19 16 -19
		mu 0 3 24 25 26
		f 3 20 13 -16
		mu 0 3 27 28 29
		f 3 -1 21 -23
		mu 0 3 30 31 32
		f 3 -4 22 -24
		mu 0 3 34 30 32
		f 3 -6 24 -26
		mu 0 3 33 35 32
		f 3 -9 26 -28
		mu 0 3 37 39 32
		f 3 -12 25 -22
		mu 0 3 31 33 32
		f 3 -13 28 -27
		mu 0 3 39 40 32
		f 3 -15 27 -25
		mu 0 3 35 37 32
		f 3 -18 23 -32
		mu 0 3 36 34 32
		f 3 -20 31 -31
		mu 0 3 38 36 32
		f 3 -21 29 -29
		mu 0 3 40 41 32
		f 3 32 34 -34
		mu 0 3 42 43 44
		f 3 35 36 -35
		mu 0 3 45 46 47
		f 3 37 39 -39
		mu 0 3 48 49 50
		f 3 40 42 -42
		mu 0 3 51 52 53
		f 3 43 33 -40
		mu 0 3 54 55 56
		f 3 44 41 -46
		mu 0 3 57 58 59
		f 3 46 38 -43
		mu 0 3 60 61 62
		f 3 47 48 -37
		mu 0 3 63 64 65
		f 3 49 15 -49
		mu 0 3 66 67 68
		f 3 50 45 -17
		mu 0 3 69 70 71
		f 3 -33 51 -53
		mu 0 3 72 73 74
		f 3 -36 52 -54
		mu 0 3 75 72 74
		f 3 -38 54 -56
		mu 0 3 76 77 74
		f 3 -41 56 -58
		mu 0 3 78 79 74
		f 3 -44 55 -52
		mu 0 3 73 76 74
		f 3 -45 58 -57
		mu 0 3 79 80 74
		f 3 -47 57 -55
		mu 0 3 77 78 74
		f 3 -48 53 -60
		mu 0 3 81 75 74
		f 3 -50 59 -30
		mu 0 3 82 81 74
		f 3 -51 30 -59
		mu 0 3 80 83 74;
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
// End of Cone_100cm.ma
