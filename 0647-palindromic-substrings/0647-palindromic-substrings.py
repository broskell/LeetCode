class Solution(object):
    def countSubstrings(self, s):
        count = 0

        for i in range(0, len(s), +1):
            for j in range(i + 1, len(s) + 1, +1):
                palindrome = s[i:j]
                if palindrome == palindrome[::-1]:
                    count += 1
        return count