class Solution(object):
    def intersection(self, nums1, nums2):
        output = []
        for i in range(0, len(nums1), +1):
            if nums1[i] in nums2 and nums1[i] not in output:
                output.append(nums1[i])
        return output