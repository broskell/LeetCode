class Solution(object):
    def findErrorNums(self, nums):
        xor_all = 0
        
        for i in range(0, len(nums), +1):
            xor_all ^= nums[i]
            xor_all ^= i + 1
            
        rightmost_set_bit = xor_all & ~(xor_all - 1)
        group0, group1 = 0, 0

        for i in range(0, len(nums), +1):
            if nums[i] & rightmost_set_bit:
                group1 ^= nums[i]
            else:
                group0 ^= nums[i]

            if i + 1 & rightmost_set_bit:
                group1 ^= i + 1
            else:
                group0 ^= i + 1
                
        for num in nums:
            if num == group1:
                return [group1, group0] 
                
        return [group0, group1]