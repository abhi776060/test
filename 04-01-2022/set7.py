#Create a union of sets
class Set:
    def __init__(self):
        pass
    def union(self,set1,set2):
        set3=set()
        for x in set1:
            set3.add(x)
        for y in set2:
            set3.add(y)
        print(set3)


solution=Set()
solution.union({1,2,3,4,5},{4,5,6,8})