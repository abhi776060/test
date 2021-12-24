#Select an item randomly
from random import randrange
class List:
    def __init__(self):
        pass

    def rand(self,lis):
        i=len(lis)
        num=randrange(i)
        print(lis[num])

list1=List()
list1.rand([1,2,5,8,6])