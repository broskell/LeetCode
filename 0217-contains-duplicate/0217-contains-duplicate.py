class Solution(object):
    def containsDuplicate(self, nums):
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for count in freqMap.values():
            if count > 1:
                return True
        return False
