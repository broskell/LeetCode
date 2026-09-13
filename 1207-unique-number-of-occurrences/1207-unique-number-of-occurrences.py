class Solution(object):
    def uniqueOccurrences(self, arr):
        freqMap = {}

        for num in arr:
            freqMap[num] = freqMap.get(num, 0) + 1
            
        return len(freqMap.values()) == len(set(freqMap.values()))