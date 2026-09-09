class Solution(object):
    def shuffle(self, nums, n):
        x, y = nums[:n], nums[n:]
        output = []

        for i in range(0, n, +1):
            output.append(x[i])
            output.append(y[i])
        return output