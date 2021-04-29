Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> True&True|False^False|True|True
True
>>> (True&True)|(False^False)|(True|True)
True
>>> (True|True)|(False^True)|True
True
>>>  (False^False)|(True^True)
 
SyntaxError: unexpected indent
>>> (False^False)|(True^True)
False
>>> (True|True)^(False|True)|True
True
>>> (True|True)^(False|False)^True
False
>>> (True|False)|(True&False)^False
True
>>> (0&1)|(0|1)&(1|1)
1
>>> (0^1)&(0^1)|(0&1)|(1^0)
1
>>> (0&0)|(1&0)|1
1
>>> o1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    o1
NameError: name 'o1' is not defined
>>> 
>>> 