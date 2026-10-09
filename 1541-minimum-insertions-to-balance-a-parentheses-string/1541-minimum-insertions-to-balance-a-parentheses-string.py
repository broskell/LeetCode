class Solution(object):
    def minInsertions(self, s):
        i, insertions, right = 0, 0, 0

        while i < len(s):
            if s[i] == '(':
                right += 2

                if right % 2 != 0:
                    insertions += 1
                    right -= 1
                i += 1 
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    insertions += 1
                    i += 1

                if right > 0:
                    right -= 2
                else:
                    insertions += 1 
        return insertions + right