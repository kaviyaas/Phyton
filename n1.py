Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sum=6
>>> if sum>=0:
	if sum==0
	
SyntaxError: invalid syntax
>>> sum=8
>>> if sum>=0:
	if sum==0:
		print("zero")
	else:
		print("positive number")
else:
	print("negative number")

	
positive number
>>> num=-3
>>> if num>0:
	print("positive")
elif num==0:
	print("zero")
else:
	print("negative")

	
negative
>>> a=30
>>> if a==50:
	print("the value of a is 50")
elif a==60:
	print("the value of a is 60")
elif a==30:
	print("the value of a is 30")
else:
	print("the value is not equal")

	
the value of a is 30
>>> 
>>> 
>>> 0&1|0&1|1&1&0
0
>>> 0|1&1^1^0
0
>>> num=3
>>> while num>10:
	print(num)
	num=num+1

	
>>> 
>>> num=3
>>> while num<10
SyntaxError: invalid syntax
>>> num=6
>>> while num<10:
	num=num+1
	print(num)

	
7
8
9
10
>>> num=1
>>> i=3
>>> while num==10;
SyntaxError: invalid syntax
>>> while num==10:
	num=num+i
	print(num)

	
>>> 
>>> 
>>> num==23
False
>>> num<i
True
>>> num>i
False
>>> num!=i
True
>>> 
>>> num=[1,2,3]
>>> sq=0
>>> for val in num:
	sq =val*val
	print(sq)

	
1
4
9
>>> num=0
>>> for val in range(0,8,2)
SyntaxError: invalid syntax
>>> for val in range(0,8,2):
	num=num+val
	print(num)

	
0
2
6
12
>>> 
>>> if num=1
SyntaxError: invalid syntax
>>> num=int(input("enter the number"))
enter the number4
>>> if num/2==0:
	print("even")
else:
	print("odd")

	
odd
>>> x,y=10,13
>>> x
10
>>> y
13
>>> x+=2
>>> x
12
>>> x="the given number is"
>>> x
'the given number is'
>>> x=input()
45
>>> x
'45'
>>> y=input()
56
>>> y
'56'
>>> x<y
True
>>> x>y
False
>>> x+y
'4556'
>>> x==y
False
>>> 0&1|1&0|0&1
0
>>> 0&1|1&0|1&1|0&1|0
1
>>> x=float(input("enter the number:"))
enter the number:34.7
>>> y=int(input("the number is:"))
the number is:45
>>> x+y
79.7
>>> x,y=0,1
>>> if (x&y|y&x^x)
SyntaxError: invalid syntax
>>> if (x&y|y&x^x==0):
	print("done")
else:
	print("not done")

	
done
>>> x="""the value is given to some other variable
for future references"""
>>> x
'the value is given to some other variable\nfor future references'
>>> print(x)
the value is given to some other variable
for future references
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> x=56
>>> w