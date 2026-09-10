class Solution(object):
    def firstUniqChar(self, s):
        frequency = {}

        for character in s:
            frequency[character] = frequency.get(character, 0) + 1

        for i, character in enumerate(s):
            if frequency[character] == 1:
                return i
                
        return -1