#Check circularly identical in two lists

class List:
    def __init__(self):
        pass

    def circular(self,lis,lis1):
        str1=''
        str2=''
        for x in lis:
            str1+=str(x)
        for x in lis1:
            str2+=str(x)
        str3=str1*2
        if str2 in str3:
            print("circular")
        else:
            print("not circular")


list1=List()

lst1 = [10, 10, 0, 0, 10]#10 10 0 0 10 10 10 0 0 10
lst2 = [10, 10, 10, 0, 0]
lst3 = [1, 10, 10, 0, 0]
list1.circular(lst1,lst3)


