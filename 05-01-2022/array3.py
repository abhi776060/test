#Reverse the order of the items in the array.
from array import array
class array:
    def __init__(self):
        pass

    def reverse(self,seq):
        array2=array('i')
        for x in range(len(seq),0,-1):
            array2.append(x)
        print(array2)

solution=array()
solution.reverse(array('i',[1,2,3,4,5]))