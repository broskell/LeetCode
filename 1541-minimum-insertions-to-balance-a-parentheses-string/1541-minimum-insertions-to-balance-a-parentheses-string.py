class Solution:
    def minInsertions(self, s):
        right, insertions, i = 0, 0, 0

        while i < len(s):
            if s[i] == '(':
                right += 1
                i += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    insertions += 1
                    i += 1

                if right > 0:
                    right -= 1
                else:
                    insertions += 1
        
        insertions += right * 2
        return insertions