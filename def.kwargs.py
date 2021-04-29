class key:
    def word(**kwargs):
        for i,j in kwargs.items():
            print(i,j)

k=key()
k.word("name=arguments","type=required arguments")
k.display()
