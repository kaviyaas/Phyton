Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample():
	def getdata(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
	def display(self):
		if(self.a > self.b)and (self.a > self.c):
			if(self.b > self.c):
				print(self.a,self.b,self.c)
			else:
				print(self.a,self.b,self.c)
		elif(self.b > self.a) and (self.b > self.c):
			if(self.a > self.c):
				print(self.b,self.a,self.c)
			else:
				print(self.b,self.c,self.a)
		elif(self.c > self.a) and (self.c > self.b):
			if(self.a > self.b):
				print(self.c,self.a,self.b)
			else:
				print(self.c,self.b,self.a)

				
>>> s=sample()
>>> s.getdata(45,23,89)
>>> s.display()
89 45 23
>>> 