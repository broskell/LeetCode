class Solution(object):
    def minAddToMakeValid(self, s):
        start = 0
        end = 0

        for ch in s:
            if ch == '(':
                end += 1
            elif ch == ')':
                if end > 0:
                    end -= 1
                else:
                    start += 1           
        return start + end