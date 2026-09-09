class Solution(object):
    def removeDuplicates(self, nums):
        unique = 0

        for j in range(0, len(nums), +1):
            if nums[unique] != nums[j]:
                unique += 1
                nums[unique] = nums[j]
        return unique + 1