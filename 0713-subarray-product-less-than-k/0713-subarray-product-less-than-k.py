class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        count, pdt, left = 0, 1, 0

        for right in range(0, len(nums), +1):
            pdt *= nums[right]

            while pdt >= k:
                pdt //= nums[left]
                left += 1
            
            count += (right - left + 1)
        return count