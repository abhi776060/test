#Append items from inerrable to the end of the array
from array import array
class Array:
    def __init__(self):
        pass

    def append(self,array1):
        array1.extend(array1)
        print(array1)

solution=Array()
solution.append(array('i',[1,2,3,4,5]))