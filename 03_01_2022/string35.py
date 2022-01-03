#to display a number with a comma separator for non negative numbers

'''
input: 30554561----3,05,54,561
'''
class String:
    def __init__(self):
        pass

    def display(self,str1):
        i=len(str1)
        str2=''
        list1=[]
        if i%2==0:
            for x in range(len(str1)):
                if x%2==0:
                    list1.append(str1[x])
                    if x <i-3:
                        list1.append(',')
                else:
                    list1.append(str1[x])
            for x in list1:
                str2+=x
        else:
            for x in range(len(str1)):
                if x % 2 != 0:
                    list1.append(str1[x])
                    if x < i-3:
                        list1.append(',')
                else:
                    list1.append(str1[x])
            for x in list1:
                str2 += x
        print(str2)

string1=String()
string1.display('93056984865584561')




