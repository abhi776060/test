# Sum of tuple elements
'''
The original tuple is : (7, 8, 9, 1, 10, 7)
The summation of tuple elements are : 42
'''
class Tup:
    def __init__(self):
        pass

    def sum(self,tup1):
        tup_sum=0
        for x in tup1:
            tup_sum+=x
        print('The summation of tuple elements are :',tup_sum)


tup=Tup()
tup.sum((7, 8, 9, 1, 10, 7))