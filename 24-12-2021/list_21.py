#List of characters into string

class List:

    def __init__(self):
        pass

    def murge(self,lis):
        str1=''
        for x in lis:
            str1+=x

        print(str1)

list1=List()
list1.murge(['a','b','h','i'])