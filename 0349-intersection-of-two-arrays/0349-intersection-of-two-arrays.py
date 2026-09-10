class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        output = []

        for num in set1:
            if num in set2:
                output.append(num)
        return output