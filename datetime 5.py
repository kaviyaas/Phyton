import pytz
from datetime import datetime
class sample():
    dict={}
    def display(self):
        for i in pytz.all_timezones:
            x=datetime.now().astimezone(tz=pytz.timezone(i))
            c=len(i)
            for j in range(0,c):
                sample.dict[i]=x
                print(sample.dict)
            print('\n')    
        
s=sample()
s.display()
