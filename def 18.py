class facts:
    def getdata(s,num=7,fact=1):
        s.num=num
        s.fact=fact
        for i in range(1,s.num+1):
            s.fact=s.fact*i
            print("the factorial of ",s.num , s.fact)


f=facts()
f.getdata()
f.display()
