class Solution(object):
    def sortArrayByParity(self, nums):
        even, odd = 0, len(nums) - 1

        while even < odd:
            if nums[even] % 2 == 0:
                even += 1
            elif nums[odd] % 2 != 0:
                odd -= 1
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 1
                odd -= 1
        return nums