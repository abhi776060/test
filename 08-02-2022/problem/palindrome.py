from itertools import  permutations
def check(str1):
    str2=str1[::-1]
    if str1==str2:
        return True
    else:
        return False
def palindrome(str1):
    v=permutations(str1,len(str1))
    list1=[]
    for x in v:
        str2=''
        for y in x:
            str2+=y
        new=check(str2)
        if new:
            if str2 not in list1:
                list1.append(str2)
    if list1:
        print(max(list1))
    else:
        print(-1)
palindrome('388003')