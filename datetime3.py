from datetime import datetime
class sample:
    def get(self):
        x=datetime.now()
        print(x.year)
        print(x.month)
        print(x.day)

s=sample()
s.get()

        
