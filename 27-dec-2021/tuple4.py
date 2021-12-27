#Adding Tuple to List and vice – versa
'''
The original list is : [5, 6, 7]
test_tup = (9, 10)
The container after addition : (9, 10, 5, 6, 7)
list=tuple+list
'''
class Tup:
    def __init__(self):
        pass
    def add(self,lis,tup1):
        lis=lis+list(tup1)
        print(lis)
tup=Tup()
tup.add([5, 6, 7],(9, 10))