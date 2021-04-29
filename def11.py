class decimal:
    def getdata(a,b,c):
        a.b=b
        a.c=c
        from decimal import Decimal
        a.b=Decimal('4.5')
        a.c=Decimal('4.3')
        print(a.b+a.c)
        print(a.b-a.c)
        print(a.b*a.c)

        
d=decimal()
d.getdata(3.4,5.6)
d.display()
