#Create an array of 5 integers and display the array items. Access individual element through indexes.
from array import array
class Array:
    def __init__(self):
        pass

    def create(self,ele1,ele2):
        array1=array(ele1,ele2)
        print(array1)
        print(type(array1))

solution=Array()
datatype=input(" enter int or str or float ").lower()
if datatype=='int':
    datatype="i"
    dt=int
elif datatype=='float':
    datatype="f"
    dt = float
else:
    datatype="u"
    dt = str
data=input(f"enter only {datatype}").split(',')
data1=list(map(dt,data))
print(data1)
solution.create(datatype,data1)