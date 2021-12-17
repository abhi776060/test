#Access dictionary keys element by index
class List:
    def __init__(self,dict1):
        self.dict1=dict1
    def access_dict_index(self,n):
        lis=list(self.dict1.keys())
        if n <len(lis):
            return lis[n]
        else:
            return " please provide valid index"


me=List({'key1':1,'key2':2,'key3':3})
print(me.access_dict_index(2))