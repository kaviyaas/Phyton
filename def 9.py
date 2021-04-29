class greater:
    def condition(gname,a,b):
        gname.a=a
        gname.b=b
        if(gname.a > gname.b):
            print("a is greater")
        elif(gname.a == gname.b):
            print("equals")
        else:
            print("a is smaller")


s=greater()
s.condition(56,78)
s.display()
