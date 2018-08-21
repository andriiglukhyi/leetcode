class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        for item in range(len(s)):
            s[item] = s[item][::-1]
        return ' '.join(s)
        