#print the even numbers from a given list
class Function:
    def __init__(self):
        pass
    def even(self,lis1):
        for x in lis1:
            if x%2==0:
                print(x)
me=Function()
lis1=[1,2,3,4,5,6,7,8]
print(me.even(lis1))