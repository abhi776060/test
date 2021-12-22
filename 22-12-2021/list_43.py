#Split a list into different variables or unpackin

class List:
    def __init__(self):
        pass

    def split(self,lis):

        for x in range(len(lis)):
            print(f'x{x+1}',lis[x])

list1=List()
list1.split([1,2,3,7])