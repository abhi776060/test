#Python program to check whether the string is Palindrome

'''
Input: khokho
Output:

The entered string is not palindrome

Input:amaama
Output:

The entered string is palindrome
'''

class List:

    def __init__(self):
        pass

    def check(self,lis):
        mid=len(lis)//2
        start=0
        end=len(lis)-1
        flag=0
        while start<=mid:
            if lis[start]==lis[end]:
                start+=1
                end-=1
            else:
                flag=1
                break

        if flag==0:
            print("entered sring is palindrome")
        else:
            print("enterd string is not palindrome")

list1=List()
list1.check('amaama')