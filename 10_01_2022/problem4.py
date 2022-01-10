'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
'''
def sum(num1,num2,num3):
    if num1 + num2 +num3 ==0:
        return [num1,num2,num3]



def sum_threepoint(arr):
    if len(arr) < 2:
        print([])
    else:
        list1=[]
        for x in range(len(arr)-2):

            init=arr[0]
            a=sum(init,arr[x+1],arr[x+2])
            if a:
                list1.append(a)
        print(list1)
sum_threepoint( [-1,0,1,2,-1,-4])
            

