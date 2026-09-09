class Solution(object):
    def reverseString(self, s):
        for i in range(0, len(s) // 2, + 1):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return s