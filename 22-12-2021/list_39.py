#Converting multiple integers into single integer
class List:
    def __init__(self):
        pass

    def convert(self,lis):
        l=''
        for x in lis:
            l+=str(x)
        print(int(l))


list1=List()
list1.convert([10,15,78])