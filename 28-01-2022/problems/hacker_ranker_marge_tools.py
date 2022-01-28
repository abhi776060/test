'''
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
'''
def marge_tools(str1,group):
    list1=[]
    for x in range(0,len(str1),group):
        list1.append(''.join(set(str1[x:x+group])))
    print(list1)

marge_tools('AABCAAADA',3)