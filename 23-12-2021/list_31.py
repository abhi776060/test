#Counting number elementswithin a specified ranges
class List:
    def __init__(self):
        pass

    def count1(self,lis,min, max):
        ctr = 0
        for x in lis:
            if min <=x or max<=x:
                ctr += 1
        print(ctr)

list1=List()
lst2 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list1.count1(lst2, 40, 100)

# list2 = ['a', 'b', 'c', 'd', 'e', 'f']
# list1.count1(lst2, 'a', 'e')
