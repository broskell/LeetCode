class Solution(object):
    def uniqueOccurrences(self, arr):
        freqMap = {}

        for num in arr:
            freqMap[num] = freqMap.get(num, 0) + 1

        seen = set()
        for count in freqMap.values():
            if count in seen:
                return False
            seen.add(count)
        return True