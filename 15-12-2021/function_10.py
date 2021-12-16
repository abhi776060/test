# sum all the numbers in a list
class Fuunction:
    def __init__(self):
        pass
    def summ(self,lis1):
        num=0
        for x in lis1:
            num+=x
        return num
me=Fuunction()
print(me.summ([1,2,3,4,5,6]))