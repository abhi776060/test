#Replace the last element in a list with another list
class List:
    def __init__(self,list1):
        self.list1=list1

    def add_at_end(self,n):
        self.list1[-1]=n

        print(self.list1)
lis=[1,2,3,4]
list1=List(lis)
list1.add_at_end([1,2,5])
