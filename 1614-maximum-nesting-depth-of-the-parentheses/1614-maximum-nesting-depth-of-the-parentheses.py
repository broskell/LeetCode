class Solution(object):
    def maxDepth(self, s):
        count, maxCount = 0, 0

        for ch in s:
            if ch == '(':
                count += 1
                maxCount = max(maxCount, count)
            elif ch == ')':
                count -= 1
        return maxCount