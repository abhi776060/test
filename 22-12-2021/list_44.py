#Generate group of five consecutive numbers in a list

class List:
    def __init__(self):
        pass

    def generate(self,lis):
        lis2=[]
        lis3=[]
        lis4=[]
        for x in range(len(lis)):
            i=len(lis)
            if x < 5:
                lis2.append(lis[x])
            elif x <10:
                lis3.append(lis[x])
            else:
                lis4.append(lis[x])
        print(lis2,lis3,lis4)
list1=List()
lis1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list1.generate(lis1)