class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = sorted(num * num for num in nums)
        k = len(nums) // 2
        return sum(squares[k:]) - sum(squares[:k])