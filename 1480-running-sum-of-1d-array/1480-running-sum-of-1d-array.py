class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums), +1):
            nums[i] += nums[i - 1]
        return nums