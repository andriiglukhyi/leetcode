class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        d = {}
        for item in nums2:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for item in nums1:
            if item in d:
                inter.append(item)
                d[item] -= 1
                if d[item] == 0:
                    del d[item]
        return inter