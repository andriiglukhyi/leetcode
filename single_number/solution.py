class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        end = [0, 0]
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            if dict[num] == 2:
                del dict[num]
        i = 0
        for item in dict:
            end[i] = item
            i += 1
        return end