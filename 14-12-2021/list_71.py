#Check if all dictionaries in a list are empty or not i=[{},{},{}]
class List:
    def __init__(self):
        pass

    def empty_not(self,lis):
        lis1=[]
        for x in lis:
            if type(x) is dict:
                lis1.append(True)
            else:
                lis1.append(False)
        if all(lis1):
            return True
        else:
            return False
me=List()
print(me.empty_not([{},{}]))
