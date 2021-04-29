from datetime import datetime
def getdata():
    x=datetime.now()
    print("{}/{}/{}".format(x.day,x.month,x.year))
    get()
def get():
    i=("if you want to complete the opration y for yes and no for n:")
    if(i=='y'):
        getdata()
    elif(i=='n'):
        print("see you later")
        



     
