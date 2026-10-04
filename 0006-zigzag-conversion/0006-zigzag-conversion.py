class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        i, step = 0, 1
        rows = [""] * numRows

        for ch in s:
            rows[i] += ch
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
        
        return "".join(rows)