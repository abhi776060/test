#Convert an array to an ordinary list with the same items.
from array import array
class Array:
    def __init__(self):
        pass

    def convert_lst(self,array_sequenc):
        list1=[]
        for x in array_sequenc:
            list1.append(x)
        print(list1)
solution=Array()
solution.convert_lst(array('i',[1,2,3,4,5]))