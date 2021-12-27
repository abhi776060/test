#Maximum and Minimum in a Set
'''
Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
Output : max is 65 min is 1
'''
class Set:
    def __init__(self):
        pass
    def max_min(self,set2):
        lis=list(set2)
        max_num=lis[0]
        min_num=lis[0]
        for x in lis:
            if max_num >x:
                max_num=x
            elif min_num<x:
                min_num=x
            
        print('max is',max_num)
        print('min is', min_num)


set1=Set()
set1.max_min({8, 16, 24, 1, 25, 3, 10, 65, 55})