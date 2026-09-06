class Solution(object):
    def triangularSum(self, nums):
        while len(nums) > 1:
            curList = []
            for i in range(0, len(nums) - 1, +1):
                curList.append((nums[i] + nums[i + 1]) % 10)
            nums = curList
        return nums[0]