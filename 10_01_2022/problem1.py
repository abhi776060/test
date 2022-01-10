from itertools import combinations, permutations
def palindrome(str1):
    reverse=str1[::-1]
    if str1=='':
        return ' '
    if str1==reverse:
        return str1
    
    
# print(palindrome('')  )
    
def permutaion(str1):
    list1=[]
    list2=[]
    i=0
    for i in range(len(str1)+1):
        a=combinations(str1,i)
        
        for x in a:
            str2=''
            str2 = "".join(x)
            if palindrome(str2):
                list1.append(str2)
            else:
                list2.append(str2)
    print(list1)
permutaion('bab')
# a=combinations('bb',2)
