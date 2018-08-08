class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(min, max, arr):
            if min >= max:
                return
            midle = (min + max) // 2
            if arr[midle] > arr[midle+1]:
                return arr[midle+1]
            if arr[midle] < arr[midle-1]:
                return arr[midle]
            left = binary_search(min, midle-1, arr)
            if left:
                return left
            rigth = binary_search(midle+1, max, arr)
            if rigth:
                return rigth
            return
        if not nums or len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0]
        if binary_search(0, len(nums)-1, nums):
            return binary_search(0, len(nums)-1, nums)
        return nums[0]