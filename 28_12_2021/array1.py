#Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.
'''
Sample Output:
1
3
5
7
9
Access first three items individually
1
3
5

'''
from array import *
class Array:
    def __init__(self):
        pass

    def create(self,nums):
        array_num=list(map(int,nums.split(' ')))
        newarray=array('i',array_num)
        print(newarray)


array1=Array()
x=input("enter integer data types seperated by white space: ")
array1.create(x)