'''
Input: [1, 2, 3]
Output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
class List:
    def __init__(self):
        pass

    def comb(self,lis):
        lis1=[]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if x!=y and y!=z and z!=x:
                        lis1.append((lis[x],lis[y],lis[z]))
        print(lis1)


list1=List()
list1.comb([1,2,3])