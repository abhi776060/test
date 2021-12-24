#Difference betweeen 2 lists

class List:
    def __init__(self):
        pass

    def diff(self,lis1,lis2):
        lis=[]
        for x in lis1:
            if x not in lis2:
                lis.append(x)
        print(lis)

list1=List()
list1.diff([1,2,3,4,5],[4,5,8,9])