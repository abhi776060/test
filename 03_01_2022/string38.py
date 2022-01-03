#to count occurrences of a substring in a string
'''
Input : man (pattern)
        dhimanman (string)
Output : 2
'''
class String:
    def __init__(self):
        pass

    def count(self,str1,str2):
        index_char=len(str2)
        first_char=str2[0]
        count=0
        for x in range(len(str1)):
            if str1[x] == first_char:
                if str1[x:x+index_char] ==str2:
                    count+=1
        print(count)

string1=String()
string1.count('aaaaa','aa')