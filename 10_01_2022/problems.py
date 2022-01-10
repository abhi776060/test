'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]'''
def sum(num1,num2,num3,num4):
    a=num1 + num2 + num3+num4
    return a
def sum_four(arr,target):
    for x in range(len(arr)):
        for y in range(x,len(arr)):
            
                        
sum_four([10, 2, 3, 4, 5, 9, 7, 8],23)
