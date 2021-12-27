#Ways to remove i’th character from string in Python
'''
The original string is : GeeksForGeeks
The string after removal of i'th character( doesn't work) : GksForGks
The string after removal of i'th character(works) : GeekForGeeks
'''
class String:
    def __init__(self):
        pass

    def remove(self,str1,ele):
        str2=''
        for x in str1:
            if x == ele:
                pass
            else:
                str2+=x
        print(str2)

string=String()
string.remove('Geeksforgeeks','e')