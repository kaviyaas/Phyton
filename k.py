Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=23
>>> type(x)
<class 'int'>
>>> x="kaviya"
>>> x="kavi"
>>> x
'kavi'
>>> id(x)
2171448973104
>>> x=23
>>> id(x)
2171405954032
>>> y=x
>>> y
23
>>> id(y)
2171405954032
>>> type(y)
<class 'int'>
>>> z=x+y
>>> z
46
>>> id(y)
2171405954032
>>> z=x-y
>>> z
0
>>> id(z)
2171405953296
>>> z=3
>>> z="kav"
>>> type(z)
<class 'str'>
>>> id(z)
2171448931184
>>> z=x*y
>>> z
529
>>> type(z)
<class 'int'>
>>> id(z)
2171448097936
>>> s=id(y)
>>> s
2171405954032
>>> id(z)
2171448097936
>>> s=type(z)
>>> s
<class 'int'>
>>> s=a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s=a
NameError: name 'a' is not defined
>>> s=x
>>> s
23
>>> id(s)
2171405954032
>>> 2171405954032
2171405954032
>>> s="a"
>>> id(s)
2171408682736
>>> type(s)
<class 'str'>
>>> 