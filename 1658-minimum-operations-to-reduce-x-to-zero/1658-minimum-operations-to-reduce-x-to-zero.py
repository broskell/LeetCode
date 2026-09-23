class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        l = 0
        max_length = -1
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                max_length = max(max_length, r - l + 1)     

        if max_length == -1:
            return -1

        return len(nums) - max_length