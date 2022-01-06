#Remove a specified item using the index from an array.
from array import array
class Array:
    def __init__(self):
        pass

    def remove(self,sequence,index):
        d_type=sequence.typecode
        array1=array(d_type)
        for x in range(len(sequence)):
            if x == index:
                pass
            else:
                array1.append(sequence[x])
        print(array1)


solution=Array()
solution.remove(array("i",[1,2,3,4,5]),2)