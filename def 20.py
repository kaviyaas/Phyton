from decimal import Decimal
class module:
    def rare(a,b,c):
        a.b=b
        a.c=c
        print(round(a.b,2))
        print(format(a.c,'^20f'))
        print(format(a.c,'>20f'))
    
            
m=module()
m.rare(234.45,5698.4598)
m.display()
