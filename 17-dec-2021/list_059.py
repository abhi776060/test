#Check if the n-th element exists in a given list

class List:
    def __init__(self,list1):
        self.list1=list1

    def present(self,n):
        if n in self.list1:
            print("present")
        else:
            print("not present")

lis=list(range(10))

list1=List(lis)
list1.present(50)