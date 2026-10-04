class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        index, d = 0, 1
        row = [[] for _ in range(0, numRows, +1)]

        for ch in s:
            row[index].append(ch)

            if index == 0:
                d = 1
            elif index == numRows - 1:
                d = -1
            index += d
        
        for i in range(0, numRows, +1):
            row[i] = ''.join(row[i])
        
        return ''.join(row)