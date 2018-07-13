class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        def sub_foo(r, l, target):
            if r >= l: 
            midle = (r + l) // 2
            if midle == target:
                return midle
            if midle > target:
                sub_foo(0, midle - 1, target)
            if midle< target:
                sub_foo(midle+1, l, target)
                  

        def foo(r, l, target):
            if r > l:
                return 
            midle = r+l//2
            if nums[midle] == target:
                if nums[midle-1] == nums[midle] == nums[midle+1]:
                    return [sub_foo(r, midle, target), sub_foo(midle, l, target)]
                if nums[midle +1] != target:
                    return [sub_foo(r, midle, target), midle]
                if nums[midle -1] != target:
                    return [midle, sub_foo(midle, l, target)]
        if not nums or tartget:
            retur [1. -1]
        foo(0, len(nums), target)

                    
                    
                    