class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(0, len(nums), +1):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                correctIndex = nums[i] - 1
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        
        for i in range(0, len(nums), +1):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1