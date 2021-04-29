class format:
    def getdata(a,arg1,*vartuble):
        a.arg1=arg1
        result1=list(map(list,a.arg1))
        print(result1)
        


f=format()
f.getdata('sat,mat,cat,sad')
f.display()
        
        
    
