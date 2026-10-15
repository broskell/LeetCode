class Solution(object):
    def sumCounts(self, nums):
        count = 0

        for i in range(0, len(nums), +1):
            distinct = set()
            for j in range(i, len(nums), +1):
                distinct.add(nums[j])
                count += len(distinct) ** 2
        return count