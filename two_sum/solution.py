class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(numbers)):
            n = numbers[i]
            comp = target - n
            if comp in m:
                return m[comp] + 1, i + 1
            m[n] = i
        return None
        