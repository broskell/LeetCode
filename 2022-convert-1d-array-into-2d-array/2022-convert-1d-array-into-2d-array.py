class Solution(object):
    def construct2DArray(self, original, m, n):
        output = []

        if len(original) != m * n:
            return []
        
        for i in range(0, m, +1):
            start = i * n
            end = start + n
            output.append(original[start:end])
        return output