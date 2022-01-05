#Find the length of a set

class Set:
    def _init__(self):
        pass

    def length(self,set1):
        count=0
        for x in set1:
            count+=1
        print(count)


solution=Set()
solution.length({1,2,3,5,6,8,8})