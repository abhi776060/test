#Insert an element before each element of a list

class List:
    def __init__(self,lis1):
        self.lis1=lis1

    def insert(self,lis2):
        lis3=[]
        for x in self.lis1:
            lis3.append(lis2)
            lis3.append(x)
        print(lis3)

list1=List(['Red', 'Green', 'Black'])
list1.insert('abhi')