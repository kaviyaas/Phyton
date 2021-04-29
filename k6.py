Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=platinum
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=platinum
NameError: name 'platinum' is not defined
>>> x="platinum"
>>> len(x)
8
>>> x[::2]
'paiu'
>>> x[:6:2]
'pai'
>>> x[::3]
'ptu'
>>> x[-1]
'm'
>>> x[::-4]
'mt'
>>> x[:7:-2]
''
>>> x[0::-2]
'p'
>>> x[0:7:-2]
''
>>> x="ADC"
>>> X
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    X
NameError: name 'X' is not defined
>>> x
'ADC'
>>> x[::-2]
'CA'
>>> x[::2]
'AC'
>>> x[::2]
'AC'
>>> x="backspace"
>>> len(x)
9
>>> x[2::3]
'cpe'
>>> x[0::-3]
'b'
>>> x[0:8:-3]
''
>>> x="acd"
>>> x[0:2:-1]
''
>>> x[0:2:-2]
''
>>> x[::-2]
'da'
>>> x[0:3:-2]
''
>>> x="string"
>>> type(x)
<class 'str'>
>>> id(x)
2665294642992
>>> x[::3]
'si'
>>> x[::-3]
'gr'
>>> x[::-2]
'git'
>>> x[0:6:-2]
''
>>> x[0:5:-2]
''
>>> x[0:6:2]
'srn'
>>> x[0:6]
'string'
>>> x[0:-3]
'str'
>>> x=20
>>> type(x)
<class 'int'>
>>> id(x)
2665288526736
>>> s=10
>>> id(x)
2665288526736
>>> y=s+x
>>> y
30
>>> id(x)
2665288526736
>>> z=y
>>> z
30
>>> a=[1,2,3,4,6]
>>> len(a)
5
>>> a[0:3]
[1, 2, 3]
>>> a[1:5]
[2, 3, 4, 6]
>>> a[1:5:-2]
[]
>>> a[0:5:-2]
[]
>>> a[::-2]
[6, 3, 1]
>>> a[0:5:2]
[1, 3, 6]
>>> a[::2]
[1, 3, 6]
>>> x[0:4:-2]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x[0:4:-2]
TypeError: 'int' object is not subscriptable
>>> a[0:4:-2]
[]
>>> type(a)
<class 'list'>
>>> id(a)
2665329607232
>>> print(a)
[1, 2, 3, 4, 6]
>>> name=['james','a','b']
>>> name
['james', 'a', 'b']
>>> len(name)
3
>>> name(1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name(1)
TypeError: 'list' object is not callable
>>> id(name)
2665329693440
>>> type(name)
<class 'list'>
>>> n
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> if n>1
SyntaxError: invalid syntax
>>> if n > 1
SyntaxError: invalid syntax
>>> type(name)
<class 'list'>
>>> x="phyton"
>>> x
'phyton'
>>> len(x)
6
>>> x[1]
'h'
>>> x[2]
'y'
>>> X[4]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    X[4]
NameError: name 'X' is not defined
>>> x[3]
't'
>>> x[4]
'o'
>>> x[-4]
'y'
>>> x[0:6]
'phyton'
>>> x[2:4]
'yt'
>>> x[2:-3]
'y'
>>> a=2;
>>> c=23
>>> z=a+c
>>> z
25
>>> z;
25
>>> a=z
>>> a
25
>>> a=c=b
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a=c=b
NameError: name 'b' is not defined
>>> a="debug"
>>> len(a)
5
>>> a[1]
'e'
>>> a[2]
'b'
>>> a[3]
'u'
>>> a[4]
'g'
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> a[-5]
'd'
>>> a[-4]
'e'
>>> importpygame
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    importpygame
NameError: name 'importpygame' is not defined
>>> a.capitalize
<built-in method capitalize of str object at 0x0000026C8F97F8F0>
>>> a[0:5:2]
'dbg'

>>> 
>>> 
>>> 
>>> 
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> 
>>> x="12345
SyntaxError: EOL while scanning string literal
>>> x="12345"
>>> x[0]
'1'
>>> x[1]
'2'
>>> x[3]
'4'
>>> x[2]
'3'
>>> x[:]
'12345'
>>> x[::1]
'12345'
>>> x[::-11]
'5'
>>> x[::-1]
'54321'
>>> x[::-2]
'531'
>>> x[2::-2]
'31'
>>> x[2:5:-2]
''
>>> x[2:4:-2]
''
>>> x[2:3:-2]
''
>>> x[2::-2]
'31'
>>> x[::-2]
'531'
>>> x="technical"
>>> len(x)
9
>>> x[2::-2]
'ct'
>>> 'ct'
'ct'
>>> x[0:9:-2]
''
>>> x[::-2]
'lcnct'
>>> x[0::-2]
't'
>>> x[1::-2]
'e'
>>> 'e'
'e'
>>> i="integer"
>>> len(i)
7
>>> len(i);
7
>>> i[0]
'i'
>>> i[-5]
't'
>>> i[-4]
'e'
>>> i[-3]
'g'
>>> 
>>> 
>>> 
>>> i[-7]
'i'
>>> 
>>> len(i-1)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    len(i-1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> len(i)
7
>>> 