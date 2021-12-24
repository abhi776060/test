#Finding a second smallest number

class List:
    def __init__(self):
        pass

    def sec_smallest(self,lis):
        lis2=[]
        for x in sorted(lis):
            lis2.append(x)
        print(f'second largest number is {lis2[1]}')




list1=List()
list1.sec_smallest([8,5,6,9,1,8,5,7,8,2])