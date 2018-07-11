class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        
        min_length = min([len(s) for s in strs])
        if min_length == 0:
            return ""
        
        for i in range(min_length):
            check = ([s[i] for s in strs])
            if check.count(check[0]) != len(check):
                return  strs[0][0:i]
        
        return strs[0][0:min_length]
        