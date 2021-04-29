def multipleof5(n):
 if(n % 5 == 0):
    return n

mylist0={10,12,13,15,20}
mylist1=list(filter(multipleof5,mylist0))
print(mylist1)
    
