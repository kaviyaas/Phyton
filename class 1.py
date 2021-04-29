Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample():
	def getdata():
		print("hi")

		
>>> s=sample()
>>> s.getdata()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.getdata()
TypeError: getdata() takes 0 positional arguments but 1 was given
>>> class sample():
	def getdata(self):
		print("hi")

		
>>> s=sample()
>>> s.getdata()
hi
>>> s1=sample()
>>> s1.getdata()
hi
>>> 
>>> class sign():
	def getdata(self):
		print("hello")

		
>>> s=sign()
>>> s.getdata()
hello
>>> s1=sign()
>>> s1.getdata()
hello
>>> s5=sign()
>>> s5.getdata()
hello
>>> s.getdata()
hello
>>> s5.getdata()
hello
>>> class sample():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x+self.y)

		
>>> s=sample()
>>> s.getdata(4,5)
>>> s.display()
9
>>> class data():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x-self.y)

		
>>> d=data()
>>> d.getdata(23,56)
>>> d.display()
-33
>>> class sample():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display():
		print(self.x+self.y)

		
>>> s=sample()
>>> s.getdata(89,67)
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s.display()
TypeError: display() takes 0 positional arguments but 1 was given
>>> class sample():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x+self.y)

		
>>> s=sample()
>>> s.getdata(self,x,y):
	
SyntaxError: invalid syntax
>>> s1=sample()
>>> s1.getdata(110,56)
>>> s1.display()
166
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.display()
  File "<pyshell#63>", line 6, in display
    print(self.x+self.y)
AttributeError: 'sample' object has no attribute 'x'
>>> s=sample()
>>> s.getdata(23,78)
>>> s.display()
101
>>> s1.display()
166
>>> class student():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x%self.y)

		
>>> s=student()
>>> s.getdata(23,4)
>>> s.display()
3
>>> class student():
	def getdata(self,name,age):
		self.name=name
		self.age=age
	def display():
		print("name="self.name)
		
SyntaxError: invalid syntax
>>> 
>>> class student():
	def getdata(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=",self.name)
		print("age="self.age)
		
SyntaxError: invalid syntax
>>> 
>>> class student():
	def getdata(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=",self.name)
		print("age=",self.age)

		
>>> s=student()
>>> s.getdata("kaviya",23)
>>> s.display()
name= kaviya
age= 23
>>> s.name
'kaviya'
>>> s.age
23
>>> self.name
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    self.name
NameError: name 'self' is not defined
>>> class student():
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)

		
>>> s=student()
>>> s=student()
>>> s1=student("kaviya",23)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    s1=student("kaviya",23)
TypeError: student() takes no arguments
>>> s1=student("kaviya","23")
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    s1=student("kaviya","23")
TypeError: student() takes no arguments
>>> class sample:
	def _init_(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def display(self):
		print("name= %s"%self.name)
		print("age= %d"%self.age)
		print("city= %s"%self.city)

		
>>> s=sample("kaviya",12,"salem")
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    s=sample("kaviya",12,"salem")
TypeError: sample() takes no arguments
>>> s=sample()
>>> s.getdata("kaviya",12,"salem")
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    s.getdata("kaviya",12,"salem")
AttributeError: 'sample' object has no attribute 'getdata'
>>> class student():
	def _init_(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def display(self):
		print("name={}".format(self.name))
		print("age={}".format(self.age))
		print("city={}".format(self.city))

		
>>> s=student("kaviya",12,"salem")
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    s=student("kaviya",12,"salem")
TypeError: student() takes no arguments
>>> def -init-(self,name):
	
SyntaxError: invalid syntax
>>> def _init_(self,name):
	z

	
>>> class student:
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)

		
>>> s=student("kaviya",12)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    s=student("kaviya",12)
TypeError: student() takes no arguments
>>> class student():
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)

		
>>> s=student("kaviya",23)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    s=student("kaviya",23)
TypeError: student() takes no arguments
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s.display()
  File "<pyshell#134>", line 7, in display
    print("name= %s"%self.name)
AttributeError: 'sample' object has no attribute 'name'
>>> class student():
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("Name = %s" %self.name)
		print("Age = %d" %self.age)

		
>>> s=student("kaviya","23")
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    s=student("kaviya","23")
TypeError: student() takes no arguments
>>> class student():
	def _init_(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print("name=".format(self.name))
		print("city=".format(self.city))

		
>>> s=student()
>>> s=student()
>>> s1=student("kaviya","salem")
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    s1=student("kaviya","salem")
TypeError: student() takes no arguments
>>> class student:
	def_init_(self,name,city):
		
SyntaxError: invalid syntax
>>> class student:
	def _init_(self,name):
		self.name=name
	def display(self):
		print("name={}".format(self.name))

		
>>> s=student()
>>> 
>>> s=student("kaviya")
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    s=student("kaviya")
TypeError: student() takes no arguments
>>> def --init--(self,name):
	
SyntaxError: invalid syntax
>>> def _init_(self,name):
	self.name=name

	
>>> class student:
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name={}".format(self.name))
		print("age={}".format(self.age))

		
>>> s=student("kaviya",23)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    s=student("kaviya",23)
TypeError: student() takes no arguments
>>> class sample:
	def _init_(self,name,city):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("city=%s"%self.city)

		
>>> s=sample("kaviya" "city")
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    s=sample("kaviya" "city")
TypeError: sample() takes no arguments
>>> class sample:
	def _init_(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print(f "{self.name}")
		
SyntaxError: invalid syntax
>>> class sample:
	def _init_(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print(f"{self.name}")
		print(f"{self.city}")

		
>>> s=sample("kaviya,salem")
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    s=sample("kaviya,salem")
TypeError: sample() takes no arguments
>>> 
================================ RESTART: F:/kaviya/class 2.py ================================
Traceback (most recent call last):
  File "F:/kaviya/class 2.py", line 9, in <module>
    s=sample("kaviya",23)
TypeError: sample() takes no arguments
>>> class sample():
	def _init_(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(f"{self.name}")
		print(f"{self.age}")

		
>>> s=sample("kaviya",32)
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    s=sample("kaviya",32)
TypeError: sample() takes no arguments
>>> class student():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)

		
>>> s=student("kavi",23)
>>> s.display()
name=kavi
age=23
>>> class student():
	def __init__(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)
		print("city=%s"%self.city)

		
>>> s=student("kaviya"32"salem")
SyntaxError: invalid syntax
>>> s=student("kaviya" 23 "salem")
SyntaxError: invalid syntax
>>> s=student("kaviya","23","salem")
>>> s.display()
name=kaviya
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    s.display()
  File "<pyshell#263>", line 8, in display
    print("age=%d"%self.age)
TypeError: %d format: a number is required, not str
>>> s=student("kaviya", 23,"salem")
>>> s.display()
name=kaviya
age=23
city=salem
>>> class sample();
SyntaxError: invalid syntax
>>> class sample():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name={}"format(self.name))
		
SyntaxError: invalid syntax
>>> 
>>> class sample():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name={}".format(self.name))
		print("age={}".format(self.age))

		
>>> s=sample("kaviya",23)
>>> s.display()
name=kaviya
age=23
>>> class sample():
	def __init__(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def display(self):
		print(f"{self.name}")
		print(f"{self.age}")
		print(f"{self.city}")

		
>>> s=sample("kaviya",23,"salem")
>>> s.display()
kaviya
23
salem
>>> class sample():
	def __init__(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print("name"=self.name)
		
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> class sample():
	def __init__(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print("name={self.name}")
		print("city={self.city}")

		
>>> s=sample("kaviya","salem")
>>> s.display()
name={self.name}
city={self.city}
>>> class sample():
	def __init__(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print("name of the student="{self.name})
		print("city="{self.city})
		
SyntaxError: invalid syntax
>>> class sample():
	def __init__(self,name,age):
		self.name=name
		self.city=city
	def display(self):
		print(f"name of the student={self.name}")
		print(f"name of the city={self.city}")

		
>>> s=sample("kaviya",3)
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    s=sample("kaviya",3)
  File "<pyshell#314>", line 4, in __init__
    self.city=city
NameError: name 'city' is not defined
>>> s=sample("kaviya","salem")
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    s=sample("kaviya","salem")
  File "<pyshell#314>", line 4, in __init__
    self.city=city
NameError: name 'city' is not defined
>>> class sample():
	def __init__(self,name,city):
		self.name=name
		self.city=city
	def display(self):
		print(f"name of the student={self.name}")
		print(f"name of the city={self.city}")

		
>>> s=sample("kavi","salem")
>>> s.display()
name of the student=kavi
name of the city=salem
>>> class student():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("name=%s"%self.name)
		print("age=%d"%self.age)

		
>>> s=student("kavi",4)
>>> s.display()
name=kavi
age=4
>>> class student(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(f"{self.name}")
		print(f"{self.age}")

		
>>> student("kaviya",3)
<__main__.student object at 0x000001E5CCEA7610>
>>> display()
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    display()
NameError: name 'display' is not defined
>>> s=student("kaviya",3)
>>> s.display()
kaviya
3
>>> class student():
	def __init__(self,name):
		self.name=name
	def display(self):
		print("name={}".format(self.name))

		
>>> s=student("kavi")
>>> s.display()
name=kavi
>>> class student():
	def __init__(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def display(self):
		print("name=%s"%self.name)
		print("name={}".format(self.age))
		print(f"{self.city}")

		
>>> s=student("kaviya",3,"salem")
>>> student.display()
Traceback (most recent call last):
  File "<pyshell#361>", line 1, in <module>
    student.display()
TypeError: display() missing 1 required positional argument: 'self'
>>> s.display()
name=kaviya
name=3
salem
>>> class sample():
	def getdata(self):
		print("hi")

		
>>> s=sample()
>>> s.getdata
<bound method sample.getdata of <__main__.sample object at 0x000001E5CCEB76A0>>
>>> s.getdata()
hi
>>> class sample():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display():
		print(self.x+self.y)

		
>>> s=sample()
>>> s.getdata(100,129)
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    s.display()
TypeError: display() takes 0 positional arguments but 1 was given
>>> class sample():
	def getdata(self,x,y):
		self.x=x
		self.y=y
	def display(self):
		print(self.x+self.y)

		
>>> s=sample()
>>> s.getdata(122,455)
>>> s.display()
577
>>> s.x
122
>>> s.y
455
>>> class sample():
	def getdata(x,a,b):
		x.a=a
		x.b=b
	def display(x):
		if(x.a>x.b)
		
SyntaxError: invalid syntax
>>> class sample():
	def getdata(x,a,b):
		x.a=a
		x.b=b
	def display(x):
		if(x.a>x.b):
			print("x.a is greater")
		else:
			print("x.b is greater")

			
>>> s=sample()
>>> s.getdata(23,45)
>>> s.display()
x.b is greater
>>> class 