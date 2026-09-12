class Solution(object):
    def isPalindrome(self, s):
        cleanedS = "".join(char.lower() for char in s if char.isalnum())

        return cleanedS == cleanedS[::-1]