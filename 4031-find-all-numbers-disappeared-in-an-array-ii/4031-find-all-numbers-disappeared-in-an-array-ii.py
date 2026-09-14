class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        cleanedNums = sorted(list(set(num for num in nums if lower <= num <= upper)))
        missing, expected = [], lower

        for num in cleanedNums:
            if num > expected:
                missing.append([expected, num - 1])
            expected = num + 1
            
        if expected <= upper:
            missing.append([expected, upper])
        return missing