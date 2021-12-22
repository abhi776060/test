#Print a nested lists (each list on a new line) using the print() function

class List:
    def __init__(self):
        pass

    def nested(self,lis):
        for x in lis:
            print(x)

list1=List()
list1.nested([['Red'], ['Green'], ['Black']])