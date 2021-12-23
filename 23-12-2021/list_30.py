#Frequency of elements

class List:
    def __init__(self,lis):
        self.lis=lis

    def frequency(self):
        dict1={}
        for x in self.lis:
            if x not in dict1:
                dict1[x]=1
            else:
                dict1[x]+=1
        print(dict1)

list1=List([1,5,1,8,2,3,6,7,6])
list1.frequency()