class phyton:
    def getdata(s,a,b,c):
        s.a=a
        s.b=b
        s.c=c
        if(a==0):
            print("the eqn is not satisfy")
        else:
            delta=b*b-4*a*c
            if(delta>0):
                r1=-b+sqrt(delta)/2*a
                r2=-b+sqrt(delta)/2*a
                print(r1,r2,"roots are real and unequal")
            elif(delta==0):
                s.r1=-b/2*a
                print(r1,"roots are real and equal")
            else:
                print("roots are cmplx and imaginary")


s=phyton()
s.getdata(4,5,2)
s.display()

                
        
