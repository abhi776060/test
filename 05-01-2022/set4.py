#Remove item(s) from set

class Set:
    def __init__(self):
        pass


    def remove(self,ele,num):
        set2=set()
        for x in ele:
            if x == num:
                pass
            else:
                set2.add(x)
        print(set2)

set1=Set()
set1.remove({1,2,3,4,5},4)