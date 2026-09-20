class Solution(object):
    def reverseDegree(self, s):
        reverseDegree = 0

        for i in range(0, len(s), 1):
            reverseDegree += (123 - ord(s[i])) * (i + 1)   
        return reverseDegree