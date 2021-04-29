a,b,c=7,9,3
if((a>b)&(a>c)&(a!=b)&(a!=c)):
    print("a is larger")
elif((b>a)&(b>c)&(b!=a)&(b!=c)):
    print("b is larger")
elif((c>a)&(c>b)&(c!=a)&(c!=b)):
    print("c is larger")
else:
    print("all are equal")
