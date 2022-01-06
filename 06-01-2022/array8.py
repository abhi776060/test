#Convert an array to an array of machine values and return the bytes representation
from array import *
class Array:
    def __init__(self):
        pass

    def convert_to_string(self,ele):
        array1=array('u')
        for x in ele:
            array1.append(chr(x))
        print(array1)

solution=Array()
solution.convert_to_string(array('i', [97,98,99,100,101,102,103]))