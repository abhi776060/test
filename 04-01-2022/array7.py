#Append items from inerrable to the end of the array
from array import array
class Array:
    def __init__(self):
        pass

    def reverse(self,seq,nums):
        for x in nums:
            seq.append(x)
        print(seq)

solution=Array()
solution.reverse(array('i',[1,2,3,4,5]),[1,2,3,5])