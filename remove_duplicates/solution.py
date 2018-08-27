class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = i + 1
        arr = len(nums)
        dif = 0
        cur = 1
        while j < len(nums)-1:
            if nums[i] == nums[j]:
                cur += 1
                j += 1
            else:
                print(i, j)
                nums = nums[:i] + nums[j-1:]
                if cur > 2:
                    dif += 2
                else:
                    dif += cur
                cur = 0
                i = dif
                j = i + 1