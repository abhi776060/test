#Finding common items from two lists
class List:
    def __init__(self):
        pass

    def find(self,lis1,lis2):
        lis3=[]
        for x in lis1:
            if x in lis2:
                lis3.append(x)
        print(lis3)

list1=List()
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
list1.find(color1,color2)