# create a tuple.

class Tup:
    def __init__(self):
        pass

    def create(self,str1):
        list1=[]
        str2 = list(map(str, str1.split(',')))
        for x in str2:
            list1.append(x)
        print(list1)
tuple1=Tup()
user=input("enter a tuple values with comma-seprate symbols :")
tuple1.create(user)