#Find missing and additional values

class List:
    def __init__(self):
        pass

    def find(self,lis3,lis4):
        missing_list=[]
        for x in lis3:
            if x not in lis4:
                missing_list.append(x)
        additional_list=[]
        for x in lis4:
            if x not in lis3 and x not in missing_list:
                additional_list.append(x)
        print('missing elements',missing_list)
        print('additional elements', additional_list)

list1=List()
lis1 = ['a','b','c','d','e','f']
lis2 = ['d','e','f','g','h']
list1.find(lis1,lis2)