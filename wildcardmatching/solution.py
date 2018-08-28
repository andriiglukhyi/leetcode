class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        while i <= len(s) and j <= len(p)
            if p[j] == s[i]:
                i += 1
                j += 1
            elif p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                j += 1
                while (s[i] != p[j] or p[j] != '?') and (s[i+1] != p[j+1] or p[j+1] == '?'):
                    i+= 1
                