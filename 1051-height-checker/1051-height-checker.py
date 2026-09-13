class Solution(object):
    def heightChecker(self, heights):
        sortedHeights = sorted(heights)
        count = 0

        for i in range(0, len(heights), +1):
            if heights[i] != sortedHeights[i]:
                count += 1
        return count