Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0 and 1
0
>>> 0 and 0
0
>>> 1 and 0
0
>>> 1 and 1
1
>>> 1 or 1
1
>>> 1 or 0
1
>>> 0 or 1
1
>>> 1^0
1
>>> 0^0
0
>>> 0^1
1
>>> 0^0
0
>>> 
>>> not True False
SyntaxError: invalid syntax
>>> not True&False
True
>>> True and False and False or True
True
>>> True and False or False
False
>>> False^True and True or False
True
>>> 0&1|0|1&1|1
1
>>> 0&1|1&1|1&0&1
1
>>> 0|1|0
1
>>> 0&0|1&0|1
1
>>> 0^1|1&0|0&1|1^0
1
>>> 0^1&0^1|0&1|1^0
1
>>> True&False|False^True|True^False
True
>>> True^True|False^False|True|True
True
>>> True|True^False^False|True
True
>>> True&True|False&False|True
True
>>> x,y=10,12
>>> x,y=y,x
>>> 
>>> print x,y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x,y)?
>>> print(x,y)
12 10
>>> True^False|True&False|True
True
>>> True|False^True|True|True
True
>>> 1&1|0&1|1&0&
SyntaxError: invalid syntax
>>> 1&1|1^0&1
1
>>> not 0&1|0|0^0
True
>>> True&False|True&True
True
>>> False|False&True|True&True|True
True
>>> True|True^True
True
>>> True & True |True^False
True
>>> True|False&True^False
True
>>> True|False|True|True
True
>>> True&True|False^False
True
>>> True|True|True^False
True
>>> True&True^True|False
False
>>> True|False^True|True|True
True
>>> True|True^True|True
True
>>> True&True|True|False|False
True
>>> 0&1|1&0|1&1
1
>>> 
>>> 1&0|0&1
0
>>> 0&1|1&0&1|1
1
>>> 0&1|1&0|1&1
1
>>> 1&0|1&1|1^0
1
>>> True|False^False|True^True|False
True
>>> True|False^False^True|True&False
True
>>> True|False^True|False|False
True
>>> True|True&False|True^True|True&False
True
>>> True^True& False^True|True^True|True
True
>>> True&True|False^False|True|True
True
>>> True^True&False
True
>>> True^True&False^True|True^True|False
False
>>> False|True&False
False
>>> True|True&False
True
>>> False&False
False
>>> True|True&True^True|True^True|True^True
True
>>> False^False|False&False^False|True
True
>>>  True|False^True
 
SyntaxError: unexpected indent
>>> True|True^True
True
>>> True|True&False|False^True
True
>>> True^True|False^False|False^True|True&False^True
True
>>> False^True|True|True&False
True
>>> True&True|False
True
>>> True|True^False
True
>>> True&True|False^False|True|True
True
>>> True|True|False^True|True
True
>>> True^True|True^True|True
True
>>> True^False|True^True
True
>>> True|True
True
>>> False^False|True^True
False
>>> True|True^False|True|True
True
>>> True|True^False|False^True
True

>>(True|False)|(False&False)^True

