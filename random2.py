Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> a=[1,2,3,4]
>>> random.choice(a)
1
>>> random.choice(a)
4
>>> random.choice(a)
4
>>> a=[i for i in range(0,100)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> random.choice(a)
28
>>> b=[i for i in range(0,6)]
>>> b
[0, 1, 2, 3, 4, 5]
>>> random.choice(b)
2
>>> 
>>> random.choice(a)
38
>>> random.randint(0,6)
5
>>> random.randint(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    random.randint(a)
TypeError: randint() missing 1 required positional argument: 'b'

>>> random.randint(a,b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    random.randint(a,b)
  File "C:\Users\dhanya\AppData\Local\Programs\Python\Python39\lib\random.py", line 339, in randint
    return self.randrange(a, b+1)
TypeError: can only concatenate list (not "int") to list
>>> random.randint(1,9)
2
>>> random.random()
0.7240988469957264
>>> random.random()
0.30271953112388716
>>> random.randint(0,5)
2
>>> from sys import intern
>>> a=intern("i18n solution")
>>> b=intern("i187n solution")
>>> id(x)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    id(x)
NameError: name 'x' is not defined
>>> id(a)
1804191781616
>>> id(b)
1804191714544
>>> x=[1,2,3]
>>> y=[4,5,6]
>>> x is y
False
>>> x is not y
True
>>> x="lap"
>>> y="sap"
>>> x is y
False
>>> x is not y
True
>>> a='string'
>>> b='straight'
>>> a is b
False
>>> a is not b
True
>>> a=['a','b','c']
>>> b=['a','c','b']
>>> a is b
False
>>> id(a)
1804190605248
>>> id(b)
1804189867840
>>> a=intern['g','h']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a=intern['g','h']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a=['a','b']
>>> b=['a','b']
>>> a is b
False
>>> from sys import intern
>>> a=intern(['a','b'])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a=intern(['a','b'])
TypeError: intern() argument must be str, not list
>>> import random
>>> a=[i for in range(0,45)]
SyntaxError: invalid syntax
>>> a=[i for i in range(0,45)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
>>> random.randint(0,3)
0
>>> random.choice(a)
42
>>> random.choice(a)
19
>>> random.choice(a)
23
>>> random.randint(0,7)
1
>>> random.randint(0,8)
7
>>> random.random()
0.9650685693715801
>>> random.random()
0.24998338491507477
>>> random.random()
0.5086573156797111
>>> random.randint()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    random.randint()
TypeError: randint() missing 2 required positional arguments: 'a' and 'b'
>>> random.randint(0,6)
0
>>> random.randint(0,7)
6
>>> random.randint(5,10)
6
>>> random.choice(a)
36
>>> from sys import intern
>>> a=[1,2,4]
>>> b=[1,2,4]
>>> a is b
False
>>> a is not b
True
>>> id(a)
1804151426880
>>> id(b)
1804191414976
>>> num=[1,2,3]
>>> list(filter(lambda x:y,x+y ,num))
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    list(filter(lambda x:y,x+y ,num))
TypeError: filter expected 2 arguments, got 3
>>> num=[1,2,3]
>>> list(filter(lambda x:x%2==0,num ))
[2]
>>> list(filter(lambda x:y X+y,[1,5,6]))
SyntaxError: invalid syntax
>>> list(filter(lambda x:y,x+y,[1,2,3,4]))
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list(filter(lambda x:y,x+y,[1,2,3,4]))
TypeError: filter expected 2 arguments, got 3
>>> list(filter(lambda(x:x+x,[1,2,3])))
SyntaxError: invalid syntax
>>> list(filter(lambda x:x+x,[1,2,3]))
[1, 2, 3]
>>> list(filter(lambda x:x*x [1,2,3]))
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(filter(lambda x:x*x [1,2,3]))
TypeError: filter expected 2 arguments, got 1
>>> list(filter(lambda x:x*x,[1,2,3]))
[1, 2, 3]
>>> 