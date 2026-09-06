import math
class Solution(object):
    def generate(self, numRows):
        pascal = []

        for i in range(0, numRows, +1):
            curList = []
            for j in range(0, i + 1, +1):
                nCr = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
                curList.append(nCr)
            pascal.append(curList)
        return pascal