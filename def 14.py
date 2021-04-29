from decimal import Decimal
class person:
    def format(a,b,c):
        a.b=b
        a.c=c
        print(format(a.b,'<10f'))
        print(format(a.c,'^20f'))
        print(round(a.b,2))
        print(a.b+a.c)
        print(a.b*a.c)
        
s=person()
s.format(23.346,45.567)
s.display()
        
    
