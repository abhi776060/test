#Check if all items of a list is equal to a given string
class List:
    def __init__(self,l):
        self.l=l

    def check(self,str1):
        str2=''
        for x in self.l:
            str2=str2+x
        if str1==str2:
            print("True")
        else:
            print("Fasle")

lis1=['a','b','h','i']
list1=List(lis1)
list1.check('abhi')