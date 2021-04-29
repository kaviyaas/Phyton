Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(0,9):
	if (i==4):
	  break
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(0,9):
	if (i==4):
	  break
	print(i)

	
0
1
2
3
>>> for i in range(1,9):
	if(i==4):
	 break
	print(i)

	
1
2
3
>>> for i in range(1,9):
	if(i==4):
	 break
	print(i)

	
1
2
3
>>> for i in range(1,9):
	print(i)
	if(i==4):
	 break

	
1
2
3
4
>>> for i in range(1,100):
	print(i)
	if(i==50):
	 break

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
>>> for i in range(0,100):
	if(i==56):
	 break
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(0,100):
	if(i==56):
	 break
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
>>> for i in range(0,10):
	print(i)
	if(i==4):
	 continue

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,10):
	print(i)
	if(i==5):
	 continue

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,5):
	if(i==5):
	 continue
	print(i)

	
0
1
2
3
4
>>> for i in range(0,10):
	if(i==5):
	 continue
	print(i)

	
0
1
2
3
4
6
7
8
9
>>> 24
24
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self.name2):
		
SyntaxError: invalid syntax
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				 if(j==4)
				 
SyntaxError: unexpected indent
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				 if(j==4):
					 
SyntaxError: unexpected indent
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				print(self.name1)
				print(self.name2)
				if(j==4):
				 break

				
>>> s=sample("kav")
>>> s.getdata("kavi")
>>> s.getdata1("kaviya")
>>> s.display()
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
kav
kavi
kaviya
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				if(j==4):
				 break
			for k in range(0,5):
				print(self.name1)
				if(j==4):
				 break
	                print(self.name2)
	                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				if(j==4):
				 break
			for k in range(0,5):
				print(self.name1)
				if(j==4):
				 break
	        print(self.name2 )
	        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				if(j==4):
				 break
			for k in range(0,5):
				print(self.name1)
				if(k==4):
				 break
		print(self.name2)
		if(i==4):
		 break
		
SyntaxError: 'break' outside loop
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				if(j==4):
				 break
			for k in range(0,5):
				print(self.name1)
				if(k==4):
				 break
		  if(i==4):
			  
SyntaxError: unindent does not match any outer indentation level
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,name1):
		self.name1=name1
	def getdata1(self,name2):
		self.name2=name2
	def display(self):
		for i in range(0,5):
			for j in range(0,5):
				print(self.name)
				if(j==4):
				 break
			for k in range(0,5):
				print(self.name1)
				if(k==4):
				 break
			for l in range(0,5):
				print(self.name2)
				if(l==4):
				 break

				
>>> s=sample("kaviya")
>>> s.getdata("healthy")
>>> s.getdata1("steps")
>>> s.display()
kaviya
kaviya
kaviya
kaviya
kaviya
healthy
healthy
healthy
healthy
healthy
steps
steps
steps
steps
steps
kaviya
kaviya
kaviya
kaviya
kaviya
healthy
healthy
healthy
healthy
healthy
steps
steps
steps
steps
steps
kaviya
kaviya
kaviya
kaviya
kaviya
healthy
healthy
healthy
healthy
healthy
steps
steps
steps
steps
steps
kaviya
kaviya
kaviya
kaviya
kaviya
healthy
healthy
healthy
healthy
healthy
steps
steps
steps
steps
steps
kaviya
kaviya
kaviya
kaviya
kaviya
healthy
healthy
healthy
healthy
healthy
steps
steps
steps
steps
steps
>>> for i in range(0,4):
	print(i)
	if(i==4):
	 break

	
0
1
2
3
>>> for i in range(0,4):
	if(i==4):
	 break
	print(i)

	
0
1
2
3
>>> class sample():
	def __init__(self,name):
		self.name=name
	def __init1__(self,name1):
		self.name1=name1
	def __init2__(self,age):
		self.age=age
	def __init3__(self.age1):
		
SyntaxError: invalid syntax
>>> class sample():
	def __init__(self,name):
		self.name=name
	def __init1__(self,name1):
		self.name1=name1
	def __init2__(self,age):
		self.age=age
	def __init3__(self,age1):
		self.age1=age1
	def display(self):
		print(self.name)
		print(self.name1)
		print(self.age)
		print(self.age1)

		
>>> s=sample("mangai")
>>> s.__init1__("vivetha")
>>> s.__init2__(22)
>>> s.__init3__(21)
>>> s.display()
mangai
vivetha
22
21
>>> class sample():
	def __init__(self,num):
		self.num=num
	def display(self):
		while(True):
			print(num)
			if(num < 10):
				print(num)
				num +=2

				
>>> s=sample(1)
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    s.display()
  File "<pyshell#140>", line 6, in display
    print(num)
UnboundLocalError: local variable 'num' referenced before assignment
>>> class sample():
	def __init__(self,num):
		self.num=num
	def display(self):
		while(True):
			print(self.num)
			if(self.num < 10):
				print(self.num)
				self.num +=2

				
>>> s=sample(1)
>>> s.display()
1
1
3
3
5
5
7
7
9
9
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s.display()
  File "<pyshell#144>", line 6, in display
    print(self.num)
KeyboardInterrupt
>>> class sample():
	def __init__(self,num):
		self.num=num
	def display(self):
		while(True):
			print(self.num)
			self.num+=2
			if(self.num < 10):
				print(self.num)
				if(i==10):
				 break

				
>>> s=sample(1)
>>> s.display()
1
3
3
5
5
7
7
9
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
101
103
105
107
109
111
113
115
117
119
121
123
125
127
129
131
133
135
137
139
141
143
145
147
149
151
153
155
157
159
161
163
165
167
169
171
173
175
177
179
181
183
185
187
189
191
193
195
197
199
201
203
205
207
209
211
213
215
217
219
221
223
225
227
229
231
233
235
237
239
241
243
245
247
249
251
253
255
257
259
261
263
265
267
269
271
273
275
277
279
281
283
285
287
289
291
293
295
297
299
301
303
305
307
309
311
313
315
317
319
321
323
325
327
329
331
333
335
337
339
341
343
345
347
349
351
353
355
357
359
361
363
365
367
369
371
373
375
377
379
381
383
385
387
389
391
393
395
397
399
401
403
405
407
409
411
413
415
417
419
421
423
425
427
429
431
433
435
437
439
441
443
445
447
449
451
453
455
457
459
461
463
465
467
469
471
473
475
477
479
481
483
485
487
489
491
493
495
497
499
501
503
505
507
509
511
513
515
517
519
521
523
525
527
529
531
533
535
537
539
541
543
545
547
549
551
553
555
557
559
561
563
565
567
569
571
573
575
577
579
581
583
585
587
589
591
593
595
597
599
601
603
605
607
609
611
613
615
617
619
621
623
625
627
629
631
633
635
637
639
641
643
645
647
649
651
653
655
657
659
661
663
665
667
669
671
673
675
677
679
681
683
685
687
689
691
693
695
697
699
701
703
705
707
709
711
713
715
717
719
721
723
725
727
729
731
733
735
737
739
741
743
745
747
749
751
753
755
757
759
761
763
765
767
769
771
773
775
777
779
781
783
785
787
789
791
793
795
797
799
801
803
805
807
809
811
813
815
817
819
821
823
825
827
829
831
833
835
837
839
841
843
845
847
849
851
853
855
857
859
861
863
865
867
869
871
873
875
877
879
881
883
885
887
889
891
893
895
897
899
901
903
905
907
909
911
913
915
917
919
921
923
925
927
929
931
933
935
937
939
941
943
945
947
949
951
953
955
957
959
961
963
965
967
969
971
973
975
977
979
981
983
985
987
989
991
993
995
997
999
1001
1003
1005
1007
1009
1011
1013
1015
1017
1019
1021
1023
1025
1027
1029
1031
1033
1035
1037
1039
1041
1043
1045
1047
1049
1051
1053
1055
1057
1059
1061
1063
1065
1067
1069
1071
1073
1075
1077
1079
1081
1083
1085
1087
1089
1091
1093
1095
1097
1099
1101
1103
1105
1107
1109
1111
1113
1115
1117
1119
1121
1123
1125
1127
1129
1131
1133
1135
1137
1139
1141
1143
1145
1147
1149
1151
1153
1155
1157
1159
1161
1163
1165
1167
1169
1171
1173
1175
1177
1179
1181
1183
1185
1187
1189
1191
1193
1195
1197
1199
1201
1203
1205
1207
1209
1211
1213
1215
1217
1219
1221
1223
1225
1227
1229
1231
1233
1235
1237
1239
1241
1243
1245
1247
1249
1251
1253
1255
1257
1259
1261
1263
1265
1267
1269
1271
1273
1275
1277
1279
1281
1283
1285
1287
1289
1291
1293
1295
1297
1299
1301
1303
1305
1307
1309
1311
1313
1315
1317
1319
1321
1323
1325
1327
1329
1331
1333
1335
1337
1339
1341
1343
1345
1347
1349
1351
1353
1355
1357
1359
1361
1363
1365
1367
1369
1371
1373
1375
1377
1379
1381
1383
1385
1387
1389
1391
1393
1395
1397
1399
1401
1403
1405
1407
1409
1411
1413
1415
1417
1419
1421
1423
1425
1427
1429
1431
1433
1435
1437
1439
1441
1443
1445
1447
1449
1451
1453
1455
1457
1459
1461
1463
1465
1467
1469
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s.display()
  File "<pyshell#149>", line 6, in display
    print(self.num)
KeyboardInterrupt
>>> 
>>> class sample():
	def __init__(self,num):
		self.num=num
	def display(self):
		while(True):
			print(self.num)
			self.num+=2
			if(self.num > 10):
				break

			
>>> s=sample(1)
>>> s.display()
1
3
5
7
9
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,age):
		self.age=age
	def display(self):
		print("name=%s",%self.name)
		
SyntaxError: invalid syntax
>>> class sample():
	def __init__(self,name):
		self.name=name
	def getdata(self,age):
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("f{self.age})
		      
SyntaxError: EOL while scanning string literal
>>> 
>>> class sample():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x+self.y )

		
>>> s=sample(12,67)
>>> s.display()
79
>>> sample __module__
SyntaxError: invalid syntax
>>> sample.__module__
'__main__'
>>> sample.__module__
'__main__'
>>> sample.__name__
'sample'
>>> sample.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function sample.__init__ at 0x00000214B36951F0>, 'display': <function sample.display at 0x00000214B3695280>, '__dict__': <attribute '__dict__' of 'sample' objects>, '__weakref__': <attribute '__weakref__' of 'sample' objects>, '__doc__': None})
>>> sample.__weakref__
<attribute '__weakref__' of 'sample' objects>
>>> sample.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function sample.__init__ at 0x00000214B36951F0>, 'display': <function sample.display at 0x00000214B3695280>, '__dict__': <attribute '__dict__' of 'sample' objects>, '__weakref__': <attribute '__weakref__' of 'sample' objects>, '__doc__': None})
>>> isinstance(s,sample)
True
>>> isinstance(s1,sample)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    isinstance(s1,sample)
NameError: name 's1' is not defined
>>> getattr(s,'x')
12
>>> getattr(s,'y')
67
>>> setattr(s,'x',100)
>>> s.x
100
>>> s.display()
167
>>> id(s)
2287932356496
>>> class sample():
	"""this is derived by me"""
	def __init__(self,name,age,grade):
		self.name=name
		self.age=age
		self.grade=grade
	def display(self):
		print("name of the student=%s"%self.name)
		print(f"age of the student{self.age}")
		print("grade={}.format{self.grade}")

		
>>> s=sample("kaviya",4,"O")
>>> s.display()
name of the student=kaviya
age of the student4
grade={}.format{self.grade}
>>> class sample():
	"""this is derived by me"""
	def __init__(self,name,age,grade):
		self.name=name
		self.age=age
		self.grade=grade
	def display(self):
		print("name of the student=%s"%self.name)
		print(f"age of the student{self.age}")
		print("grade={}".format{self.grade})