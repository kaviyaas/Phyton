import random
from sys import intern
class range:
    def func(a,b,c):
        a.b=b
        a.c=c
        print(a.b is a.c)
        print(a.b is not a.c)
        print(id(a.b),id(a.c))
        print(random.random())
        print(random.randint(0,7))
        print(random.randint(0,67))
        
        
r=range()
r.func("i18n solution","i18n solution")
r.display()
