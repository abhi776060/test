# Avoid Spaces in string length
'''
Input : test_str = ‘geeksforgeeks 33 best’
Output : 19
Explanation : Total characters are 19.
'''
class String:
    def __init__(self):
        pass

    def avoid(self,str1):
        count=0
        for x in str1:
            if x ==" ":
                pass
            else:
                count+=1

        print(count)

string=String()
string.avoid('geeksforgeeks 33 best')
