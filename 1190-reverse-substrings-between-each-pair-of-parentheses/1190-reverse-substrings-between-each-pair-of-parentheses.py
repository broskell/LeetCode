class Solution(object):
    def reverseParentheses(self, s):
        stack, ans = [], ""

        for ch in s:
            if ch == '(':
                stack.append(ans)
                ans = ''
            elif ch == ')':
                ans = ans[::-1]
                ans = stack.pop() + ans
            else:
                ans += ch
        return ans