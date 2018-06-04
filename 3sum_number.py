def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return False
        found = []
        n = len(nums)
        for i in range(0, n-2):
     
            for j in range(i+1, n-1):

                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j :
                        found.append([nums[i], nums[j], nums[k]])
        """
        O(n^3)
        """