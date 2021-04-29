from decimal import Decimal
class module:
    def getdata(self,a,b):
        self.a=a
        self.b=b
        print(round(self.a,2))
        print(round(self.b))
        print(format(self.a,'<20f'))
        print(format(self.b,'^20f'))
        print(format(self.a,'>20f'))
        print('%2f'%self.a)
        print(self.a+self.b)

s=module()
s.getdata(2345.678,6780.1234)
s.display()



        
