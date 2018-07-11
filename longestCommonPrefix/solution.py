def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)
arr = ['newligth' for x in range(300)]
arr[-2] = "newligghhgh"
print(arr)
print(longestCommonPrefix(arr))