#Create a list by concatenating a given list which range goes from 1 to n

class List:
    def __init__(self):
        pass

    def con(self,lis,n):
        lis1=[]
        i=0
        while True:
            if i >=n:
                break
            else:
                for x in lis:
                    lis1.append(f'{x}{i+1}')
                i += 1
        print(lis1)

list1=List()
list1.con(['p','q'],10)