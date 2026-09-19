class Solution(object):
    def longestConsecutive(self, nums):
        unique, longest = set(nums), 0

        for num in unique:
            if num - 1 not in unique:
                curNum = num
                streak = 1
                while curNum + 1 in unique:
                    streak += 1
                    curNum += 1
                longest = max(longest, streak)
        return longest