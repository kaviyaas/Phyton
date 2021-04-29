def display():
    row=int(input("enter the num"))
    for r in range(1,row):
        for c in range(row,0,-1):
            print(c,end="")
        print("")
        
display()
        
