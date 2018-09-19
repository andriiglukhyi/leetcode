class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = [0]
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
                if d[item] == 3:
                    del d[item]
            else:
                d[item] = 1
        i = 0
        for item in d:
            answer[i] = item
            i += 1
        return answer[0]  