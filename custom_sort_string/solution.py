class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        di = {}
        for item in T:
            if item in di:
                di[item] += 1
            else:
                di[item] = 1
        ans = ""
        for item in S:
            if item in di:
                ans += item * di[item]
                del di[item]
        for item in di:
            ans += item * di[item]
        return ans
            