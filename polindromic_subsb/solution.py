class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for idx in range(len(s)):
            # check for odd length
            i = idx -1
            j = idx +1
            while i>=0 and j<len(s) and s[i] == s[j]:
                counter +=1
                i -=1
                j +=1

            # check for even length
            i = idx
            j = idx +1
            while i>=0 and j<len(s) and s[i] == s[j]:
                counter +=1
                i -=1
                j +=1
        return counter