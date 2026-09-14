class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            a = {}
            b = {}
            for x, y in zip(word,pattern):
                if (x in a and a[x] != y) or (y in b and b[y] != x):
                    return False
                a[x] = y
                b[y] = x
            return True
        return [word for word in words if match(word)]