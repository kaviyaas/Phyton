Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class phyton():
	def __init__(self,r):
		self.r=r
	def display(self):
		for i in range(0,r+1):
			for j in range(i):
				print(i,end="")
			print("")

			
>>> p=phyton(6)
>>> p.display()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    p.display()
  File "<pyshell#9>", line 5, in display
    for i in range(0,r+1):
NameError: name 'r' is not defined
>>> class phyton():
	def __init__(self,r):
		self.r=r
	def display(self):
		for i in range(0,self.r+1):
			for j in range(i):
				print(i,end="")
			print("")