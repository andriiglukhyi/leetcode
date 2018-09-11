class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        dict = {}
        for item in s:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
            if dict[item] == 2:
                longest += 2
                del dict[item]
        if dict:
            return longest + 1
        return longest