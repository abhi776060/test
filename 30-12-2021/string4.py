#Replace first occurance character

'''
Input : test_str = 'geeksforgeeksforgeeks', K = '@'
Output : geeksfor@eeksfor@eeks
'''

class String:
    def __init__(self):
        pass

    def replace(self,str1,k):
        str2=''
        b=str1[0]
        for x in str1[1:]:
            if x==b:
                str2+=k
            else:
                str2+=x
        str3=b+str2
        print(str1)
        print(str3)


string1=String()
string1.replace("geeksforgeeksforgeeks",'@')