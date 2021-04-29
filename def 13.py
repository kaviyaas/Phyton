class loop:
    def getdata(a,b,c):
        a.b=a
        a.c=a
        return(format(a.b,'<10f'))
        #return((format(a.c,'>10f'))


l=loop()
l.getdata(45362,67895)
l.display()
        
