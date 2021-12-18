#Compute the similarity between two lists

class List:
    def __init__(self):
        pass

    def compare(self,lis1,lis2):
        i=False
        for x in range(len(lis1)):
            if lis1[x]==lis2[x]:
                i=True
            else:
                i=False
        print(i)
list1=List()
list1.compare([1,2,3],[1,2,8])