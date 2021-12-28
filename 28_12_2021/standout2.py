'''
The original list is : [‘geekforgeeks’, [5, 4, 3, 4], ‘is’, [‘best’, ‘good’, ‘better’, ‘average’]]

All index Combinations : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’, ‘good’],
                            [‘geekforgeeks’, 3, ‘is’, ‘better’], [‘geekforgeeks’, 4, ‘is’, ‘average’]]
'''
class List:
    def __init__(self):
        pass
    def combine(self,lis):
        lis1=[]
        initial = 0
        length=len(lis)
        while initial <length-1:
            lis2=[]
            for x in lis:
                if type(x) is not list:
                    lis2.append(x)
                else:
                    lis2.append(x[initial])
            initial+=1
            lis1.append(lis2)
        print(lis1)

list1=List()
list1.combine(['geekforgeeks', [5, 4, 3, 4], 'is', ['best', 'good', 'better', 'average']])