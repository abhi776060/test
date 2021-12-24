#To access index of list

class List:
    def __init__(self,lis):
        self.lis=lis

    def index(self,num):
        for x in range(len(self.lis)):
            if num == x:
                print(self.lis[x])

list1=List([1,2,3,5,6,6])
list1.index(5)