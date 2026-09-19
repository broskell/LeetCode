class Solution(object):
    def subarraysDivByK(self, nums, k):
        curSum, count = 0, 0
        freqMap = {0 : 1}

        for num in nums:
            curSum += num
            rem = curSum % k

            if rem in freqMap:
                count += freqMap[rem]
                freqMap[rem] += 1
            else:
                freqMap[rem] = 1
        return count