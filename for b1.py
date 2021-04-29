for r in range(0,6):
    for c in range(0,5):
        if(c==0 or c==5)|(r==0 or r==2 or r==5)and(c>0 and c<4):
            print("*",end="")
        else:
            print(end="")
    print()        
        
        
