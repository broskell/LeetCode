class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            
            curSum = sum((num + mid - 1) // mid for num in nums)
            
            if curSum <= threshold:
                result = mid
                right = mid - 1
            else: left = mid + 1
        return result