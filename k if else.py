Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=input("enter the value of num:")
enter the value of num:6
>>> if(num>=10):
	if(num>10):
		print("num is greater")
	else:
		print("num is equal")
else:
	print("num is less")

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    if(num>=10):
TypeError: '>=' not supported between instances of 'str' and 'int'
>>>  num=input("enter the value of num:")
 
SyntaxError: unexpected indent
>>> 
>>> num=7
>>> if(num >= 10):
	if(num > 10):
		print("num is greater")
	else:
		print("equal")
else:
	print("num is less")

	
num is less
>>> i=20
>>> if(i<=20):
	print("i is equals to or greater than 20")
	print("i am in if block")
else:
	print("i am in else block")

	
i is equals to or greater than 20
i am in if block
>>> i=20
>>> if(i>=15 ):
	if(i>15):
		print("i is greater than 15")
	else:
		print("i is equals to 15")
else:
	print("i is less than 15")

	
i is greater than 15
>>> var1=100
>>> var2=0
>>> ch=input("enter the choice:")
enter the choice:var1
>>> if(ch==var1):
	print("the expression is true")
elif(ch==var1):
	print("the expression is false")
else:
	print("the expression is not given")

	
the expression is not given
>>> ch
'var1'
>>> if(ch==var1):
	print("the exp is true")
elif(ch==var2):
	print("the exp is false")
else:
	print("the exp is not given")

	
the exp is not given
>>> if(ch=var1):
	
SyntaxError: invalid syntax
>>> if(ch==var1):
	print("the exp is true")
elif(ch==var2):
	print("the exp is false")

	
>>> 
>>> var1,var2=100,0
>>> ch=input("enter the ch:")
enter the ch:var1
>>> if(ch == var1):
	print("true exp")
elif(ch == var2):
	print("false exp")
else:
	print("not given")

	
not given
>>> 
============ RESTART: C:/Users/dhanya/AppData/Local/Programs/Python/Python39/var.py ===========
enter the c value : v1
>>> 
==== RESTART: C:/Users/dhanya/AppData/Local/Programs/Python/Python39/var.py ====
true exp
>>> var1=int(input())
23
>>> var2=int(input())
0
>>> ch==var1
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    ch==var1
NameError: name 'ch' is not defined
>>> ch=""
>>> ch==var1
False
>>> 