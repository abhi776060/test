#A list contains group of strings.Convert each word to capital letter and print
class List:
    def __init__(self):
        pass

    def capital(self,lis):
        lis1=[]
        for x in lis:
            lis1.append(x.upper())
        return lis1
me=List()

print(me.capital(['apple','banana','cat','dog']))
