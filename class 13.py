def getdata():
	i=input('''please type the math operation would you like:
+ for addition
- for subtraction
* for multiplication
/ for division''')
	a=int(input("enter the first num1:"))
	b=int(input("enter the second num2:"))
	if i=='+':
		print('{} + {}'.format(a,b))
		print(a+b)
	elif i=='-':
		print('{} -{}'.format(a,b))
		print(a-b)
	elif i=='*':
		print('{} * {}'.format(a,b))
		print(a*b)
	elif i=='/':
		print('{} /{}'.format(a,b))
		print(a/b)
	else:
		print("enter the valid operation")



	get()
def get():
    c=input('''if you like to repeat the operation again press y for yes and n for no''')
    if(c=='y'):
        getdata()
    elif(c=='n'):
        print("see u later : ")
        get()
    getdata()
