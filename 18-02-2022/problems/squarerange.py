import math
def squares(a, b):
    # Write your code here
    a1=int(math.sqrt(a))
    b1=int(math.sqrt(b))+2
    range_list=[x*x for x in range(a1,b1) if x*x >=a and x*x<=b ]
    print(range_list)
    if range_list:
        return len(range_list)
    else:
        return 0
    
# squares(24,49)
# squares(3,9)
# squares(17,24)
# print(squares(35,70))
print(squares(100,1000))