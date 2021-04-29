Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")
	get()
	def get():
		c=input("if you like to continue the operation again press y for yes and no for n:")
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")

			
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division+
enter the first num1:6
enter the second num2:8
6 + 8
14
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    getdata()
  File "<pyshell#33>", line 23, in getdata
    get()
UnboundLocalError: local variable 'get' referenced before assignment
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")
	get()
	def get():
		c=input("if you like to continue the operation again press y for yes and no for n:")
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")
		else:
			get()
			getdata()

			
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division+
enter the first num1:7
enter the second num2:8
7 + 8
15
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    getdata()
  File "<pyshell#39>", line 23, in getdata
    get()
UnboundLocalError: local variable 'get' referenced before assignment
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
	def get():
		c=input("if you like to continue the operation again press y for yes and no for n:")
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")
		else:
			get()
			getdata()

			
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division-
enter the first num1:9
enter the second num2:6
9 -6
3
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    getdata()
  File "<pyshell#42>", line 24, in getdata
    get()
UnboundLocalError: local variable 'get' referenced before assignment
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
def get():
	c=input("if you like to continue the operation again press y for yes and no for n:")
	if(c=='y'):
		getdata()
	elif(c=='n'):
		print("see you later")

	
SyntaxError: invalid syntax
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
     def get():
	     c=input("if you like to continue the operation again press y for yes and no for n:")
	     if(c=='y'):
		     getdata()
	     elif(c=='n'):print("see you later")
	     
SyntaxError: unindent does not match any outer indentation level
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
def get():
	
SyntaxError: invalid syntax
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
     def get():
	     
SyntaxError: unindent does not match any outer indentation level
>>> 
	def getdata():
		i=input('''please type the math operation would you like:
	+ for addition
	- for subtraction
	* for multiplication
	/ for division''')
		a=int(input("enter the first num1:"))
		b=int(input("enter the second num2:"))
		if i=='+':
			print('{} + {}'.format(a,b))
			print(a+b)
		elif i=='-':
			print('{} -{}'.format(a,b))
			print(a-b)
		elif i=='*':
			print('{} * {}'.format(a,b))
			print(a*b)
		elif i=='/':
			print('{} /{}'.format(a,b))
			print(a/b)
		else:
			print("enter the valid operation")

		get()
	 def get():
		 
SyntaxError: unexpected indent
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
     def get():
	     
SyntaxError: unindent does not match any outer indentation level
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
    def get():
	    
SyntaxError: unindent does not match any outer indentation level
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> copyright
Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
	def get():
		c=input("if you like to repeat the operation again press y for yes
			
SyntaxError: EOL while scanning string literal
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	get()
	def get():
		c=input('''if you like to repeat the operation again press y for yes and n for no''')
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")
		else:
			get()
			getdata()

			
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division+
enter the first num1:6
enter the second num2:4
6 + 4
10
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    getdata()
  File "<pyshell#72>", line 24, in getdata
    get()
UnboundLocalError: local variable 'get' referenced before assignment
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")

	def get():
		c=input('''if you like to repeat the operation again press y for yes and n for no''')
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")
		else:
			get()
			getdata()

			
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division-
enter the first num1:8
enter the second num2:7
8 -7
1
>>> get()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    get()
NameError: name 'get' is not defined
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")



	get()
	def get():
		c=input('''if you like to repeat the operation again press y for yes and n for no''')
		if(c=='y'):
			getdata()
		elif(c=='n'):
			print("see you later")
			
KeyboardInterrupt
>>> def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")



	get()
   def get():
		c=input('''if you like to repeat the operation again press y for yes and n for no''')
		if(c=='y'):
			getdata()
		elif(c=='n'):
			
SyntaxError: unindent does not match any outer indentation level
>>> 
================================ RESTART: F:/kaviya/class 13.py ===============================
>>> 
================================ RESTART: F:/kaviya/class 13.py ===============================
>>> 
================================ RESTART: F:/kaviya/class 13.py ===============================
>>> getdata()
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division-
enter the first num1:6
enter the second num2:7
6 -7
-1
if you like to repeat the operation again press y for yes and n for noY
please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division+
enter the first num1:5
enter the second num2:6
5 + 6
11
if you like to repeat the operation again press y for yes and n for no
=============================== RESTART: F:/kaviya/class2(1).py ===============================
Traceback (most recent call last):
  File "F:/kaviya/class2(1).py", line 1, in <module>
    class a():
  File "F:/kaviya/class2(1).py", line 7, in a
    b()
NameError: name 'b' is not defined
>>> 
=============================== RESTART: F:/kaviya/class2(1).py ===============================
Traceback (most recent call last):
  File "F:/kaviya/class2(1).py", line 1, in <module>
    class a():
  File "F:/kaviya/class2(1).py", line 8, in a
    b()
NameError: name 'b' is not defined
>>> 
=============================== RESTART: F:/kaviya/class2(1).py ===============================
Traceback (most recent call last):
  File "F:/kaviya/class2(1).py", line 1, in <module>
    class a():
  File "F:/kaviya/class2(1).py", line 8, in a
    b()
NameError: name 'b' is not defined
>>> 
>>> class student:
	name="kaviya"
	age=23

	
>>> s=student()
>>> hasattr(s,age)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    hasattr(s,age)
NameError: name 'age' is not defined
>>> hasattr(s,"age")
True
>>> hasattr(s,"exp")
False
>>> class student():
	def getdata(self,name,age,year):
		self.name=name
		self.age=age
		self.year=year
	def display(self):
		print("name of the student=%s" %self.name)
		print("age of the student=%d" %self.age)
		print("passed out year=%d" %self.year)

		
>>> s=student()
>>> s.getdata("abc",20,2020)
>>> s.display()
name of the student=abc
age of the student=20
passed out year=2020
>>> hasattr(s,"age")
True
>>> hasattr(s,"name")
True
>>> hasattr(s,"percentage")
False
>>> hasattr(s,"age","name")
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    hasattr(s,"age","name")
TypeError: hasattr expected 2 arguments, got 3
>>> class a():
	def getdata(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(f"{self.a}")
		print(f"{self.b}")

		
>>> a=a()
>>> a.getdata(9,7)
>>> a.display()
9
7
>>> hasattr(a,"a")
True
>>> import datetime
>>> datetime.time
<class 'datetime.time'>
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 4, 26, 13, 30, 14, 785838)
>>> x=datetime.now()
>>> x.month()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    x.month()
TypeError: 'int' object is not callable
>>> x.month
4
>>> x.year
2021
>>> x.microsecond
614589
>>> x.second
23
>>> x.fromisocalendar
<built-in method fromisocalendar of type object at 0x00007FFAA5584650>
>>> x.day
26
>>> x.date
<built-in method date of datetime.datetime object at 0x00000223095F7870>
>>> x.combine
<built-in method combine of type object at 0x00007FFAA5584650>
>>> datetime.fromisocalendar
<built-in method fromisocalendar of type object at 0x00007FFAA5584650>
>>> datetime.hour()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    datetime.hour()
TypeError: 'getset_descriptor' object is not callable
>>> today=datetime.now()
>>> today.date
<built-in method date of datetime.datetime object at 0x00000223095F7E70>
>>> today.day
26
>>> x=datetime.now()
>>> x.day
26
>>> import time
>>> today.day
26
>>> import time
>>> y.day
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    y.day
NameError: name 'y' is not defined
>>> import time
>>> import date
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    import date
ModuleNotFoundError: No module named 'date'
>>> from datetime import datetime
>>> datetime
<class 'datetime.datetime'>
>>> datetime.__dict__
mappingproxy({'__repr__': <slot wrapper '__repr__' of 'datetime.datetime' objects>, '__hash__': <slot wrapper '__hash__' of 'datetime.datetime' objects>, '__str__': <slot wrapper '__str__' of 'datetime.datetime' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'datetime.datetime' objects>, '__lt__': <slot wrapper '__lt__' of 'datetime.datetime' objects>, '__le__': <slot wrapper '__le__' of 'datetime.datetime' objects>, '__eq__': <slot wrapper '__eq__' of 'datetime.datetime' objects>, '__ne__': <slot wrapper '__ne__' of 'datetime.datetime' objects>, '__gt__': <slot wrapper '__gt__' of 'datetime.datetime' objects>, '__ge__': <slot wrapper '__ge__' of 'datetime.datetime' objects>, '__add__': <slot wrapper '__add__' of 'datetime.datetime' objects>, '__radd__': <slot wrapper '__radd__' of 'datetime.datetime' objects>, '__sub__': <slot wrapper '__sub__' of 'datetime.datetime' objects>, '__rsub__': <slot wrapper '__rsub__' of 'datetime.datetime' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFAA5584650>, 'now': <method 'now' of 'datetime.datetime' objects>, 'utcnow': <method 'utcnow' of 'datetime.datetime' objects>, 'fromtimestamp': <method 'fromtimestamp' of 'datetime.datetime' objects>, 'utcfromtimestamp': <method 'utcfromtimestamp' of 'datetime.datetime' objects>, 'strptime': <method 'strptime' of 'datetime.datetime' objects>, 'combine': <method 'combine' of 'datetime.datetime' objects>, 'fromisoformat': <method 'fromisoformat' of 'datetime.datetime' objects>, 'date': <method 'date' of 'datetime.datetime' objects>, 'time': <method 'time' of 'datetime.datetime' objects>, 'timetz': <method 'timetz' of 'datetime.datetime' objects>, 'ctime': <method 'ctime' of 'datetime.datetime' objects>, 'timetuple': <method 'timetuple' of 'datetime.datetime' objects>, 'timestamp': <method 'timestamp' of 'datetime.datetime' objects>, 'utctimetuple': <method 'utctimetuple' of 'datetime.datetime' objects>, 'isoformat': <method 'isoformat' of 'datetime.datetime' objects>, 'utcoffset': <method 'utcoffset' of 'datetime.datetime' objects>, 'tzname': <method 'tzname' of 'datetime.datetime' objects>, 'dst': <method 'dst' of 'datetime.datetime' objects>, 'replace': <method 'replace' of 'datetime.datetime' objects>, 'astimezone': <method 'astimezone' of 'datetime.datetime' objects>, '__reduce_ex__': <method '__reduce_ex__' of 'datetime.datetime' objects>, '__reduce__': <method '__reduce__' of 'datetime.datetime' objects>, 'hour': <attribute 'hour' of 'datetime.datetime' objects>, 'minute': <attribute 'minute' of 'datetime.datetime' objects>, 'second': <attribute 'second' of 'datetime.datetime' objects>, 'microsecond': <attribute 'microsecond' of 'datetime.datetime' objects>, 'tzinfo': <attribute 'tzinfo' of 'datetime.datetime' objects>, 'fold': <attribute 'fold' of 'datetime.datetime' objects>, '__doc__': 'datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])\n\nThe year, month and day arguments are required. tzinfo may be None, or an\ninstance of a tzinfo subclass. The remaining arguments may be ints.\n', 'min': datetime.datetime(1, 1, 1, 0, 0), 'max': datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), 'resolution': datetime.timedelta(microseconds=1)})
>>> from datetime import datetime
>>> datetime.yesterday()
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    datetime.yesterday()
AttributeError: type object 'datetime.datetime' has no attribute 'yesterday'
>>> datetime.now()
datetime.datetime(2021, 4, 26, 13, 43, 13, 959947)
>>> x.minute
37
>>> y=datetime.now()
>>> y
datetime.datetime(2021, 4, 26, 13, 45, 33, 740800)
>>> y.fold
0
>>> y.day
26
>>> y.hour
13
>>> y.fromisocalendar
<built-in method fromisocalendar of type object at 0x00007FFAA5584650>
>>> y.microsecond
740800
>>> today=datetime.now()
>>> today.year
2021
>>> x=datetime.now()
>>> x.year
2021
>>> x.month
4
>>> x=datetime.day()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    x=datetime.day()
TypeError: 'getset_descriptor' object is not callable
>>> x=datetime.now()
>>> x.year
2021
>>> x=datetime.now()
>>> x.day
26
>>> x.year
2021
>>> x.month
4
>>> x.time
<built-in method time of datetime.datetime object at 0x00000223095F7E70>
>>> datetime.now()
datetime.datetime(2021, 4, 26, 13, 56, 17, 369125)
>>> x=datetime.now()
>>> x
datetime.datetime(2021, 4, 26, 13, 56, 37, 934662)
>>> x.year
2021
>>> x.day
26
>>> x.month
4
>>> x.second
37
>>> x.microsecond
934662
>>> x.hour
13
>>> y=datetime.now()
>>> y.year
2021
>>> y.day
26
>>> y.now
<built-in method now of type object at 0x00007FFAA5584650>
>>> y.hour
14
>>> y.microsecond
119708
>>> y.minute
1
>>> y.max
datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
>>> y.date
<built-in method date of datetime.datetime object at 0x00000223095F7E70>
>>> y.day
26
>>> y.hour
14
>>> y=datetime.now()
>>> y.date
<built-in method date of datetime.datetime object at 0x00000223095F7330>
>>> y.day
26
>>> 