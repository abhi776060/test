'''
 Write a Python program to append a new item to the end of the array
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])
'''
from array import *
class Array:
    def __init__(self,a_array):
        self.a_array=a_array

    def add(self,num):
        self.a_array.append(num)
        print(self.a_array)
a=array("i",[1,3,5,7,9])
array1=Array(a)
array1.add(11)
