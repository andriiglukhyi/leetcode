class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for item in range(len(A)):
            if A[item]>A[item+1] and A[item] > A[item-1]:
                return item
            