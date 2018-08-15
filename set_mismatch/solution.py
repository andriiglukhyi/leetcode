class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def bin_search(beg, end, arr):
            midle = (beg + end)/2
            if arr[midle] == midle:
                bin_search(midle+1, end, arr)
            elif arr[midle] != midle:
                if arr[midle] == arr[midle-1]:
                    return [arr[midle-1],arr[midle]+1]
                elif arr[midle] == arr[midle+1]:
                    return [arr[midle+1],arr[midle]+1]
                bin_search(beg, midle-1, arr)
        if not nums or len(nums)<2:
            return False
        beg = 0
        end = len(nums)-1
        return bin_search(beg, end, nums)


