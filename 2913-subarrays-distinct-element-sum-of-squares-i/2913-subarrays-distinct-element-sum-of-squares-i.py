class Solution(object):
    def sumCounts(self, nums):
        count = 0

        for i in range(0, len(nums), +1):
            for j in range(0, len(nums), +1):
                distinct = set(nums[i:j+1])
                count += len(distinct) ** 2
        return count