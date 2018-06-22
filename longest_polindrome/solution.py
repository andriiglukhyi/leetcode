class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len less then two
        if len(s) < 2:
            return s
        self.res = ""
        # loop true each letter nd run helper function
        for i in range(len(s)):
            # for odd number of car
            self.helper(s, i, i)
            # for even number of car
            self.helper(s, i, i+1)
        return self.res
    
    def helper(self,s, left, right):
        # run till 0 or end and check if letter are ecoual at this point of time
        while left>=0 and right < len(s) and s[left] == s[right]:
            # increment left and decrement rigth
            left -= 1
            right += 1
            # if neg length is biger - mekr new res
        if right -left -1 > len(self.res):
            self.res = s[left+1:right]