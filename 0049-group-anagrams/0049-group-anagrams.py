class Solution(object):
    def groupAnagrams(self, strs):
        strMap = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString not in strMap:
                strMap[sortedString] = []

            strMap[sortedString].append(string)
        return list(strMap.values())