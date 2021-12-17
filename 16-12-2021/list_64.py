#Iterate over two lists simultaneously

class List:
    def __init__(self):
        pass
    def iterate(self,lis1,lis2):
        for x in range(len(lis1)):
            print(lis1[x],lis2[x])
me=List()
list1=[1,2,3,4,5]
list2=[5,6,8,9,7]
print(me.iterate(list1,list2))