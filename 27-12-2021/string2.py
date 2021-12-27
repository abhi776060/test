#Python program to check whether the string is Symmetrical

'''
Input: khokho
Output:
The entered string is symmetrical

Input:amaama
Output:
The entered string is symmetrical

'''

class List:
    def __init__(self):
        pass

    def check(self,lis):
        n=len(lis)
        flag=0
        if n%2==0:
            mid= n // 2

        else:
            mid=n // 2+1
        start=0
        end=mid
        while start< mid and end <n:
            if lis[start]==lis[end]:
                start+=1
                end+=1
            else:
                flag=1
                break
        if flag == 0:
            print("entered string is symetric")
        else:
            print("entered string is not symetric")



list1=List()
list1.check('khokho')