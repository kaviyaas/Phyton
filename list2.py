Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample():
	def getdata(self):
		b=({"name":"xyz"})
		print(f"name oh the person:{}")
		
SyntaxError: f-string: empty expression not allowed
>>> class sample():
	def getdata(self):
		b=({"name":"xyz"})
		print(f"name oh the person:{b}")

		
>>> s=sample()
>>> s.getdata()
name oh the person:{'name': 'xyz'}
>>> class sample():
	def getdata(self):
		b=[1,2,3,4]
	def display(self):	
		print(b.append(2))
		print(b.count(3))
		print(b.index(2,1))
		print(b.insert(3,3))
		print(b.reverse())
		print(b.sort())

		
>>> s=sample()
>>> s.getdata()
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.display()
  File "<pyshell#18>", line 5, in display
    print(b.append(2))
NameError: name 'b' is not defined
>>> class sample():
	def getdata(self):
		b=[1,2,3,4]
		print(b.append(2))
		print(b.count(3))
		print(b.index(2,1))
		print(b.insert(3,3))
		print(b.reverse())
		print(b.sort())

		
>>> s=sample()
>>> s.getdata()
None
1
1
None
None
None
>>> class sample():
	b=[1,2,3,4]
	def getdata(self):
	def display(self):
		
SyntaxError: expected an indented block
>>> class sample():
	b=[1,2,3,4]
	def getdata(self):
		print(sample.b)
	def display():
		print(sample.b.append(4))

		
>>> s=sample()
>>> s.getdata()
[1, 2, 3, 4]
>>> s.display()class sample():
	b=[1,2,3,4]
	def getdata(self):
		print(sample.b)
	def display(self):
		print(sample.b.append(5))
		
SyntaxError: invalid syntax
>>> class sample():
	b=[1,2,3,4]
	def getdata(self):
		print(sample.b)
	def display(self):
		print(sample.b.append(5))

		
>>> s=sample()
>>> s.getdata()
[1, 2, 3, 4]
>>> s.display()
None
>>> class sample():
	b=[1,2,3,4]
	def getdata(self,x):
		self.x=x
		print(sample.b)
	def display(self):
		print(sample.b.append(self.x))

		
>>> s=sample()
>>> s.getdata(5)
[1, 2, 3, 4]
>>> s.display()
None
>>> class sample():
	a=[1,2,3]
	x=5
	print(a.append(5))

	
None
>>> class sample():
	a=[1,2,3]
	x=5
	print(a.append(x))

	
None
>>> class sample():
	a=[1,2,3,4]
	def getdata(self,x):
		self.x=x
	def display(self):
		print(sample.a.append(self.x))
		print(sample.a.sort())

		
>>> s=sample()
>>> s.getdata(3)
>>> s.display()
None
None
>>> class sample():
	def getdata(self,list,x):
		self.list=list
		self.x=x
	def display(self):
		print(self.list.append(self.x))
		print(self.list.sort())

		
>>> s=sample()
>>> s.getdata([1,2,3,4],5)
>>> s.display()
None
None
>>> a=[1,2,3]
>>> a.append(3)
>>> a
[1, 2, 3, 3]
>>> None
>>> class sample():
	list=[12,45,56]
	def getdata(self,x):
		self.x=x
	def display(self):
		print(self.list.append(self.x))
		print(self.list.sort())
		pass


	

		





	


		
	def display(self):	