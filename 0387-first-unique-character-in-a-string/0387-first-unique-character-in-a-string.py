class Solution(object):
    def firstUniqChar(self, s):
        for i in range(0, len(s), +1):
            if s[i] not in s[:i]:
                if s[i] not in s[i + 1:]:
                    return i
        return -1