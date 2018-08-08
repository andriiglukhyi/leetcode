class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dict = {}
        for item in nums:
            if item in dict:
                del dict[item]
            else:
                dict[item] = 1
        for item in dict:
            return item
        