'''
Given an array arr[] of size, N. Find the subarray with maximum XOR. A subarray is a contiguous part of the array.


Example 1:

Input:
N = 4
arr[] = {1,2,3,4}
Output: 7
Explanation: 
The subarray {3,4} has maximum xor 
value equal to 7.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSubarrayXOR() which takes the array arr[], its size N as input parameters and returns the maximum xor of any subarray.
 
'''
def max_xor(list1):
    list2=[]
    for x in list1:
        for y in list1:
            list2.append((x^y))
    print(max(list2))

max_xor([25, 10, 2, 8, 5, 3])