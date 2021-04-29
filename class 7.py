Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class myclass():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		if(self.a == str):
			print("true")
		elif(self.b == str):
			print("true self.b")
		else:
			print("not a string")

			
>>> m=myclass("arrow","add")
>>> m.display()
not a string
>>> class dog():
	def __init__(self,breed,color,name):
		self.breed=breed
		self.color=color
		self.name=name
	def display(self):
		self.name=input("enter the choice:")
		if(self.name="rodger"):
			
SyntaxError: invalid syntax
>>> class dog():
	def getdata1(self,name):
		self.name=name
	def getdata2(self,breed,color,name):
		self.breed=breed
		self.color=color
	def display(self):
		self.name=input("enter the choice:")
		if(self.name == "rodger"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
>>> d=dog()
>>> d.getdata1()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d.getdata1()
TypeError: getdata1() missing 1 required positional argument: 'name'
>>> d.getdata1("rodger")
>>> d.getdata2("pug","brown")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.getdata2("pug","brown")
TypeError: getdata2() missing 1 required positional argument: 'name'
>>> class dog():
	def getdata1(self,name):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		self.name=input("enter the choice:")
		if(self.name == "rodger"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
>>> d=dog()
>>> d.getdata1("rodger")
>>> d.getdata2("pug","brown")
>>> d.display()
enter the choice:rodger
breed=pug
color=brown
>>> d.display()
enter the choice:buz0
choice is not given
>>> d.display()
enter the choice:buzo
breed=pug
color=brown
>>> class dog():
	def getdata1(self,name=input('enter the choice:'):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")
		     
SyntaxError: invalid syntax
>>> class dog():
	def getdata1(self,name=input('enter the choice:')):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
enter the choice:rodger
>>> d=dog()
>>> d.getdata2("pug","black")
>>> d.display()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d.display()
  File "<pyshell#47>", line 8, in display
    if(self.name == "rodger"):
AttributeError: 'dog' object has no attribute 'name'
>>> d=dog()
>>> d.getdata1("rodger")
>>> d.getdata2("pug","black")
>>> d.display()
breed=pug
color=black
>>> 
>>> 
>>> class dog():
	def getdata1(self,name=input('enter the choice:')):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
enter the choice:buzo
>>> 
>>> class dog():
	def getdata1(self,name=input('enter the choice:')):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("rodger details")
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("buzo details")
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
enter the choice:buzo
>>> d.getdata1("buzo")
>>> d.getdata2("bulldog","brown")
>>> d.display()
breed=bulldog
color=brown
>>> class dog():
	def getdata1(self,name=input('enter the choice:')):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("rodger details")
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		elif(self.name == "buzo"):
			print("buzo details")
			print("breed={}".format(self.breed))
			print("color={}".format(self.color))
		else:
			print("choice is not given")

			
enter the choice:buzo
>>> d.getdata1("buzo")
>>> d.getdata2("bull","brown")
>>> d.display()
breed=bull
color=brown
>>> class dog():
	def getdata1(self,name=input('enter the choice:')):
		self.name=name
	def getdata2(self,breed,color):
		self.breed=breed
		self.color=color
	def display(self):
		if(self.name == "rodger"):
			print("rodger details")
			print("breed of the rodger={}".format(self.breed))
			print("color of the rodger={}".format(self.color))
		elif(self.name == "buzo"):
			print("buzo details")
			print("breed of the buzo={}".format(self.breed))
			print("color of the buzo={}".format(self.color))
		else:
			print("choice is not given")

			
enter the choice:
>>> class sample():
	def getdata(self,name):
		self.name=name
	def display(self):
		for i in range(0,10):
			print(self.name)

			
>>> s=sample()
>>> s.getdata("kaviya")
>>> s.display()
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
>>> class sample():
	def init(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			print(self.name)
		print(self.name2)
		
SyntaxError: expected an indented block
>>> class sample():
	def init(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
		print(self.name2)

		
>>> class sample():
	def __init__(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
		print(self.name2)

		
>>> s=sample(kaviya,Dhanya)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s=sample(kaviya,Dhanya)
NameError: name 'kaviya' is not defined
>>> s=sample("kaviya","dhanya")
>>> s.display()
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
dhanya
>>> class sample():
	def init(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
			 break
		print(self.name2)

		
>>> s=sample("kaviya","dhanya")
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s=sample("kaviya","dhanya")
TypeError: sample() takes no arguments
>>> class sample():
	def __init__(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
			 break
		print(self.name2)

		
>>> s=sample("kaviya","dhanya")
>>> s.display()
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
kaviya
dhanya
>>> class sample():
	def __init__(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
			 break
		        print(self.name2)
		        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class sample():
	def __init__(self,name,name2):
		self.name=name
		self.name2=name2
	def display(self):
		for i in range(0,10):
			for j in range(0,10):
			 print(self.name)
			 break
		         print(self.name2)