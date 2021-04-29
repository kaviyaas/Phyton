for row in range(7):
    for col in range(4):
        if(col==0 and row>=0)or(col==1 and row==2)or(col==1 and row==4)or(col==2 and row==1) and (col==2 and row==5)or(col==3 and row==0) or (col==3 and row==6):
                print("*",end="")
        else:
            print(end="")
    print() 
