Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=["xyz","erd","ujh"]
>>> a=map(lambda t:t.count("x"),["xyz","erd","ujh"])
>>> for i in a:
	print(i)

	
1
0
0
>>> t=["xyz","erd","ujh"]
>>> a=map(lambda t:t.count("x"),["xyz","erd","ujh"])
>>> for i in a:
	print(a)

	
<map object at 0x0000028F55002CA0>
<map object at 0x0000028F55002CA0>
<map object at 0x0000028F55002CA0>
>>> t=(1,2,5,19,2)
>>> a=map(lambda t:t