'''
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''

lis1= [1,2,3,4,7,8,5]
lis3=[]
if len(lis1)%2==0:
    for x in range(0,len(lis1)-1,2):
        lis3.append(lis1[x+1])
        lis3.append(lis1[x])

elif len(lis1)==0:
    lis3.append([])
else:
    for x in range(0, len(lis1) - 1, 2):
        lis3.append(lis1[x + 1])
        lis3.append(lis1[x])
    lis3.append(lis1[-1])


print(lis3)