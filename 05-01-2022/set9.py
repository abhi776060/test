#Create a symmetric difference.

class Set:
    def __init__(self):
        pass

    def symmertric_difference(self,set1,set2):
        set3=set()
        for x in set1:
            if x in set2:
                pass
            else:
                set3.add(x)
        for x in set2:
            if x in set1:
                pass
            else:
                set3.add(x)
        print(set3)
solution1=Set()
solution1.symmertric_difference({1,2,3,4,5,6},{4,5,6,7,8})