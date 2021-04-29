Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="information"
>>> len(x)
11
>>> x[-12]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[-12]
IndexError: string index out of range
>>> x[-11]
'i'
>>> x[-9]
'f'
>>> x[-8]
'o'
>>> x[::]
'information'
>>> x[::2]
'ifrain'
>>> x[::-2]
'niarfi'
>>> x[0:9:-2]
''
>>> 