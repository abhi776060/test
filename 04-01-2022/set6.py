#Create an intersection of sets
class Set:
    def __init__(self):
        pass

    def intersection(self,set1,set2):
        new_set=set()
        for x in set1:
            if x in set2:
                new_set.add(x)
        print(new_set)

solution1=Set()
solution1.intersection({1,2,3,4},{2,3,5,6})