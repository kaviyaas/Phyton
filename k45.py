Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x,y,z=1,6,8
>>>  min=mid=max=""
 
SyntaxError: unexpected indent
>>> min=mid=max=""
>>> if((x<y)and(x<z)):
	if(y<z):
		min,mid,max=x,y,z
	else:
		min,mid,max=x,z,y
elif((y<x)&(y<z)):
	if(x<z):
		min,mid,max=y,x,z
	else:
		min,mid,max=y,z,x
elif:
	
SyntaxError: invalid syntax
>>> if((x<y)and(x<z)):
	if(y<z):
		min,mid,max=x,y,z
	else:
		min,mid,max=x,z,y
elif((y<x)&(y<z)):
	if(x<z):
		min,mid,max=y,x,z
	else:
		min,mid,max=y,z,x
elif((z<x)&(z<y)):
	if(x<y):
		min,mid,max=z,x,y
	else:
		min,mid,max=z,y,x

		
>>> 
>>> print("numbers in ascending order",min,mid,max)
numbers in ascending order 1 6 8
>>> 