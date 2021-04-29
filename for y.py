for row in range(5):
    for col in range(5):
        if(col==2 and row>1)or(row==col and col<2)or(row==0 and col==4)or(row==1 and col==3):
            print("*",end="")
        else:
            print(end="")
    print()

for row in range(7):
      for col in range(4):
            if(col==0 and row>=0)or(col==1 and row==2)or(col==1 and row==4)or(col==2 and row==1)or(col==2 and row==5)or(col==3 and row==0)or(col==3 and row==6):
                print("*",end="")
      print()        
