class Mul():
    def mul(self,list1):
        total=1
        for x in list1:
            total*=x
        return total

me=Mul()
list1=[1,2,4,2,4]
print(me.mul(list1))