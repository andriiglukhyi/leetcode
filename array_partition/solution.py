class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        j = 0
        nums = sorted(nums)
        for _ in range(len(nums)//2):
            summ += nums[j] 
            j += 2
        return summ
            