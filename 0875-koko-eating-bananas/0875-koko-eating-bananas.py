class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            totalHrs = 0

            for pile in piles:
                totalHrs += (pile + mid - 1) // mid

            if totalHrs <= h:
                right = mid  - 1
            else: 
                left = mid + 1
        return left