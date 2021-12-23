#Variable unique identification number

class List:
    def __init__(self):
        pass

    def identy(self,lis):
        for x in range(len(lis)):
            print(id(lis[x]),f'{lis[x]}')
        print(id(lis),f'{lis}')

list1=List()
list1.identy([1,2,3,4])