Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import random
>>> val=[1,2,3,4,6]
>>> random.choice(val)
2
>>> a=[34,45,56,78]
>>> random.choice(a)
56
>>> randon.choice(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    randon.choice(a)
NameError: name 'randon' is not defined
>>> random.choice(a)
34
>>> random.choice(a)
45
>>> random.choice(a)
56
>>> random.choice(a)
78
>>> random.choice(a)
78
>>> b=[1,9,7,6]
>>> random.choice(a)
34
>>> random.choice(b)
9
>>> random.choice(b)
7
>>> val=[for i in range(20)]
SyntaxError: invalid syntax
>>> a=[i for i in range(20)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> a=[j for j in range(2,80)]
>>> a
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
>>> c=[i for i in range(0,20)]
>>> c
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> c=[i for i in range(9,78)]
>>> c
[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
>>> import random
>>> a=[1,3,5,6]
>>> random.choice(a)
5
>>> random.choice(c)
15
>>> random.choice(b)
7
>>> random.radint(0,3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    random.radint(0,3)
AttributeError: module 'random' has no attribute 'radint'
>>> random.randint(0,3)
3
>>> random.randint(0,5)
5
>>> random.randint(0,78)
55
>>> random.randint(0,67)
23
>>> a=[i for i in range(56 80)]
SyntaxError: invalid syntax
>>> a=[i for i in range(56,80)]
>>> a
[56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
>>> random.randint(0,5)
0
>>> random.random()
0.8817620148570875
>>> random.random()
0.08788589687493098
>>> random.random()
0.46725032824402446
>>> random.random()
0.5712611928706103
>>> random.random()
0.0654101504167034
>>> random.random()
0.2401815389058607
>>> random.randint(0,3)
2
>>> 12 is 12
True
>>> x=56
>>> y=67
>>> x is not y
True
>>> x is y
False
>>> x="after"
>>> y="after"
>>> type(x)
<class 'str'>
>>> id(x)
2498213696048
>>> id(y)
2498213696048
>>> x is y
True
>>> x="solution"
>>> y="soluton"
>>> x is y
False
>>> x is not y
True
>>> x="i18n solution"
>>> y="i18n solution"
>>> x is y
False
>>> x is not y
True
>>> id(x)
2498245474224
>>> id(y)
2498245472304
>>> from sys import intern
>>> x=intern("i18n solution")
>>> y=intern("i18n solution")
>>> x is y
True
>>> True
True
>>> x is not y
False
>>> from sys import intern:
	
SyntaxError: invalid syntax
>>> import random
>>> a=[2,4,5,7]
>>> random.choice(a)
7
>>> random.choice(a)
4
>>> random.choice(a)
2
>>> random.choice(a)
4
>>> b=[3,67,89,000]
>>> random.choice(b)
67
>>> random.choice(b)
89
>>> random.choice(b)
67
>>> random.choice(b)
3
>>> random.choice(b)
0
>>> a=[i for i in range(0,6)]
>>> a
[0, 1, 2, 3, 4, 5]
>>> b=[i for i in range(0,100)]
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> random.randint(0,3)
2
>>> random.randint(0,6)
5
>>> random.randint(7,40)
13
>>> random.random()
0.16884914400829987
>>> random.random()
0.162080931468767
>>> random.random()
0.9383267035610915
>>> 67 is 67
True
>>> 67 is not 56
True
>>> "row" is "row"
True
>>> "string" is "string"
True
>>> x="backspace"
>>> y="backspace"
>>> x is y
True
>>> x,y="i18n solution"
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    x,y="i18n solution"
ValueError: too many values to unpack (expected 2)
>>> from sys import intern
>>> x="i18n solution"
>>> y=""
>>> x is not y
True
>>> x=intern("i18n solution")
>>> y=intern("i18n solution")
>>> x is y
True
>>> 