#Check a list contains sublist

class List:
    def __init__(self):
        pass
    def check(self,lis):
        flag=False
        for x in lis:
            if type(x) is list:
                flag=True
            else:
                pass
        print(flag)


list1=List()
list1.check([1,2,3,5,[8,58]])