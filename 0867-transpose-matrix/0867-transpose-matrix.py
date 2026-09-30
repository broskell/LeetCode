class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for j in range(0, cols, +1):
            row = []
            for i in range(0, rows, +1):
                row.append(matrix[i][j])
            result.append(row)
        return result