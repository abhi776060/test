#Remove an item from a set if it is present in the set.
class Set:
    def __init__(self):
        pass

    def remove(self,ele,num):
        flag="not present"
        for x in ele:
            if x == num:
                flag="present"
            else:
               flag="not present"
        print(flag)



set1=Set()
set1.remove({1,2,3,4,5,6},5)