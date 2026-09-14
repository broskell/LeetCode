class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        numsSet = set(nums)
        missing, i = [], lower

        while i <= upper:
            if i not in numsSet:
                expected = i

                while i <= upper and i not in numsSet:
                    i += 1
                missing.append([expected, i - 1])
            else:
                i += 1
        return missing