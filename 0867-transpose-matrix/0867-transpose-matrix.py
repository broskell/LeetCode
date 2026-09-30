class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * rows for _ in range(0, cols, +1)]

        for i in range(0, rows, +1):
            for j in range(0, cols, +1):
                result[j][i] = matrix[i][j]         
        return result