class Solution(object):
    def getRow(self, rowIndex):
        row, prevVal = [1], 1

        for i in range(1, rowIndex + 1, +1):
            nextVal = prevVal * (rowIndex - i + 1) // i
            row.append(nextVal)
            prevVal = nextVal
        return row