#Append a new item to the end of the array.
from array import array
class Array:
    def __init__(self):
        pass

    def append(self,seq,num):
        seq=seq+array('i',[num])
        print(seq)
solution=Array()
solution.append(array('i',[1,2,3,4,5]),6)