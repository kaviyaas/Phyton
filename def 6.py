def dis():
    row=int(input("enter the num"))
    currentnum=1
    stop=2
    for r in range(row):
        for c in range(1,stop):
            print(currentnum,end="")
            currentnum +=1
        print("")
        stop+=2

dis()        
        
            
