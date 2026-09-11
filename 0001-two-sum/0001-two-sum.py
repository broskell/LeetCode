class Solution(object):
    def twoSum(self, nums, target):
        output = {}

        for i in range(0, len(nums), +1):
            required = target - nums[i]
            if required in output:
                return i, output[required]
            output[nums[i]] = i