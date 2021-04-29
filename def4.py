def display():
    i=int(input("enter the input"))
    j=int(input("enter the input"))
    for i in range(0,i):
        for j in range(0,j):
            if(j>=1 or j<=5) or (i==0 or i==3 or i==5)and(j==0):
                print("*",end="")
            else:
                print(end="")
        print()

display()        
