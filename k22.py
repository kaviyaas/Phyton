Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x,y,z=10,12,11
>>> if(x>y&y>z):
	print("the condition is true")
elif((z>x)^(x<y)):
	Print("the condition2 is true")
elif((z==x)|(z<y)):
	print("the condition3 is true")

	
the condition3 is true
>>> if(x<y):
	print("hello")
else:
	print("hi")

	
hello
>>> if((x>y)|(z<=x)):
	print("condition1 is true")
elif((x>=y)&(y>z)):
	print("condition2 is true")
elif((x<=y)&(z<y)|(x>y)):
	print("condition3 is true")
else:
	print("all conditions failed")

	
condition3 is true
>>> if((True&False)|(True|False)^(False|False):
   
SyntaxError: invalid syntax
>>> if((True&False)|(True|False)^(False|False)):
	print("true 1")
elif((0&1)|(0&1)|(0^1)):
	print("true 2")
elif((not not not not not False)):
	print("true 3")
elif((x>y)&(y>z)):
	print("true 4")
else:
	print("all the conditions not satisfied")

	
true 1
>>> 
>>> if((True&False)|(True|False)&(False|False):
   
SyntaxError: invalid syntax
>>> if((True&False)|(True|False)&(False|False)):
	print("true 1")
elif((0&1)|(0&1)&(0^1)):
	print("true 2")
elif((not not not not not True)):
	print("true 3")
elif((x>y)&(y>z)):
	print("true 4")
else:
	print("all the conditions not satisfied")
   
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> if((True&False)|(True|False)&(False|False)):
	print("true 1")
elif((0&1)|(0&1)&(0^1)):
	print("true 2")
elif((not not not not not True)):
	print("true 3")
elif((x>y)&(y>z)):
	print("true 4")
else:
	print("all the conditions not satisfied")

   
all the conditions not satisfied
>>> if(True):
	print("hello world")
else:
	print("welcome")

	
hello world
>>> if(True):
	print("hi")

hi
>>> if(False):
	print("happy")
else:
	print("world")

	
world
>>> x=int(input())
53
>>> y=67
>>> x,y
(53, 67)
>>> if((x<y)):
	print("x is less than y")
else:
	print("x is greater than y")

	
x is less than y
>>> x,y,z=10,14,8
>>> if((x&y)|(y&x)):
	print("correct1")
elif((x|y)^(x&y)):
	print("correct 2")
elif((x&y)^(x|y)):
	print("correct 3")
else:
	print("all are wrong")

	
correct1
>>> x=100
>>> if (x>200):
	print("x is greater")
elif(x<90):
	print("x is smaller")
elif(x==100):
	print("x is equals 100")
else:
	print("x is not a tru value")

	
x is equals 100
>>> x is equals 100
SyntaxError: invalid syntax
>>> sum=6
>>> if(sum>0):
	print("positive number")
else:
	print("negative number")

	
positive number
>>> a=6
>>> if(a>=0):
	print("a is a positive number")
else:
	print("a is negative number")

	
a is a positive number
>>> discount=""
>>> sales=60000
>>> if sales>=10000
SyntaxError: invalid syntax
>>> if sales>=10000:
	discount=sales*0.2
	print("dis"=discount)
	
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(discount)

>>> sales=60000
>>> if sales>=10000:
	discount=sales*0.2
	print(discount)
else:
	discount=sales*0.4
	print(discount)

	
12000.0
>>> x,y,z=0
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    x,y,z=0
TypeError: cannot unpack non-iterable int object
>>> x,y,z===0
SyntaxError: invalid syntax
>>> x=y=z=0
>>> x=int(input("enter x:")
    34
      
SyntaxError: invalid syntax
>>> x=int(input("enter x"))
enter x34
>>> y=int(input("enter y"))
enter y45
>>> z=int(input("enter z"))
enter z56
>>> max=""
>>> max=x
>>> if (y>max):
	max=y
         if(z>max):
		 
SyntaxError: unexpected indent
>>> x=int(input("enter x"))
enter x36
>>> y=int(input("enter y"))
enter y57
>>> z=int(input("enter z"))
enter z56
>>> max=""
>>> max=x
>>> if (y>max):
	max=y
elif(z>max):
	max=z
	print("max number is:",max)

	
>>> 
>>> 
>>> a=int(input("enter the number:"))
enter the number:37
>>> if(a//2==0):
	print("the number is even")
else:
	print("the number is odd")

	
the number is odd
>>> sum1=0
>>> sum2=0
>>> num1,num2,num3=1,2,3
>>> sum1=num1+num2+num3
>>> sum1
6
>>> if ((num1 != num2) and (num1 != num3)):
	sum2=sum2+num1
if((num2 !=num3)):
	
SyntaxError: invalid syntax
>>> if ((num1 != num2) and (num1 != num3)):
	sum2=sum2+num1
	if ((num2 !=num3)):
		sum2=sum2+num2
		if ((num3!=num1)):
			sum2=sum2+num3

			
>>> print(sum1,sum2)
6 6
>>> x=44
>>> y=11
>>> if (x//y==0):
	print("x is divided by y")
else:
	print("x is not divided by y")

	
x is not divided by y
>>> 



>>> 
SyntaxError: invalid syntax
>>> remainder=x%y
>>> if(remainder==0):
	print("the number is divided")
else:
	print("the no is not divided")

	
the number is divided
>>> x,y,z=150,56,78
>>> a,b=12,43
>>> divisor=15
>>> r1=""
>>> r1=x%divisor
>>> if (r1==0):
	print("x is divided")
	r1=y%divisor
	if (r1==0):
		print("y is divided")
		r1=z%divisor
		if(r1==0):
			print("z is divided")
			r1=a%divisor
			if(r1==0):
				print("a is divided")
				r1=b%divisor
				if (r1==0):
					print("b is divisor")

					
x is divided
>>> radius=20
>>> if (radius>10):
	area=3.14*radius*radius
	perimeter=2*3.14*radius
	print(area)
	print(perimeter)

	
1256.0
125.60000000000001
>>> print("1.area")
1.area
>>> print("2.perimeter")
2.perimeter
>>> choice=int(input("enter your choice 1 or 2:")
	   if (choice==1):
	   
SyntaxError: invalid syntax
>>> a=2
>>> b=34
>>> op=input("enter the operator[+ * - /]")
enter the operator[+ * - /]+ - * /
>>> result=0
>>> if (op==+):
	
SyntaxError: invalid syntax
>>> if (op== +):
	
SyntaxError: invalid syntax
>>> if(op=='+'):
	result=a+belif (op+)
	
SyntaxError: invalid syntax
>>> if (op=='+'):
	result=a+b
elif (op=='-'):
	result=a-b
elif(op=='*')
SyntaxError: invalid syntax
>>> if (op=='+'):
	result=a+b
elif (op=='-'):
	result=a-b
elif(op=='*'):
	result=a*b
elif(op=='/'):
	result==a/b
else:
	print("the operator is invalid")

	
the operator is invalid
>>> if (op=='+'):
	result=a+b
	print(result)
elif (op=='-'):
	result=a-b
	print(result)
elif(op=='*'):
	result=a*b
	print(result)
elif(op=='/'):
	result==a/b
	print(result)
else:
       print("the operator is invalid")

       
the operator is invalid
>>> a=2
>>> b=34
>>> op=input("enter the operator[+ * - /]")
enter the operator[+ * - /]+ - * /
>>> result=0
SyntaxError: multiple statements found while compiling a single statement
>>> a=2
>>> b=34
>>> op=input('enter the operator')
enter the operator+ = * %
>>> 
KeyboardInterrupt
>>> a=2
>>> b=34
>>> op=input("enter the operator[+ * - /]")
enter the operator[+ * - /]+ - * /
>>> result=0
SyntaxError: multiple statements found while compiling a single statement
>>>  a=2
 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> a=2
>>> b=4
>>> op=input("enter the operator")
enter the operator+ = * %
>>> if (op==+)
SyntaxError: invalid syntax
>>> if(op==+):
	
SyntaxError: invalid syntax
>>> if(op=='+'):
	r=a+b
elif(op=='-'):
	r=a-b
elif(op=='*'):
	r=a*b
elif(op=='%'):
	r=a%b

	
>>> print(r)
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    print(r)
NameError: name 'r' is not defined
>>> a=int(input("enter the num"))
enter the num67
>>> b=int(input("enter the num"))
enter the num23
>>> op=input("enter the operator[+ * - %]")
enter the operator[+ * - %]+
>>> if(op=='+'):
	r=a+b
	print(r)
elif(op=='-'):
	r=a-b
	print(r)
elif(op=='*'):
	r=a*b
	print(r)
else:
	print("not valid")

	
90
>>> x,y,z=1,6,8
>>> min= mid =max=none
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    min= mid =max=none
NameError: name 'none' is not defined
>>> min=mid=max
>>> if((x<y)and(x<z)):
	if(y<z):
	  min=mid=max=x,y,z
	else:
                min=mid=max=x,z,y
  elif((y<x)and(y<z)):
          if(x<z):
