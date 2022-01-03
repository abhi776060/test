#get the nth element and nth element from list of a tuple
class Tup:
    def __init__(self):
        pass

    def index(self,tuple1,num):
        for x in range(len(tuple1)):
            if x ==num:
                print(tuple1[x])

tup1=Tup()

tup1.index((1,2,3,4,5),1)
