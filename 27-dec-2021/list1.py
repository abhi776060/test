#Python program to swap two elements in a list
'''
Input : List = [23, 65, 19, 90], pos1 = 0, pos2 = 2
Output : [19, 65, 23, 90]
'''
class List:
    def __init__(self,lis):
        self.lis=lis

    def swap(self,elm1,elm2):
        a = self.lis[elm1]
        b = self.lis[elm2]
        self.lis[elm1]=b
        self.lis[elm2]=a
        print(self.lis)

list1=List([23, 65, 19, 90])
list1.swap(0,2)
