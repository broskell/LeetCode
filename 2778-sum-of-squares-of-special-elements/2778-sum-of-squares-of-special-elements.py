class Solution(object):
    def sumOfSquares(self, nums):
        sqaureSum = 0

        for i, num in enumerate(nums):
            if len(nums) % (i + 1) == 0:
                sqaureSum += (num * num)
        return sqaureSum