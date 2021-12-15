#Two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j
class List:
    def __init__(self):
        pass

    def two_array(self,lis):
        lis1=[]
        for x in range(1,lis[0]+1):
            lis2=[]
            for y in range(1,lis[1]+1):
                lis2.append(x*y)
            lis1.append(lis2)
        return lis1
me=List()
print(me.two_array([5,5]))
