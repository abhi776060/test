'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
 reverse order, and each of their nodes contains a single digit. Add the two numbers and
 return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
class Leet:
    def __init__(self):
        pass

    def some(self,list1,list2):
        str1=''
        for x in reversed(list1):
            str1+=str(x)
        str2=''
        for x in reversed(list2):
            str2+=str(x)
        sum_of_two=int(str1)+int(str2)
        list3=[]
        for x in reversed(str(sum_of_two)):
            list3.append(int(x))
        print(list3)
solution=Leet()
solution.some([9,9,9,9,9,9,9],[9,9,9,9])