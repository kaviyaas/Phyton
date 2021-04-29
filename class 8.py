class sample():
    def __init__(self,name,c):
        self.name=name
        self.c=c
    def getdata(self,name1):
        self.name1=name1
    def display(self):
        for i in range(0,10):
            for j in range(0,self.c):
                 print(self.name)
                 if(self.c==10):
                      for j in range(0,10):
                          print(self.name1)
            if(j==10):
                break
            print("")
                 
                    
            
            
        
s=sample("kaviya",10)
s.getdata("dhanya")
s.display()
