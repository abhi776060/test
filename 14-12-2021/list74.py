#Reverse list of elements and print in upper case
class List:
    def __init__(self):
        pass

    def reverse_andUpper(self,lis):
        lis1=[]
        for x in lis:
            lis1.insert(0,x.upper())
        return lis1
me=List()

print(me.reverse_andUpper(['apple','banana','cat','dog']))
