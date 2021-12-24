#Flatten a shallow

class List:
    def __init__(self):
        pass

    def flatten(self,*lis1):
        lis2=[]
        for x in lis1:
            lis2+=x
        print(lis2)
list1=List()
list1.flatten([1,2,3,5,6],['a','f','h'],[6],[8,6,8,6])