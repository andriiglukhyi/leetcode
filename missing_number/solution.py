class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for item in nums:
            dict[item] = True
        for item in range(len(dict)):
            if item not in dict:
                return item