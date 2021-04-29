Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print("name of the person:%s"%self.a)
		print("age of the person:%d"%self.b)

		
>>> s=sample("xyz",56)
>>> s.display()
name of the person:xyz
age of the person:56
>>> class person():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(f"name of the person={self.name}")
		print(f"age of the person={self.age}")

		
>>> p=person("abc",6)
>>> p.display()
name of the person=abc
age of the person=6
>>> class dog:
	def __init__(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		print("Rodger details:",self.breed)
		print(self.color)

		
>>> d=dog(bulldog,black)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d=dog(bulldog,black)
NameError: name 'bulldog' is not defined
>>> d=dog("bulldog","black")
>>> d.display()
Rodger details: bulldog
black
>>> class myclass():
	def __init__(self,x,y,*vartubule):
		self.x=x
		self.y=y
	def display(self):
		print(x+y)

		
>>> m=myclass(1,2,3,4)
>>> m=myclass([1,2,3,4][2,3,4])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    m=myclass([1,2,3,4][2,3,4])
TypeError: list indices must be integers or slices, not tuple
>>> class myclass():
	def __init__(self,x,*vartubule):
		self.x=x
	def display(self):
		return(x+x)

	
>>> m=myclass(1,2,3)
>>> m.display()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    m.display()
  File "<pyshell#41>", line 5, in display
    return(x+x)
NameError: name 'x' is not defined
>>> 
================================ RESTART: F:/kaviya/class 5.py ================================
Traceback (most recent call last):
  File "F:/kaviya/class 5.py", line 8, in <module>
    m.display()
  File "F:/kaviya/class 5.py", line 5, in display
    return (self.x+self.y)
AttributeError: 'myclass' object has no attribute 'y'
>>> 
================================ RESTART: F:/kaviya/class 5.py ================================
>>> 
================================ RESTART: F:/kaviya/class 5.py ================================
2
>>> class data():
	pass

>>> import array
>>> class data():
	s1=array.array('i',[1,2,4])
	s2=array.array('i',[4,5,6])
	def __init__(self,s1,s2):
		self.s1=s1
		self.s2=s2
	def display(self):
		print(self.s1+self.s2)

		
>>> d=data([1,2,4],[2,3,4])
>>> d.display()
[1, 2, 4, 2, 3, 4]
>>> import array
>>> class data():
	def __init__(self,s1,s2):
		self.s1=s1
		self.s2=s2
	def display(self):
		print(self.s1+self.s2)

		
>>> d=data([1,3,8],[3,5,6])
>>> d.display()
[1, 3, 8, 3, 5, 6]
>>> class data():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(len(self.a))
		print(self.a[0]+self.b[0])
		print(self.a[1]+self.b[1])
		print(self.a[2]+self.b[2])

		
>>> d=data([1,2,3],[2,3,4])
>>> d.display()
3
3
5
7
>>> class data();
SyntaxError: invalid syntax
>>> class data():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(len(self.a))
		print(len(self.b))
		for i in range(0,4):
			result=self.a[i]+self.b[i]
			print(result)

			
>>> d=data([1,2,3,5],[3,5,6,7])
>>> d.display()
4
4
4
7
9
12
>>> class data():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		pass

	
>>> for i in range(0,9):
	for j in range(0,3):
		print(j)

		
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
0
1
2
>>> for i in range(0,9):
	for j in range(0,3):
		print(i)

		
0
0
0
1
1
1
2
2
2
3
3
3
4
4
4
5
5
5
6
6
6
7
7
7
8
8
8
>>> 
>>> for i in range(0,9):
	for j in range(0,3):
		print(i)
	print(j)

	
0
0
0
2
1
1
1
2
2
2
2
2
3
3
3
2
4
4
4
2
5
5
5
2
6
6
6
2
7
7
7
2
8
8
8
2
>>> class data():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		for i in range(0,5):
			result=self.a[i]*self.b[i]
			print(result)

			
>>> d=data([1,2,3],[2,3,4])
>>> d.display()
2
6
12
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    d.display()
  File "<pyshell#121>", line 7, in display
    result=self.a[i]*self.b[i]
IndexError: list index out of range
>>> class sample():
	def __init__(self,i,j):
		self.i=i
		self.j=j
	def display(self):
		for self.i in range(0,self.i):
			for self.j in range(0,self.j):
				print(self.i)
			print(self.j)

			
>>> s=sample(10,4)
>>> s.display()
0
0
0
0
3
1
1
1
2
2
2
1
3
0
0
0
0
0
0
0
>>> class sample():
	def __init__(self,i,j):
		self.i=i
		self.j=j
	def display(self):
		for self.i in range(0,self.i):
			for self.j in range(0,self.j):
				print(self.j)
		print(self.i)

		
>>> s=sample(10,4)
>>> s.display()
0
1
2
3
0
1
2
0
1
0
9
>>> class sample():
	def __init__(self,r,c):
		self.r=r
		self.c=c
	def display(self):
		for r in range(0,self.r):
			for c in range(0,self.c):
				if(c==0 |c==6 | r>=0)&(r==0 & r==6 & c>0 & c<6):
					print("*",end="")
				else:
					print(end="")
			print('/n')

			
>>> s=sample(7,7)
>>> s.display()
/n
/n
/n
/n
/n
/n
/n
>>> class sample():
	def __init__(self,r,c):
		self.r=r
		self.c=c
	def display(self):
		for r in range(0,self.r):
			for c in range(0,self.c):
				if(c==0 |c==6 | r>=0)&(r==0 & r==6 & c>0 & c<6):
					print("*",end="")
				else:
					print(end="")
			print()

			
>>> s=sample(7,7)
>>> s.display()







>>> class sample():
	def __init__(self,r,c):
		self.r=r
		self.c=c
	def display(self):
		for r in range(0,self.r):
			for c in range(0,self.c):
				if(c==0 |c==6 | r>=0)|(r==0 & r==6 & c>0 & c<6):
					print("*",end="")
				else:
					print(end="")
			print()

			
>>> s=sample(7,7)
>>> s.display()
*

*

*

*
>>> class sample():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		for i in range(self.x,self.y):
			print(self.x,self.y)

			
>>> 
>>> s=sample(2,9)
>>> s.display()
2 9
2 9
2 9
2 9
2 9
2 9
2 9
>>> class myclass():
	def __init__(self,a,x):
		self.a=a
		self.x=x
	def display(self):
		self.a=[i for i in range(0,self.x)]
		print(self.a)

	
>>> 
>>> m=myclass(0,9)
>>> m.display()
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> import random
>>> class myclass():
	def __init__(self,a):
		self.a=a
	def display(self):
		self.a=[i for i in range(0,self.a)]
		print(self.a)