a,b,c=3,5,2
>>> if(a==0):
	print("the root is not possible" )
else:
	delta=(b*b-4*a*c)
	if delta >0:
		root1=-b+math.sqrt(delta)/(2*a)
		root2=-b-math.sqrt(delta)/(2*a)
		print(root1,root2)
		print("roots are real and uneqal")
		elif(delta==0):
  x,y,z=1,6,8
>>>  min=mid=max=""                  

 if((x<y)and(x<z)):
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
