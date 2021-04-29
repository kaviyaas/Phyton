class number:
    def getdata(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print(self.x,self.y,self.z)
        if(self.x>self.y):
            print(self.x)
        elif(self.y>self.z):
            print(self.y)
        else:
            print("the value is not given")

s=number()
s.getdata(34,65,56)
s.display()
