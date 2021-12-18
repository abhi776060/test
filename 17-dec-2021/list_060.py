#Find a tuple, the smallest second index value from a list of tuples
class List:
    def __init__(self,list1):
        self.list1=list1

    def find_tuple_index(self,n):
        for x in self.list1:
            if type(x) is tuple:
                print(x[n])


lis=[1,2,3,4,5,(1,2,5)]
list1=List(lis)
list1.find_tuple_index(1)