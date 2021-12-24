#Finding index of an item in specified list

class List:
    def __init__(self,lis):
        self.lis=lis

    def index(self,num):
        message='not vali'
        for x in range(len(self.lis)):
            if num==self.lis[x]:
                message=str(x)
            else:
                pass
        print(message)


list1=List([1,2,3,4,5])
list1.index(5)