class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        nums = []
        for e in s:
            nums.append(dict[e])
        max = 0
        result = 0
        print(nums)
        for num in nums[::-1]:
            if max <= num:
                max = num
                result += num
            else:
                result -= num
        return result
        