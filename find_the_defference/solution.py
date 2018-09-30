class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1 = {}
        for item in s:
            if item in d1:
                d1[item] += 1
            else:
                d1[item] = 1
        for item in t:
            if item not in d1:
                return item
            else:
                d1[item] -= 1
                if d1[item] == 0:
                    del d1[item]
            