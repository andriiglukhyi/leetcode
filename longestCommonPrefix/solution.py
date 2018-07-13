def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        temp = enumerate(zip(*strs))
        print(list(temp))
        for i, letter_group in temp:
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)
arr =  ["flower","flow","flight"]
print(arr)
print(longestCommonPrefix(arr))