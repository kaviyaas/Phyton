class myclass():
    def __init__(self,x,*vartuble):
        self.x=x
    def display(self):
        print(self.x+self.x)

m=myclass(1,2,3)
m.display()
    
