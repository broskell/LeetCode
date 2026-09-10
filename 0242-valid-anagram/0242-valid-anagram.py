class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        anagramMap = {}

        for letter in s:
            anagramMap[letter] = anagramMap.get(letter, 0) + 1
        
        for letter in t:
            if letter not in anagramMap:
                return False
            anagramMap[letter]  -= 1
        
        for count in anagramMap.values():
            if count != 0:
                return False
        return True