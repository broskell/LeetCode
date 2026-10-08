class Solution(object):
    def removeOuterParentheses(self, s):
        output, start = [], 0
        for ch in s:
            if ch == "(":
                if start > 0:
                    output.append(ch)
                start += 1
            else:
                start -= 1
                if start > 0:
                    output.append(ch)
        return "".join(output)