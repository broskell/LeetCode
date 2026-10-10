class Solution(object):
    def sortArrayByParity(self, nums):
        even, odd = 0, len(nums) - 1

        while even < odd:
            if nums[even] % 2 == 0:
                even += 1
            elif nums[odd] % 2 != 0:
                odd -= 1
            elif nums[even] % 2 != 0 and nums[odd] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums