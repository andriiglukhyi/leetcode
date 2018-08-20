class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        dict = {}
        for number in nums:
            if number in dict:
                dict[number] += 1
            else:
                dict[number] = 1
        for item in range(len(nums)-1):
            cur = dict[nums[item]]
            if nums[item] + 1 in dict:
                cur += dict[nums[item]+1]
                if cur > longest:
                    longest = cur
        return longest
                