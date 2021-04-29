Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def disp1():
	x=input("enter the name")
	y=int(input("enter the age"))
	print(len(x))
	print(x[0])

	
>>> 
>>> disp1()
enter the name"kaviya"
enter the age23
8
"
>>> disp1()
enter the namekaviya
enter the age23
6
k
>>> x[0:5:2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[0:5:2]
NameError: name 'x' is not defined
>>> 
>>> def display():
	x=int(input("enter num"))
	y=input("enter the string"))
	
SyntaxError: unmatched ')'
>>> def display4():
	x=int(input("enter num"))
	y=input("enter the string")
	y[0:6:2]
	print(len(y))
	print(x*x)

	
>>> display4()
enter num45
enter the stringbackspace
9
2025
>>> def display():
	i=int(input("enter the i"))
	while(i<10):
		print(i,end="")
		i++
		
SyntaxError: invalid syntax
>>> def display(i):
	while(i<10):
		print(i,end="")
		i+=1

		
>>> display(0)
0123456789
>>> 
======= RESTART: C:/Users/dhanya/AppData/Local/Programs/Python/Python39/kaviya/for b1.py ======
***

***


***
>>> def triangle(n):
	k=n-1
	for r in range(0,n):
		for c in range(0,k):
			print(end="")
			k=k-1
		for c in range(0,r+1):
			print("*",end="")
		print("\n")

		
>>> triangle(5)
*

**

***

****

*****

>>> def tri1(n):
	s=2*n-2
	for r in range(0,n):
		for c in range(0,s):
			print(end="")
			k=k-2
		for c in range(0,r+1):
			print("*",end="")
		print()

		
>>> tri1(5)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tri1(5)
  File "<pyshell#55>", line 6, in tri1
    k=k-2
UnboundLocalError: local variable 'k' referenced before assignment
>>> def tri1(n):
	k=2*n-2
	for r in range(0,n):
		for c in range(0,k):
			print(end="")
			k=k-2
		for c in range(0,r+1):
			print("*",end="")
		print()

		
>>> tri1(5)
*
**
***
****
*****
>>> def display1(x):
	x=input("enter the character")
	if(chr >= "a" or chr <= "z"):
		print(the input is  lowercase)
		
SyntaxError: invalid syntax
>>> def display(x):
	x=input("enter the chr")
	if(x >= 'a' and x <= 'z'):
		print("the input is lower case")
	elif(x >= 'A' and x <= 'z'):
		print("the input is uppercase")
	elif(x >=0 and x <=9):
		print("the input is number")
	else:
		print("the chr is not entered")

		
>>> display(D)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    display(D)
NameError: name 'D' is not defined
>>> display(x)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    display(x)
NameError: name 'x' is not defined
>>> def display():
	x=input("enter the chr")
	if(x >= 'a' and x <= 'z'):
		print("the input is lower case")
	elif(x >= 'A' and x <= 'z'):
		print("the input is uppercase")
	elif(x >=0 and x <=9):
		print("the input is number")
	else:
		print("the chr is not entered")






		
		
		
		
		
	elif(x >= 'A' and x <= 'z'):
		