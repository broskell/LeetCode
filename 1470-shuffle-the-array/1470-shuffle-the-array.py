class Solution(object):
    def shuffle(self, nums, n):
        output = []

        for i in range(0, n, +1):
            output.append(nums[i])
            output.append(nums[i + n])
        return output