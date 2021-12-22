#Convert a pair of values into a sorted unique array
class List:
    def __init__(self):
        pass

    def convert(self,lis):
        lis1=set()
        for x in lis:
            for y in x:
                lis1.add(y)
        print(list(lis1))


list1=List()
lis1=[(1, 5), (3, 4), (1, 5), (5, 6), (7, 8), (1, 9), (3, 4), (3, 4), (7, 8), (9, 10)]
list1.convert(lis1)