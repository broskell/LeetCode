class Solution(object):
    def sortedSquares(self, nums):
        for i in range(0, len(nums), +1):
            nums[i] = nums[i] * nums[i]
        
        return sorted(nums)