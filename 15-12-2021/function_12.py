#to reverse a string
class Fuunction:
    def __init__(self):
        pass
    def check_range(self,str1):
        str2=''
        for x in str1:
            str2=x+str2
        return str2
me=Fuunction()
print(me.check_range('abhishek'))