#Reverse each word and reverse word again. Input
'''
Input : Split Reverse Join
Output : tilpS esreveR nioJ
'''
class String:
    def __init__(self):
        pass
    def reverse(self,str1):
        list2=[]
        list1=str1.split(" ")
        for x in list1:
            str2=''
            for y in x:
                str2=y+str2
            list2.append(str2)
        str3=''
        for x in list2:
            str3=x+" "+str3
        print(str1)
        print(str3)
string1=String()
string1.reverse("Split Reverse Join")