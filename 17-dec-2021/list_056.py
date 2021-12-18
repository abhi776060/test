#Convert a string to a list

class List:
    def __init__(self):
        pass

    def get_list(self,str1):
        lis1=[]
        for x in str1:
            lis1.append(x)
        print(lis1)

list1=List()
list1.get_list('abhi')