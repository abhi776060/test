
from cmath import e
from itertools import count


def equalizeArray(arr):
    # Write your code here
    dict1={}
    max_len=len(arr)
    for  x in arr:
        dict1[x]=arr.count(x)

    max_acc=max(dict1.values())

    
    print(abs(max_acc-max_len))
# equalizeArray([1,2,3,1,2,3,3,3])
# equalizeArray([1,2,2,3])
equalizeArray([37,32,97,35,76,62])
# equalizeArray([3, 3, 2, 1, 3])