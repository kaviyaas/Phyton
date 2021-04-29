class sample:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name=%s"%self.name)
        print("age=%d"%self.age)

s=sample("kaviya",23)
s.display()
