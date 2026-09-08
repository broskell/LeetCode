class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid_speed = (left + right) // 2

            total_hours = sum((pile + mid_speed - 1) // mid_speed for pile in piles)

            if total_hours <= h:
                result = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1
                
        return result