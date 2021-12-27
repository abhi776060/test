#reverse a list
'''
Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]

Input : list = [4, 5, 6, 7, 8, 9]
Output : [9, 8, 7, 6, 5, 4]
'''

class List:
    def __init__(self):
        pass

    def reverse(self,lis):
        lis1=[]
        for x in reversed(sorted(range(len(lis)))):
            lis1.append(lis[x])
        print(lis1)

list1=List()
list1.reverse([10,11,12,13,14,15])
