class Solution(object):
    def singleNumber(self, nums):
        XOR = 0

        for num in nums:
            XOR ^= num
        return XOR