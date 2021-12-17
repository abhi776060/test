#Insert a given string at the beginning of all items in a list
class List:
    def __init__(self,lis):
        self.lis=lis
    def insert_begin(self,str1):
        l=[]
        l.append(str1)
        for x in self.lis:
            l.append(x)
        return l
list1=[1,2,3,4]
me=List(list1)
print(me.insert_begin('abhi'))