class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, result, total = 0, float('inf'), 0

        for right, num in enumerate(nums):
            total += num

            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        if result == float('inf'):
            return 0
        else:
            return result