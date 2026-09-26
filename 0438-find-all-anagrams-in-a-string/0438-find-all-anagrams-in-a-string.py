class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        c1, c2 = [0] * 26, [0] * 26
        result = []

        for i in range(0, len(p), +1):
            c1[ord(p[i]) - ord('a')] += 1
            c2[ord(s[i]) - ord('a')] += 1
        
        if c1 == c2:
            result.append(0)

        for i in range(len(p), len(s), +1):
            c2[ord(s[i]) - ord('a')] += 1
            c2[ord(s[i - len(p)]) - ord('a')] -= 1
            if c1 == c2:
                result.append(i - len(p) + 1)
        return result