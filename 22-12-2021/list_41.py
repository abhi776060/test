#Create multiple list

class List:
    def __init__(self):
        pass

    def create(self,lis):
        dict1={}
        for x in range(lis):
            dict1[x+1]=[]
        print(dict1)



list1=List()
list1.create(5)