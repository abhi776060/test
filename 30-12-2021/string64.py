#Reverse a given string  Input : "Python"   Output : "nohtyP"
'''
"abcdef"----fedcba
"Python Exercises."---.sesicrexE nohtyP

'''
class String:
    def __init__(self):
        pass

    def reverse(self,str1):
        str2=''
        for x in str1:
            str2=x+str2
        print(str2)

string1=String()
string1.reverse("abcdef")