class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            temp = {}
            for letter in word:
                if letter in temp:
                    temp[letter] += 1
                else:
                    temp[letter] = 1
            temp = str(sorted(list(temp.items())))
            print(temp)
            try:
                dict[temp] = [word] + dict[temp]
            except KeyError:
                dict[temp] = [word]
        end = []
        for value in dict.values():
            end.append(value)
        return end