class Solution(object):
    def spiralOrder(self, matrix):
        output = []
        rows, cols = len(matrix), len(matrix[0])

        left, top = 0, 0
        right, bottom = cols - 1, rows - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1, +1):
                output.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1, +1):
                output.append(matrix[i][right])
            right -= 1

            if left > right or top > bottom:
                break
            
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        return output