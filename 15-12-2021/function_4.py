#factorial of given number

class Function:
    def __init__(self):
        pass
    def facto(self,num):
        if num<=0:
            return 0
        elif num==1:
            return 1 #returning one if entered value is equal to one
        else:
            n=2
            for x in range(2,num):
                n=(x+1)*n
            print(n)
me=Function()
print(me.facto(6))