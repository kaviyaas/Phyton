Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample():
	count=0
	def __init__(self,name,age,exp):
		self.name=name
		self.age=age
		self.exp=exp
		sample.count+=1
	def display(self):
		print("Name of the employee:%s"%self.name)
		print("age of the employee:{}".format(self.age))
		print(f"Exp of the employee:{self.exp}")
		print(sample.count)

		
>>> s=sample("kaviya",23,2)
>>> s.display()
Name of the employee:kaviya
age of the employee:23
Exp of the employee:2
1
>>> s1=sample("xyz",54,7)
>>> s1.display()
Name of the employee:xyz
age of the employee:54
Exp of the employee:7
2
>>> getattr(s1,"name")
'xyz'
>>> setattr(s1,"age",45)
>>> s1.display()
Name of the employee:xyz
age of the employee:45
Exp of the employee:7
2
>>> getattr(s,"age")
23
>>> id(s)
2570259561488
>>> setattr(s,"name","abc")
>>> s.display()
Name of the employee:abc
age of the employee:23
Exp of the employee:2
2
>>> isinstance(s,sample)
True
>>> isinstance(s1,sample)
True
>>> class myclass():
	college name:"sims"
	
SyntaxError: invalid syntax
>>> class myclass():
	collegename:"sims"
	def __init__(self,name,year,course):
		self.name=name
		self.year=year
		self.course=course
	def display(self):
		print("name of the student:{}".format(self.name))
		print("year of the student:%d"%dself.year)
		print("")