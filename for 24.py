for r in range(0,5):
    for c in range(0,5):
        if(c==0 or r==0)&(c==1 or r==1)&(c==2 or r==2)&(c==3 or r==3)&(c==4 or r==4):
            print("*",end="")
        else:
            print(end="")
    print('\n')        
