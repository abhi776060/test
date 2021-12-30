#Append chars to string at end

'''
"geeksforgeeks" y
"geeksforgeeksy"
'''
class String:
    def __init__(self):
        pass
    def append(self,str1,chr1):
        str1=str1+chr1[0]
        print(str1)

string1=String()
string1.append("geeksforgeeks","yc")