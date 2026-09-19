class Solution(object):
    def longestConsecutive(self, nums):
        unique, longest = set(nums), 0

        for num in unique:
            if num - 1 not in unique:
                streak = 1
                while num + streak in unique:
                    streak += 1
                longest = max(longest, streak)
        return longest