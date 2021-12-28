'''
Write a Python program to reverse the order of the items in the array.
Sample Output
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('i', [3, 9, 1, 7, 3, 5, 3, 1])
'''
from array import *
class Array:
    def __init__(self):
        pass


    def reverse(self,array2):
        array3=array2.reverse()
        print()

array1=Array()
a=array('i', [1, 3, 5, 3, 7, 1, 9, 3])
array1.reverse(a)