class format:
    def getdata(a,b,c):
        a.b=b
        a.c=c
        from decimal import Decimal
       # print(round(a.b))
        #print(round(a.c))
        print(format(a.b,'<10f'))
        #print(format(a.c,'>10f'))
        #print(format(a.c,'^10f'))
        #print(format(-a.c,'>10f'))
        #print(round(a.c,-3))


f=format()
f.getdata(123.4567,2345.6789)
