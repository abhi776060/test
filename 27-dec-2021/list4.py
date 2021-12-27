# find negative numver in a list

'''
Input: list1 = [12, -7, 5, 64, -14]
Output: -7, -14

Input: list2 = [12, 14, -95, 3]
Output: -95
'''
class List:
    def __init__(self):
        pass

    def find(self,lis):
        lis1=[]
        for x in lis:
            if x<0:
                lis1.append(x)
        print(lis1)

list1=List()
list1.find([12, -7, 5, 64, -14])