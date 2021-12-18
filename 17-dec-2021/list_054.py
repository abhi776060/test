#Concatenate elements of a list
class List:
    def __init__(self):
        pass

    def concat(self,lis):
        add=0
        for x in lis:
            add+=x
        print(add)

list1=List()
list1.concat([1,2,3,4,5,8])