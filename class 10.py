class sample():
    def __init__(self,name,i):
        self.name=name
        self.i=i
    def getdata(self,name1):
        self.name1=name1
    def display(self):
        while(self.i<10):
           self.i=1
           print(self.name)
           self.i+=1
        else:
            if(self.i<20):
                print(self.name1)
                self.i+=1

s=sample("kaviy",1)
s.getdata("dhanya")
s.display()

            
        
