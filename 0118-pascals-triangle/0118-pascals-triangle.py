class Solution(object):
    def generate(self, numRows):
        pascal = []

        for i in range(0, numRows, +1):
            curList = [1] * (i + 1)
            for j in range(1, i, +1):
                curList[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(curList)
        return pascal