#Append items from a specified list.
from array import array
class Array:
    def __init__(self):
        pass

    def append_to_specified_type(self,sequence,datatyp):
        array1=array(datatyp)
        for x in sequence:
            array1.append(x)
        print(array1)

solution=Array()
solution.append_to_specified_type([1,2,3,4,5,8],'i')