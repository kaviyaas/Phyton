Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display(x):
	x=x.upper()

	
>>> def display(x):
	x=x.upper()
	print(x)

	
>>> def display1(a):
	a=a.lower(a)
	print(a)

	
>>> class sample():
	def display(x):
		x=x.upper(x)
		print(x)
	def display1(y):
		y=y.lower(y)
		print(y)
	def show(f,f1,a,b):
		a=f(a)
		b=f1(b)
		print(a)
		print(b)

		
>>> s=sample()
>>> s.display("source")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.display("source")
TypeError: display() takes 1 positional argument but 2 were given
>>> s=sample()
>>> s.display("s")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.display("s")
TypeError: display() takes 1 positional argument but 2 were given
>>> def display(x):
	x=x.upper(x)
	print(x)

	
>>> display("data")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    display("data")
  File "<pyshell#33>", line 2, in display
    x=x.upper(x)
TypeError: str.upper() takes no arguments (1 given)
>>> class sample():
	def display(x):
		x=x.upper()
		print(x)
	def display1(y):
		y=y.lower()
		print(y)
	def show(f,f1,a,b):
		a=f(a)
		b=f1(b)
		print(a)
		print(b)

		
>>> s=sample()
>>> s.display("source")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.display("source")
TypeError: display() takes 1 positional argument but 2 were given
>>> 