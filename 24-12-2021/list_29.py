#Get unique values

class List:
    def __init__(self):
        pass

    def uniq(self,lis):
        lis1=[]
        for x in lis:
            if x not in lis1:
                lis1.append(x)
            else:
                pass

        print(lis1)


list1=List()
list1.uniq([1,2,3,5,7,6,2,4,5,8,9])