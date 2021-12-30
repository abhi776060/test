#Swapping chars in string
'''
s = "geeksforgeeks" e--k
"gkkksforgkkks"


'''
class String:
    def __init__(self):
        pass

    def swap(self,str1,f1,f2):
        str2=''
        for x in str1:
            if x==f1:
                str2+=f2
            else:
                str2+=x
        print(str2)
string1=String()
string1.swap("geeksforgeeks",'e','k')