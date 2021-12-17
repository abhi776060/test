#Extend a list without append

class List:
    def __init__(self,lis):
        self.lis=lis
    def new_append(self,n):
        n1=str(n)
        for x in n1:
            self.lis.append(int(x))
        return self.lis
me=List([1,2,3,4])
print(me.new_append(2))