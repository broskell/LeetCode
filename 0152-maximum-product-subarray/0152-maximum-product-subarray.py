class Solution(object):
    def maxProduct(self, nums):
        result = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums), +1):
            num = nums[i]
            temp_max = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp_max, num * cur_min)
            result = max(result, cur_max)  
        return result