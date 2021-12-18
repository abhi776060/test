#Split a list every Nth element

class List:
    def __init__(self,lis):
        self.lis=lis

    def split_list(self,n):
        lis1=[]
        lis2=[]
        for x in range(len(self.lis)):
            if x<=n:
                lis1.append(self.lis[x])
            else:
                lis2.append(self.lis[x])
        print(lis1,lis2)
list2=[1,2,3,4]
list1=List(list2)
list1.split_list(2)