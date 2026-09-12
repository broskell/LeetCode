class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        prefix, suffix = 1, 1

        for i in range(0, len(nums), +1):
            answer[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer