class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        freqMap = {}
        count = 0

        for num1 in nums1:
            for num2 in nums2:
                pair = num1 + num2
                freqMap[pair] = freqMap.get(pair, 0) + 1
        
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in freqMap:
                    count += freqMap[target]
        
        return count