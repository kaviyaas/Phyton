class primenumber:
    def prime(self,num):
        self.num=num
        for i in range(2,num):
            if(num%i==0):
                print("num is not a prime number")
            else:
                print("prime number")

p1=primenumber()
p1.prime(11)
p1.display()
