class Solution(object):
    def buildArray(self, nums):
        output = []

        for i in range(0, len(nums), +1):
            output.append(nums[nums[i]])
        return output