class Solution(object):
    def findMaxAverage(self, nums, k):
        curSum = sum(nums[:k])
        maxSum = curSum

        for i in range(k, len(nums), +1):
            curSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, curSum)
        return float(maxSum) / k