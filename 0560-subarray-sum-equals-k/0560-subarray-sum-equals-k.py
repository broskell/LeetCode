class Solution(object):
    def subarraySum(self, nums, k):
        curSum, count = 0, 0 
        freqMap = {0 : 1}

        for num in nums:
            curSum += num
            if curSum - k in freqMap:
                count += freqMap[curSum - k]
            freqMap[curSum] = freqMap.get(curSum, 0) + 1
        return count