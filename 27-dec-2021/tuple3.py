#Python program to create a list of tuples from given list having number and its cube in each tuple

'''
Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''
class Tup:
    def __init__(self):
        pass

    def lis_of_tuple(self,lis):
        lis1=[]
        for x in lis:
            lis1.append((x,x**3))
        print(lis1)


tup=Tup()
tup.lis_of_tuple([1, 2, 3])