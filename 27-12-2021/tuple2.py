#Maximum and Minimum K elements in Tuple
'''
Input : test_tup = (3, 7, 1, 18, 9), k = 2
Output : (1, 3, 9, 18)
Input : test_tup = (3, 7, 1), k=1
Output : (1, 3)
'''

class Tup:
    def __init__(self):
        pass
    def max_min(self,tup1,accu):
        lis=[]
        end=-accu
        for x in sorted(tup1):
            lis.append(x)
        tup2=tuple(lis[:accu]+lis[end:])
        print(tup2)
tup=Tup()
tup.max_min((3, 7, 1, 18, 9),2)