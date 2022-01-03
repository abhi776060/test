#count repeated characters in a string
'''
Input : N = 10 str = "abcac"
Output : 4
Explanation: "abcacabcac" is the substring from the infinitely repeated string. In first 10 letters 'a' occurs 4  times.

Input: N = 10, str = "aba"
Output : 7
'''

class String:
    def __init__(self):
        pass

    def cunt(self,str1,repeatlimit):
        list1=[str1[x] for x in range(len(str1))]*repeatlimit
        str2=''
        for x in list1:
            if len(str2)<repeatlimit:
                str2+=x
        count=0
        for x in str2:
            if x== str2[0]:
                count+=1
        print(count)

string1=String()
string1.cunt("aba",10)