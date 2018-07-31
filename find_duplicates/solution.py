class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        end = []
        dict = {}
        for item in nums:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
            if dict[item] == 2:
                end.append(item)
        return end