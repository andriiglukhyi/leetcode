class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1
        def binary(beg, end, nums, target):
            nonlocal ans
            if beg > end:
                return -1
            midle = (beg+end)//2
            if nums[midle] == target:
                print(midle)
                ans = midle
                return midle
            elif target > nums[midle]:
                binary(midle, end, nums, target)
            elif target < nums[midle]:
                binary(beg, midle, nums, target)
        binary(0, len(nums)-1, nums, target)
        return ans