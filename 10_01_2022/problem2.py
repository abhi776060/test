class Solution:
    def twoSum(self, nums: list, target: int):
        for x in range(len(nums)-1):
            if target==nums[x]+nums[x+1]:
                print(x,x+1)
solutions=Solution()
solutions.twoSum([3,2,4],6)