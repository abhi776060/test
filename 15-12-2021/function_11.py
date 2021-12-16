#multiply all the numbers in a list
class Fuunction:
    def __init__(self):
        pass
    def multy(self,lis1):
        num=1
        for x in lis1:
            num*=x
        return num
me=Fuunction()
print(me.multy([1,2,3,4,5,6]))