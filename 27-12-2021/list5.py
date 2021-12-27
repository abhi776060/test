# find positive and negative number accurence

'''
Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Input: list2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1
'''

class List:
    def __init__(self):
        pass

    def find(self,lis):
        positive=0
        negative=0
        for x in lis:
            if x<0:
                negative+=1
            else:
                positive+=1
        print("positive",positive)
        print("negative",negative)


list1=List()
list1.find([2, -7, 5, -64, -14])