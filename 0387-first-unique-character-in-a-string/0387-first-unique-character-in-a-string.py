class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1