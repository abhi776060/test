#Sort a list of nested dictionaries
class List():
    def __init__(self):
        pass

    def sort(self,lis):
        dict2={}
        for x,y in lis.items():
            dict3={}
            for i,j in sorted(y.items()):
                dict3[i]=j
            dict2[x]=dict3
        print(dict2)

list1=List()
list1.sort({5: {7:51, 6:68},
            1: {6:89, 1:59}})