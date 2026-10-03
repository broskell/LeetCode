class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        maxCount = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxCount = max(maxCount, i - stack[-1])
        return maxCount