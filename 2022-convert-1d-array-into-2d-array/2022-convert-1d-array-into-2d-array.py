class Solution(object):
    def construct2DArray(self, original, m, n):
        output = []

        if len(original) == m * n:
            for i in range(0, len(original), n):
                output.append(original[i:i+n])
        return output