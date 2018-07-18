class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ""
        if len(nums) <3:
            return "/".join(map(str, nums))
            # return str(nums[0]) + "/" + str(nums[1])         
        end = "("+"/".join(map(str, nums[1:]))+")"
        return str(nums[0])+"/"+end
            