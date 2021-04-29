class student:
    def operators(lf,a,b,c,d,e):
        lf.a=a
        lf.b=b
        lf.c=c
        lf.d=d
        lf.e=e
        if(lf.a%lf.e==0):
            print("a is divided")
        elif(lf.b%lf.e==0):
            print("b is divided")
        elif(lf.c%lf.e==0):
            print("c is divided")
        elif(lf.d%lf.d==0):
            print("d is divided")
        else:
            print("not divided")


s=student()
s.operators(56,67,78,90,15)
s.display()
        
        
        
