#Create a shallow copy of sets.
class Set:
    def __init__(self):
        pass

    def shallow_copy(self,set1):
        print('main set',id(set1))
        set2=list(set1)
        set3=set(set2)
        print('new set',id(set3))

solution=Set()
solution.shallow_copy({1,2,3,4,8,9})

