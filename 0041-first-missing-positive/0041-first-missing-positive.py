class Solution(object):
    def firstMissingPositive(self, nums):
        unique = set(nums)
        missing = 1

        for i in range(0, len(nums) + 1, +1):
            if missing not in unique:
                return missing
            missing += 1