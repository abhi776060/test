class Sum():
    def sum(self,list1):
        total=0
        for x in list1:
            total+=x
        return total

me=Sum()
list1=[1,2,4,2,4]
print(me.sum(list1))