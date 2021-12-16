#check whether a number is in a given range
class Fuunction:
    def __init__(self):
        pass
    def check_range(self,n):
        if n in range(0,10):
            return f'{n} is present'
        return f'{n} is not present'
me=Fuunction()
print(me.check_range(10))