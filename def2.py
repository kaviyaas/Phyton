Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def display(name,age,year):
	return(name)

>>> display("kaviya",23,1998)
'kaviya'
>>> def getstudent(x,y,z):
	if(x<y)&(x>z):
		if(y<z):
			return(x,y,z)
		else:
			return(x,z,y)
	else:
		return("all are equal")

	
>>> getstudent(22,45,23)
'all are equal'
>>> 
>>> def getnum(x,y,z):
	return x

>>> getnum(56,67,78)
56
>>> 
>>> def array():
	print(array)

	
>>> array(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    array(1,2,3,4)
TypeError: array() takes 0 positional arguments but 4 were given
>>> def display(*args):
	print(args)

	
>>> display(1,2,3)
(1, 2, 3)
>>> def displayme():
	n=int(input("enter the input"))
	k=n*2
	for r in range(0,n):
		for c in range(0,k):
			print(end="")
			k=k-2
			for c in range(0,n+1):
				print("*",end="")
		print()	