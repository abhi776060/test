#Find maximum and the minimum value in a set

class Set:
    def __init__(self):
        pass

    def max_min(self,set1):
        set1=list(set1)
        max=min=set1[0]
        for x in set1:
            if x<min:
                min=x
        for x in set1:
           if x>max:
               max=x
        print(min,max)


solution1=Set()
solution1.max_min({2,99,-6,3,4,5})