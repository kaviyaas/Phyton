Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=6
>>> while(i>10):
	print("true")
else:
	print("false")

	
false
>>> i=0
>>> while(i<10):
	print(i)
	i+=1

	
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
>>> 
>>> range(0,10)
range(0, 10)
>>> range(2,3)
range(2, 3)
>>> range(10)
range(0, 10)
>>> for i in range(0,10):
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
>>> for i in range(0,10,2):
	print(i)

	
0
2
4
6
8
>>> for i in range(0,100,5):
	print(i,end="")

	
05101520253035404550556065707580859095
>>> for i in range(0,13):
	print(i,end="")

	
0123456789101112
>>> for i in range(4)
SyntaxError: invalid syntax
>>> for i in range(4):
	for j ij range(5):
		
SyntaxError: invalid syntax
>>> for i in range(4):
	for j in range(3):
		print(j)

		
0
1
2
0
1
2
0
1
2
0
1
2
>>> for i in range(10):
	for j in range(6):
		print(j)

		
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
>>> for i in range(23):
	for j in range(4):
		print(i)

		
0
0
0
0
1
1
1
1
2
2
2
2
3
3
3
3
4
4
4
4
5
5
5
5
6
6
6
6
7
7
7
7
8
8
8
8
9
9
9
9
10
10
10
10
11
11
11
11
12
12
12
12
13
13
13
13
14
14
14
14
15
15
15
15
16
16
16
16
17
17
17
17
18
18
18
18
19
19
19
19
20
20
20
20
21
21
21
21
22
22
22
22
>>> for i in range(0,10):
	for j in range(5):
		print(i,j)

		
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
5 0
5 1
5 2
5 3
5 4
6 0
6 1
6 2
6 3
6 4
7 0
7 1
7 2
7 3
7 4
8 0
8 1
8 2
8 3
8 4
9 0
9 1
9 2
9 3
9 4
>>> for i in range(0,3):
	for j in range(0,2):
		print(i,j end="")
		
SyntaxError: invalid syntax
>>> 
>>> for i in range(0,3):
	for j in range(0,2):
		print(i,j,end="")

		
0 00 11 01 12 02 1
>>> for i in range(124):
	print(chr(i),end="")

	
	

 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{
>>> for i in range(56):
	print(chr(i))

	









	
























 
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
0
1
2
3
4
5
6
7
>>> for i in range(65,91):
	print(chr(i))

	
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
>>> for i in range(66,90):
	print(chr(i))

	
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
>>> for i in range(65,77):
	print(chr(i),end="")

	
ABCDEFGHIJKL
>>> ord('&')
38
>>> ord('}')
125
>>> for(i in range(5)):
	
SyntaxError: invalid syntax
>>> for i in range(5):
	for j in range(4):
		print(j,end="")

		
01230123012301230123
>>> for i in range(5):
	for j in range(4):
		print(j)
	print(end="")

	
0
1
2
3
0
1
2
3
0
1
2
3
0
1
2
3
0
1
2
3
>>> for i in range(6):
	for j in range(5):
		print(j)
	print("")

	
0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

>>> for i in range(4):
	for j in range(3):
		print(i,j)
	print("")

	
0 0
0 1
0 2

1 0
1 1
1 2

2 0
2 1
2 2

3 0
3 1
3 2

>>> for i in range(5):
	for j in range(3):
		print(i,j)
		print("\n")

		
0 0


0 1


0 2


1 0


1 1


1 2


2 0


2 1


2 2


3 0


3 1


3 2


4 0


4 1


4 2


>>> for i in range(0,5):
	for j in range(0,i):
		print(j)

		
0
0
1
0
1
2
0
1
2
3
>>> for i in range(0,5)
SyntaxError: invalid syntax
>>> for i in range(0,5):
	for j in range(0,3):
		print(j)

		
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
>>> for i in range(0,5):
	for j in range(0,i):
		print(j)

		
0
0
1
0
1
2
0
1
2
3
>>> for i in range(8):
	for j in range(0,i+1):
		print(j)

		
0
0
1
0
1
2
0
1
2
3
0
1
2
3
4
0
1
2
3
4
5
0
1
2
3
4
5
6
0
1
2
3
4
5
6
7
>>> for i in range(6):
	for j in range(5):
		print(j,end="")

	
012340123401234012340123401234
>>> for i in range(6):
	for j in range(5):
		print(j)
	print("\n")

	
0
1
2
3
4


0
1
2
3
4


0
1
2
3
4


0
1
2
3
4


0
1
2
3
4


0
1
2
3
4


>>> for i in range(6):
	for j in range(5):
		print(j)
	print("")

	
0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

>>> for i in range(6):
	for j in range(5):
		print(j,end="")
		print("")

		
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
>>> for i in range(6):
	for j in range(5):
		print(j,end="")
	print("")

	
01234
01234
01234
01234
01234
01234
>>> for i in range(6):
	for j in range(0,i):
		print(j,end="")
	print("")

	

0
01
012
0123
01234
>>> for i in range(8):
	for j in range(0,i):
		print('*',end="")
	print("\n")

	


*

**

***

****

*****

******

*******

>>> for i in range(67,91):
	for j in range(67,i):
		print(chr(j),end="")
	print("\n")

	


C

CD

CDE

CDEF

CDEFG

CDEFGH

CDEFGHI

CDEFGHIJ

CDEFGHIJK

CDEFGHIJKL

CDEFGHIJKLM

CDEFGHIJKLMN

CDEFGHIJKLMNO

CDEFGHIJKLMNOP

CDEFGHIJKLMNOPQ

CDEFGHIJKLMNOPQR

CDEFGHIJKLMNOPQRS

CDEFGHIJKLMNOPQRST

CDEFGHIJKLMNOPQRSTU

CDEFGHIJKLMNOPQRSTUV

CDEFGHIJKLMNOPQRSTUVW

CDEFGHIJKLMNOPQRSTUVWX

CDEFGHIJKLMNOPQRSTUVWXY

>>> for i in range(65,91):
	for j in range(0,i+1):
		print("*","\n")

		
* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

* 

>>> for i in range(5):
	for j in range(0,i+1):
		print('*')

		
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> for i in range(8):
	for j in range(6):
		print("&",end="")

		
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
>>> num=1
>>> for i in range(5):
	for j in range(0,i):
		print(num)
		num=num+1
	print("\n")

	


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


>>> num=1
>>> for i in range(9):
	for j in range(0,num):
		print("*",end="")
		num=num+1

		
*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
>>> num=65
>>> for i in range(9):
	for j in range(0,i+1):
		print(chr(num),"\n")
		num=num+1

		
A 

B 

C 

D 

E 

F 

G 

H 

I 

J 

K 

L 

M 

N 

O 

P 

Q 

R 

S 

T 

U 

V 

W 

X 

Y 

Z 

[ 

\ 

] 

^ 

_ 

` 

a 

b 

c 

d 

e 

f 

g 

h 

i 

j 

k 

l 

m 

>>> num=1
>>> for i in range(0,3):
	for j in range(0,i):
		print(chr(num),end="")
		num=num+1
	print("")

	



>>> num=65
>>> for i in range(0,7):
	for j in range(0,i):
		print(chr(num),end="")
		num=num+1
	print("")

	

A
BC
DEF
GHIJ
KLMNO
PQRSTU
>>> n=5
>>> k=2*n-2
>>> for i in range(0,5):
	for j in range(0,k):
		print(end="")
		k-=2
		for j in range(0,i+1):
			print("*")
			print("\n")

			
*


*


*


*


*


*


*


*


>>> n=5
>>> k=2*n-2
>>> k
8
>>> for i in range(0,n):
	for j in range(0,k):
		print(end="")
		k-=2
		for j in range(0,i+1):
			print("*",end="")
			print("\n")

			
*

*

*

*

*

*

*

*

>>> 
KeyboardInterrupt
>>> for i in range(0,n):
	
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> n=5
>>> k=2*n-2
>>> for i in range(0,n):
	for j in range(0,k):
		print(end="")
		k-=2
		for j in range(0,i+1):
			print("*",end="")
		print("\n")

		
*

*

*

*

*

*

*

*

>>> num=65
>>> for i in range(0,5):
	for j in range(0,6):
		print(chr(num),end="")
		num=num+1
	print("\n")

	
ABCDEF

GHIJKL

MNOPQR

STUVWX

YZ[\]^

>>> num=45
>>> for i in range(0,8):
	for j in range(0,i+1):
		print(chr(num),end="")
		num=num+1
	print("\n")

	
-

./

012

3456

789:;

<=>?@A

BCDEFGH

IJKLMNOP

>>> n=5
>>> num=65
>>> k=2*n-2
>>> for i in range(0,5):
	for j in range(0,k):
		print(end="")
		k=k-2
		for j in range(0,i+1):
			print('*',end="")
	print("\n")

	
********









>>> n=5
>>> num=65
>>> k=2*n-2
>>> for i in range(0,5):
	for j in range(0,k):
		print(end="")
		k=k-2
		for j in range(0,i+1):
			print("*",end="")
print("\n")
SyntaxError: invalid syntax
>>> 
>>> 
