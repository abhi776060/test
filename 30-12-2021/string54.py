#find the first repeated character of a given string where the index of first occurrence is smallest
'''
abcabc---('a', 0)
"abcb"---('b', 1)
"abcc"----('c', 2)
"abcxxy"----('x', 3)
"abc"---None
'''
class String:
    def __init__(self):
        pass
    def tostring(self,str1):
        list1=[]
        dict1={}
        for x in str1:
            if x not in list1:
                list1.append(x)
            else:
                i=str1.index(x)
                dict1[str1[i]]=i
        # print(list1)
        print(dict1)

string1=String()
string1.tostring('abc')