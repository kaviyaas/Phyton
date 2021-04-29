Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=34
>>> type(x)
<class 'int'>
>>> x=56.8
>>> type(x)
<class 'float'>
>>> a='just follow the healthy step'
>>> a
'just follow the healthy step'
>>> c="hello world "
>>> b="""just follow your own steps
live your life
as it is"""
>>> b
'just follow your own steps\nlive your life\nas it is'
>>> print(a)
just follow the healthy step
>>> print(b,c)
just follow your own steps
live your life
as it is hello world 
>>> x,y=20
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x,y=20
TypeError: cannot unpack non-iterable int object
>>> x,y=20,10
>>> x
20
>>> y
10
>>> x,y
(20, 10)
>>> a.b,c,d=23,43,45,56
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.b,c,d=23,43,45,56
ValueError: too many values to unpack (expected 3)
>>> a,b,c=23,45,56
>>> a
23
>>> b
45
>>> c
56
>>> x=10
>>> y=7
>>> temp=""
>>> temp=x
>>> x=y
>>> y=temp
>>> x
7
>>> y
10
>>> x=0
>>> y=7
>>> temp=''
>>> temp=x
>>> x=y
>>> y=temp
>>> x'y
SyntaxError: EOL while scanning string literal
>>> x,y
(7, 0)
>>> f
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> "f"
'f'
>>> input()
23
'23'
>>> x=input()
45
>>> x
'45'
>>> type(x)
<class 'str'>
>>> x=input()
my name is
>>> x
'my name is'
>>> type(x)
<class 'str'>
>>> x=input(23)
23
>>> y=input(23)
23
>>> x+y
''
>>> x=input()
23
>>> y=input()
34
>>> type(x)
<class 'str'>
>>> x+y
'2334'
>>> type(input())
"this is kaviya"
<class 'str'>
>>> type(input("enter your name"))
enter your name
<class 'str'>
>>> id(input())

1900667094640
>>> x=(input("enter the name:"))
enter the name:kaviya
>>> y=(input("enter the course:"))
enter the course:eee
>>> x+y
'kaviyaeee'
>>> x=int(input("enter your id:"))
enter your id:43
>>> y=int(input("enter your age:"))
enter your age:23
>>> x+y
66
>>> x=float(input("enter your id:"))
enter your id:45.6
>>> x=int(input("enter the number:"))
enter the number:45.7
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    x=int(input("enter the number:"))
ValueError: invalid literal for int() with base 10: '45.7'
>>> x,y,z=10,40,35
>>> x
10
>>> y
40
>>> z
35
>>> x,y=10
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x,y=10
TypeError: cannot unpack non-iterable int object
>>> a,b,c=1,3.4,5
>>> a,b,c
(1, 3.4, 5)
>>> x="""the float value are
used in the phyton
to read the value"""
>>> x
'the float value are\nused in the phyton\nto read the value'
>>> print(x)
the float value are
used in the phyton
to read the value
>>> x="the float value are taken"
>>> x
'the float value are taken'
>>> x="the float value are taken'
SyntaxError: EOL while scanning string literal
>>> x=23
>>> y=12
>>> temp=""
>>> temp=x
>>> x=y
>>> y=temp
>>> x.y
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    x.y
AttributeError: 'int' object has no attribute 'y'
>>> x,y
(12, 23)
>>> x=input()
my age
>>> x
'my age'
>>> x=input()
34
>>> x
'34'
>>> y=input()
45
>>> y
'45'
>>> x+y
'3445'
>>> y=input("the problem is")
the problem is nothing
>>> y
' nothing'
>>> b=input("the age is")
the age is 45
>>> c=int(input())
45
>>> c
45
>>> d=float(input())
67.8
>>> d
67.8
>>> c+d
112.8
>>> b=int(input(the age is))
SyntaxError: invalid syntax
>>> b
' 45'
>>> b=int(input("the age is"))
the age is45
>>> b
45
>>> b=float(input("the number1 :"))
the number1 :23.5
>>> b
23.5
>>>x,y=13,7
>>>x,y=y,x
>>>x
>>>7
>>>
















