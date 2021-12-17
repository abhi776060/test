#Print a list of space-separated elements
class List:
    def __init__(self):
        pass
    def space_separated(self,lis):
        str1=''
        for x in lis:
            str1=str1+str(x)+' '
        return str1

me=List()
print(me.space_separated([1,2,3,4]))

