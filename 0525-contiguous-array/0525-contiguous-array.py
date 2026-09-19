class Solution(object):
    def findMaxLength(self, nums):
        count, maxCount, freqMap = 0, 0, {0 : -1}

        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else: count += 1

            if count in freqMap:
                maxCount = max(maxCount, index - freqMap[count])
            else:
                freqMap[count] = index
        return maxCount