class Solution(object):
    def subarraysDivByK(self, nums, k):
        curSum, count = 0, 0
        freq = [0] * k
        freq[0] = 1

        for num in nums:
            curSum += num
            rem = curSum % k
            count += freq[rem]

            freq[rem] += 1
        return count