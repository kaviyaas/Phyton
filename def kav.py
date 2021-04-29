Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> round(4.5)
4
>>> round(4.6)
5
>>> round(45.6)
46
>>> round(45.678,2)
45.68
>>> round(123.567,2)
123.57
>>> a=453.678
>>> round(a,2)
453.68
>>> format(a,'<10f')
'453.678000'
>>> format(a,'<20f')
'453.678000          '
>>> format(a,'>20f')
'          453.678000'
>>> format(a,'^20f')
'     453.678000     '
>>> format(b,'^30f')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    format(b,'^30f')
NameError: name 'b' is not defined
>>> from decimal import Decimal
>>> a=Decimal(23.456)
>>> b=Decimal(456.789)
>>> print(a+b)
480.2449999999999867839051149
>>> print(a-b)
-433.3329999999999877502432355
>>> 