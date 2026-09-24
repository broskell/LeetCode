class Solution(object):
    def smallestIndex(self, nums):
        def sumOfDigits(num):
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            return sum

        for i in range(0, len(nums), +1):
            if sumOfDigits(nums[i]) == i:
                return i
        return -1