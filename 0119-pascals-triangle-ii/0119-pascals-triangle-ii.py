import math
class Solution(object):
    def getRow(self, rowIndex):
        pascal = [1] * (rowIndex + 1)
        for i in range(1, rowIndex, +1):
            pascal[i] = math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i))
        return pascal