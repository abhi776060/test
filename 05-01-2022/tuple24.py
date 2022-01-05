# count the elements in a list until an element is a tuple
'''
num = [10,20,30,(10,20),40]
'''
class Tup:
    def __init__(self):
        pass

    def count_tuple(self,ele):
        for x in range(len(ele)):
            if type(ele[x]) is tuple:
                print(x)

tuple1=Tup()
tuple1.count_tuple([10,20,30,(10,20),40])