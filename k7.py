Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> z=[1,2,3,4]
>>> z[2::-2]
[3, 1]
>>> s="array"
>>> s="array"
>>> s[::-2]
'yra'
>>> s[0:4:-2]
''
>>> s[0:5:-2]
''
>>> s[::-3]
'yr'
>>> s[::3]
'aa'
>>> s[0::5]
'a'
>>> s[0::3]
'aa'
>>> s[0:-2:-1]
''
>>> s[0::-1]
'a'
>>> 
>>> s[::-1]
'yarra'
>>> s[0::-1]
'a'
>>> s[0::-2]
'a'
>>> s[0:-1]
'arra'
>>> s[1]
'r'
>>> s[2]
'r'
>>> s[3]
'a'
>>> s[4]
'y'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> s[1:5]
'rray'
>>> s[2:4]
'ra'
>>> s[2::-2]
'ra'
>>> s[1::-2]
'r'
>>> s[0::2]
'ary'
>>> s[0::-2]
'a'
>>> type(s)
<class 'str'>
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'array'
>>> id(s)
1641650780080
>>> x="kaviya"
>>> len(x)
6
>>> x[0]
'k'
>>> x[1]
'a'
>>> x[2]
'v'
>>> x[3]
'i'
>>> x[4]
'y'
>>> x[5]
'a'
>>> x[0:5]
'kaviy'
>>> x[0:-6]
''
>>> x[0:-1]
'kaviy'
>>> x[-6:-1]
'kaviy'
>>> x[-1:-6]
''
>>> a="""lorem ipsum dolor sit amet,consecutor adipiscing elit,sed do eisusomed tempor incididunt ut labore et dolore magna aliqua"""
>>> a
'lorem ipsum dolor sit amet,consecutor adipiscing elit,sed do eisusomed tempor incididunt ut labore et dolore magna aliqua'
>>> a="hello ,world"
>>> len(a)
12
>>> a[0]
'h'
>>> a[5]
' '
>>> a[6]
','
>>> x="the best in life are free"
>>> print("free in text")
free in text
>>> if
SyntaxError: invalid syntax
>>> x="hello"
>>> y="world"
>>> z=(x+y)
>>> z
'helloworld'
>>> z=(x*3)
>>> z
'hellohellohello'
>>> x='''hello world the draw items in the work may be rare to the earth,xx yy,:'''
>>> x
'hello world the draw items in the work may be rare to the earth,xx yy,:'
>>> len(x)
71
>>> x[1]
'e'
>>> x[0]
'h'
>>> x[1:71]
'ello world the draw items in the work may be rare to the earth,xx yy,:'
>>> x[0::-2]
'h'
>>> x[::-2]
':y xhreeto rre a rwetn mt adetdrwolh'
>>> x='string operator'
>>> x
'string operator'
>>> y='concodination'
>>> z=x+y
>>> z
'string operatorconcodination'
>>> z*3
'string operatorconcodinationstring operatorconcodinationstring operatorconcodination'
>>> x[-1:-6]
''
>>> x[-6:-1]
'erato'
>>> x[-4:-2]
'at'
>>> x[-2:-1]
'o'
>>> s="zet code"
>>> s[0]
'z'
>>> s[8]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s[8]
IndexError: string index out of range
>>> s[7]
'e'
>>> s[5]
'o'
>>> s[6]
'd'
>>> a='i saw the wolf in the forest'
>>> print(a.find("wolf"))
10
>>> print(a.find("wolf,15))
	     
SyntaxError: EOL while scanning string literal
>>> print(a.find("wolf",15))
-1
>>> print(a.find("wolf",4))
10
>>> print(a.find('forest'))
22
>>> a='i saw the   wolf in the forest'
>>> print(a.find("wolf"))
12
>>> 