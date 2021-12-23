#Printing elements in ascending order

class List:
    def __init__(self):
        pass

    def assend(self,lis1):
        lis2=[]
        for x in sorted(lis1):
            lis2.append(x)
        print(lis2)
list1=List()
list1.assend([5,1,7,8,9,3,5])