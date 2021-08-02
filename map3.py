Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(n):
	return n+n

>>> m=(4,7,8,9)
>>> a=map(add,m)
>>> print(list(a))
[8, 14, 16, 18]
>>> x=[4,5,7,8]
>>> y=[8,9,6,7]
>>> result=map(lambda x,y:x+y,x,y)
>>> print(result)
<map object at 0x000001FDEFDF1160>
>>> result
<map object at 0x000001FDEFDF1160>
>>> return result
SyntaxError: 'return' outside function
>>> print(list(result))
[12, 14, 13, 15]
>>> m=["sun","mon","tue","wed"]
>>> a=map(lambda x:x.replace(o,s),m)
>>> for i in a:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for i in a:
  File "<pyshell#14>", line 1, in <lambda>
    a=map(lambda x:x.replace(o,s),m)
NameError: name 'o' is not defined
>>> m=["sun","mon","tue","wed"]
>>> a=map(lambda x:x.replace(o,s),m)
>>> m=["sun","mon","tue","wed"]
>>> a=map(lambda x:x.replace('o','s'),m)
>>> for i in a:
	print(i)

	
sun
msn
tue
wed
>>> a=[6.77,78,99,6.34,7.888]
>>> mapobj=map(round,a)
>>> print(list(mapobj))
[7, 78, 99, 6, 8]
>>> a=[78.999,67.888,5.6666]
>>> m=map(round(2),a)
>>> print(tuple(m))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(tuple(m))
TypeError: 'int' object is not callable
>>> a=[78.999,67.888,5.6666]
>>> m=map(round(2),a)
>>> print(list(m))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(list(m))
TypeError: 'int' object is not callable
>>> a=[78.999,67.888,5.6666]
>>> m=map(round,a)
>>> print(list(m))
[79, 68, 6]
>>> a=78.999
>>> round(a,2)
79.0
>>> a=[78.999,67.888,5.6666]
>>> m=map(round(a,2),a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    m=map(round(a,2),a)
TypeError: type list doesn't define __round__ method
>>> def display(x):
	x=x.upper()
	print(x)

	
>>> m=map(display,x)
>>> for i in x:
	print(i,end="")

	
4578
>>> display("lambda reduce the codeing")
LAMBDA REDUCE THE CODEING
>>> def display(x):
	x=x.upper()
	print(x)

	
>>> a="lambda reduce the codeing"
>>> m=map(display,a)
>>> for i in m:
	print(i)

	
L
None
A
None
M
None
B
None
D
None
A
None
 
None
R
None
E
None
D
None
U
None
C
None
E
None
 
None
T
None
H
None
E
None
 
None
C
None
O
None
D
None
E
None
I
None
N
None
G
None
>>> def display(x):
	x=x.upper()
	print(x)

	
>>> m=map(display,a)
>>> def display(x):
	x=x.upper()
	print(x)

	
>>> a="lambda reduce the codeing"
>>> m=map(display,a)
>>> for i in m:
	print(i,end="")

	
L
NoneA
NoneM
NoneB
NoneD
NoneA
None 
NoneR
NoneE
NoneD
NoneU
NoneC
NoneE
None 
NoneT
NoneH
NoneE
None 
NoneC
NoneO
NoneD
NoneE
NoneI
NoneN
NoneG
None
>>> 