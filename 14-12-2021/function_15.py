#takes a list and returns a new list with unique elements of the first list.

class Function:
    def __init__(self):
        pass
    def unique(self,lis1):
        lis2=[]
        for x in lis1:
            if x in lis2:
                pass
            else:
                lis2.append(x)
        return lis2
me=Function()
lis1=[1,2,3,1,2,7,4,5,6,7,8]
print(me.unique(lis1))