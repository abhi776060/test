#Finding a second largest number

class List:
    def __init__(self):
        pass

    def sec_large(self,lis):
        lis2=[]
        for x in sorted(lis):
            lis2.append(x)
        print(f'second largest number is {lis2[-2]}')




list1=List()
list1.sec_large([8,5,6,9,1,8,5,7,8,2])