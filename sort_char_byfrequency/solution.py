class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        ans = [0 for x in range(len(dic))]
        i = 0
        for item in dic:
            # print(item, dic[item])
            ans[i] = (item, dic[item])
            i += 1
        ans.sort(key= lambda item: item[1], reverse=True)
        end = ""
        for item in ans:
            end += item[0] * item[1] 
        return end