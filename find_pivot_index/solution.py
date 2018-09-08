class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = sum(nums)
        l = 0
        for item in range(len(nums)):
            r -= nums[item]
            if l == r:
                return item
            l += nums[item]
        return -1