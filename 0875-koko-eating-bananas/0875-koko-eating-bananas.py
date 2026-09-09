class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        output = float('inf')

        while left <= right:
            mid = (left + right) // 2
            totalHrs = sum((pile + mid - 1) // mid for pile in piles)

            if totalHrs <= h:
                output = mid
                right = mid  - 1
            else: left = mid + 1
        return output