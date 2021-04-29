for r in range(0,5):
    for c in range(0,5):
        if(c==0 or r>=0)and(c>0 and r==0) or (r==3  and c>0):
            if(c==0 or r>=0) or (r==0 and c>0) or (r==4 and c>0):
                print("$",end="")
            else:
                print()
        else:
            print(end="")
    print()        
