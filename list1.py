Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2)
>>> type(a)
<class 'tuple'>
>>> id(a)
2307929849216
>>> a[0]
1
>>> a(1,3,4,5,7,8,9)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a(1,3,4,5,7,8,9)
TypeError: 'tuple' object is not callable
>>> a=(1,2,3,4,5,8)
>>> id(a)
2307929892512
>>> type(a)
<class 'tuple'>
>>> a[0]=100
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[0]=100
TypeError: 'tuple' object does not support item assignment
>>> a=(1,2,4,5,6,7,8,9)
>>> a[1]
2
>>> a[1]+a[2]
6
>>> a=(1,k,2,&)
SyntaxError: invalid syntax
>>> a=(&,%)
SyntaxError: invalid syntax
>>> a=(2,7,8,9,e,u,y)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a=(2,7,8,9,e,u,y)
NameError: name 'e' is not defined
>>> a=(2,3,4,"d","&")
>>> a
(2, 3, 4, 'd', '&')
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> a.count(2)
1
>>> a.count(&)
SyntaxError: invalid syntax
>>> a.count('&')
1
>>> a.index(1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.index(1)
ValueError: tuple.index(x): x not in tuple
>>> a.index[1]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.index[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.index(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.index(1)
ValueError: tuple.index(x): x not in tuple
>>> x.index(2)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x.index(2)
NameError: name 'x' is not defined
>>> a.index(2)
0
>>> a.count(2)
1
>>> a.index('&')
4
>>> a=[i for i in range(30)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> a.count(20)
1
>>> a.index(2)
2
>>> a=[1,5,7,'h','e','y','u']
>>> type(a)
<class 'list'>
>>> id(a)
2307930691456
>>> a[3]='p'
>>> a
[1, 5, 7, 'p', 'e', 'y', 'u']
>>> a[4]='6'
>>> a
[1, 5, 7, 'p', '6', 'y', 'u']
>>> a=(i for i in range(30))
>>> a
<generator object <genexpr> at 0x000002195B6447B0>
>>> a
<generator object <genexpr> at 0x000002195B6447B0>
>>> a=[i for i in range(15)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> a.index(1)
1
>>> a.index(2)
2
>>> a=[1,6,7,8,9,10]
>>> a.index(6)
1
>>> a.index(9)
4
>>> a.index(10)
5
>>> a.index(8)
3
>>> a.count(2)
0
>>> a.count(3)
0
>>> a.count(9)
1
>>> a.append(23)
>>> a
[1, 6, 7, 8, 9, 10, 23]
>>> a.append(23)
>>> a.count(23)
2
>>> a.index(23)
6
>>> a.index(6,23)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.index(6,23)
ValueError: 6 is not in list
>>> a.index(23,6)
6
>>> a
[1, 6, 7, 8, 9, 10, 23, 23]
>>> a.index(23,6)
6
>>> len(a)
8
>>> a.index(23,7)
7
>>> a.append(34)
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34]
>>> b=a.copy()
>>> b
[1, 6, 7, 8, 9, 10, 23, 23, 34]
>>> b.clear()
>>> b.clear()
>>> b
[]
>>> b=[1,2,3,4]
>>> a.extend(b)
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4]
>>> a.append(21)
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4, 21]
>>> c=(11,22,33)
>>> a.extend(c)
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4, 21, 11, 22, 33]
>>> a.pop(-2)
22
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4, 21, 11, 33]
>>> a.pop(-3)
21
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4, 11, 33]
>>> a.append(22)
>>> a
[1, 6, 7, 8, 9, 10, 23, 23, 34, 1, 2, 3, 4, 11, 33, 22]
>>> a.remove(10)
>>> a
[1, 6, 7, 8, 9, 23, 23, 34, 1, 2, 3, 4, 11, 33, 22]
>>> a.count(23)
2
>>> a.remove(23)
>>> a
[1, 6, 7, 8, 9, 23, 34, 1, 2, 3, 4, 11, 33, 22]
>>> a.remove(23)
>>> a
[1, 6, 7, 8, 9, 34, 1, 2, 3, 4, 11, 33, 22]
>>> a.reverse()
>>> a
[22, 33, 11, 4, 3, 2, 1, 34, 9, 8, 7, 6, 1]
>>> a.sort()
>>> a
[1, 1, 2, 3, 4, 6, 7, 8, 9, 11, 22, 33, 34]
>>> a.sort()
>>> a
[1, 1, 2, 3, 4, 6, 7, 8, 9, 11, 22, 33, 34]
>>> a=(1,2,3,4)
>>> a.index(1)
0
>>> a.index(2)
1
>>> a.count(3)
1
>>> a=[1]
>>> id(a)
2307925193280
>>> tyoe(a)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    tyoe(a)
NameError: name 'tyoe' is not defined
>>> type(a)
<class 'list'>
>>> a=(1)
>>> type(a)
<class 'int'>
>>> l=list("kaviya")
>>> l
['k', 'a', 'v', 'i', 'y', 'a']
>>> l=list("apple","steps")
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    l=list("apple","steps")
TypeError: list expected at most 1 argument, got 2
>>> l=list(2,3,4)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    l=list(2,3,4)
TypeError: list expected at most 1 argument, got 3
>>> l=list(1)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    l=list(1)
TypeError: 'int' object is not iterable
>>> l=list(input("enter the value"))
enter the value3
>>> l
['3']
>>> l=list(input("enter the value"))
enter the value"kaviya"
>>> l
['"', 'k', 'a', 'v', 'i', 'y', 'a', '"']
>>> l=list(input("enter the value"))
enter the valuekaviya
>>> l
['k', 'a', 'v', 'i', 'y', 'a']
>>> a=[i for i in range(5)]
>>> a
[0, 1, 2, 3, 4]
>>> a.insert(0,5)
>>> A
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
[5, 0, 1, 2, 3, 4]
>>> a.insert(1,23)
>>> a
[5, 23, 0, 1, 2, 3, 4]
>>> a.append(340)
>>> a
[5, 23, 0, 1, 2, 3, 4, 340]
>>> a.pop(-5)
1
>>> a.sort()
>>> a
[0, 2, 3, 4, 5, 23, 340]
>>> a.clear()
>>> a
[]
>>> l=list()
>>> l
[]
>>> b=[1,2,3]
>>> a=[i for i in range(20)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> a.extend(b)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3]
>>> a.index(2)
2
>>> a.pop(-7)
16
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 1, 2, 3]
>>> a.pop(-6)
17
>>> a.count(1)
2
>>> a.remove(1)
>>> a
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 1, 2, 3]
>>> a.remove(1)
>>> a
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 2, 3]
>>> a.count(1)
0
>>> class sample():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(self.a.append(self.b))

		
>>> a=sample(2,3,4)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    a=sample(2,3,4)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> class sample():
	def __init__(self,a):
		self.a=a
	def getdata(self,b):	
		self.b=b
	def display(self):
		print(self.a.append(self.b))

		
>>> s=sample[2,3,4,6]
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    s=sample[2,3,4,6]
TypeError: 'type' object is not subscriptable
>>> class sample():
	def __init__(self,a=[]):
		self.a=a
	def getdata(self,b):
		self.b=b
	def display(self):
		print(self.a.append(self.b))

		
>>> s=sample([1,4,5,6])
>>> s.getdata(4)
>>> s.display()
None
>>> class sample():
	def __init__(self,a=[]):
		self.a[]=a[]
	def getdata(self,b):
		self.b=b
	def display(self):
		print(self.a[].append(self.b))
		
SyntaxError: invalid syntax
>>> class sample():
	a=[1,2,4,5]
	print(a.append(3))

	
None
>>> class sample():
	a=[1,2,4,5]
	print(type(a))

	
<class 'list'>
>>> class sample():
	a=[5,6,7,8]
	print(a.append(23))
	print(a.insert(0,6))

	
None
None
>>> a=[1,2,3,4]
>>> a=[56,78,43,89]
>>> a.index(78)
1
>>> a.index(0)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    a.index(0)
ValueError: 0 is not in list
>>> a.count(43)
1
>>> a.append(110)
>>> a
[56, 78, 43, 89, 110]
>>> a.pop(-1)
110
>>> a.pop(-2)
43
>>> a.sort()
>>> a
[56, 78, 89]
>>> a.sort()
>>> a
[56, 78, 89]
>>> a.sort(*)
SyntaxError: invalid syntax
>>> a.sort(reverse)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a.sort(reverse)
NameError: name 'reverse' is not defined
>>> a.sort(reverse=False)
>>> a
[56, 78, 89]
>>> a.sort(key=none)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a.sort(key=none)
NameError: name 'none' is not defined
>>> a.sort(Key=None)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    a.sort(Key=None)
TypeError: 'Key' is an invalid keyword argument for sort()
>>> a.sort(None)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    a.sort(None)
TypeError: sort() takes no positional arguments
>>> a=[i for i in range(20)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> a.append(33)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 33]
>>> a.pop(-4)
17
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 33]
>>> a.reverse()
>>> a
[33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a.insert(34,-1)
>>> a
[33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
>>> a.insert(23,21)
>>> a
[33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 21]
>>> a.insert(0,23)
>>> a
[23, 33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 21]
>>> a.insert(1,55)
>>> a
[23, 55, 33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 21]
>>> b=[2,3,4]
>>> a.extend(23)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    a.extend(23)
TypeError: 'int' object is not iterable
>>> a.extend(b)
>>> a
[23, 55, 33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 21, 2, 3, 4]
>>> a.count(3)
2
>>> b.clear()
>>> b
[]
>>> a.clear(19)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    a.clear(19)
TypeError: list.clear() takes no arguments (1 given)
>>> b=a.copy()
>>> b
[23, 55, 33, 19, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 21, 2, 3, 4]
>>> 