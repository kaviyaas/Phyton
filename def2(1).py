def getnum(x,y,z):
    if(x>y & x>z | x!=y | x!=z):
        if(y>z):
            print(x,y,z)
        else:
            print(x,z,y)
    elif(y>z & y>x | y!=x | y!=z):
        if(x>z):
            print(y,x,z)
        else:
            print(y,z,x)
    elif(z>x & z>y | z!=x | z!=y):
        if(x>y):
            print(z,x,y)
        else:
            print(z,y,x)
    else:
        print("all are equal")
    

getnum(1,2,3)       
            
        
        
        
