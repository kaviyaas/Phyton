class sample():
    def __init__(self,name):
        self.name=name
    def getdata(self,name1):
        self.name1=name1
    def display(self):
        result1=(10*self.name)
        result2=(10*self.name1)
        print(result1)
        print(result2)

        
s=sample("kaviya")
s.getdata("dhanya")
s.display()
