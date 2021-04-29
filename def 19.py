from decimal import Decimal
class name:
    def filter(a,b,c):
        a.b=b
        a.c=c
        print(round(a.b,2))
        print(round(a.c,3))
        print(format(a.b,'^20f'))
        print(format(a.c,'<10f'))
        print(format(a.b,'>20f'))
        print(round(a.b,-2))
        print(round(-a.c))
        print(a.b+a.c)
        print(a.b-a.c)
        print('%2f'%a.b)

d=name()
d.filter(4539.675,67843.67898)
d.display()

        
        
