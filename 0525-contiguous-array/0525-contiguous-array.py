class Solution(object):
    def findMaxLength(self, nums):
        count, maxCount, freqMap = 0, 0, {0 : 0}

        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else: count += 1

            if count in freqMap:
                maxCount = max(maxCount, index - freqMap[count])
            else:
                freqMap[count] = index
        return maxCount