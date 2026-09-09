class Solution(object):
    def shuffle(self, nums, n):
        output = [0] * (2 * n)
        
        for i in range(0, len(nums) // 2, +1):
            output[i * 2] = nums[i]
        insert = 1
        for j in range(len(nums) // 2, len(nums), +1):
            output[insert] = nums[j]
            insert += 2
        return output