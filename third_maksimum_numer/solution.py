class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort 
        temp = list(set(nums))
        temp.sort(reverse = True)
        if len(temp) >= 3:
            return temp[2]
        if len(temp) <= 2:
            return max(nums)