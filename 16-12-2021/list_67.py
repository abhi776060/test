#Find all the values in a list are greater than a specified number

class List:
    def __init__(self,lis):
        self.lis=lis
    def greater(self,n):
        for x in self.lis:
            if n >x:
                return True
            return False

me=List([8,5,6,9])
print(me.greater(9))