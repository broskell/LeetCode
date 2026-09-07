import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            curSum = 0

            for num in nums:
                curSum += math.ceil(float(num) / mid)
            
            if curSum <= threshold:
                result = mid
                right = mid - 1
            else: left = mid + 1
        return result