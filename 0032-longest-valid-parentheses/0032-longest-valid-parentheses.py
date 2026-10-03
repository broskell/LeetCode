class Solution(object):
    def longestValidParentheses(self, s):
        left = right = maxCount = 0

        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxCount = max(maxCount, 2 * right)
            elif right > left:
                right = left = 0
        
        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxCount = max(maxCount, 2 * left)
            elif left > right:
                right = left = 0

        return maxCount