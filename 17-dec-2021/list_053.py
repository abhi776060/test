#Create a list with infinite elements

class List:
    def __init__(self):
        pass

    def infinite(self,n):
        lis1=[x for x in range(1,n+1)]
        print(lis1)

list1=List()
list1.infinite(50)