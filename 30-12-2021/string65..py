#Reverse each word in given string Input
'''
Input : Hello World
Output : olleH dlroW
'''
class String:
    def __init__(self):
        pass

    def reverse(self,str1):
        list1=str1.split(" ")
        list2 = []
        for x in list1:
            str2=''
            for y in x:
                str2=y+str2
            list2.append(str2)
        str3=''
        for x in list2:
            str3+=x+" "
        print(str3)

string1=String()
string1.reverse("Hello World")