class Solution:
    def maxProduct(self, nums):
        curMax = curMin = answer = nums[0]

        for num in nums[1:]:
            if num < 0:
                curMax, curMin, = curMin, curMax
            
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)

            answer = max(answer, curMax)
        return answer