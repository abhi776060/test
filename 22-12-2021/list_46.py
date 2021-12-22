#Slect odd items of a list

class List:
    def __init__(selfself):
        pass

    def odd(self,lis):
        lis1=[]
        for i in lis:
            if i%2 !=0:
                lis1.append(i)
        print(lis1)

list1=List()
list1.odd( [1, 2, 3, 4, 5, 6, 7, 8, 9])