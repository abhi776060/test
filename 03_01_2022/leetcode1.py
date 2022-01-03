'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Leet:
    def __init__(self):
        pass
    def find(self,list1,target):
        for x in range(0,len(list1)-1):
            for y in range(x+1,len(list1)):
                if list1[x]+list1[y]==target:
                    print(x,y)

solution=Leet()
solution.find([3,5,3],6)