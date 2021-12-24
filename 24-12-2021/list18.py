#All permutations of list elements
import itertools
class List:

    def __init__(self):
        pass

    def permutation(self,lis):
        for x in range(1,len(lis)+1):
            print(list(itertools.permutations(lis,x)))
list1=List()
lis1=[1,2,3]
# lis1='asdd'
list1.permutation(lis1)
