class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        xor_all = 0
        
        for num in nums:
            xor_all ^= num
        for i in range(1, n + 1):
            xor_all ^= i
            
        rightmost_set_bit = xor_all & ~(xor_all - 1)
        
        group0 = 0
        group1 = 0
        
        for num in nums:
            if num & rightmost_set_bit:
                group1 ^= num
            else:
                group0 ^= num

        for i in range(1, n + 1):
            if i & rightmost_set_bit:
                group1 ^= i
            else:
                group0 ^= i
                
        for num in nums:
            if num == group1:
                return [group1, group0] 
                
        return [group0, group1]