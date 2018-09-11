class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        end = ""
        for item in S:
            if item.isalpha() or item.isnumeric():
                end += item.upper()
        end1 = ''
        counter = 0
        for item in reversed(range(len(end))):
            if counter == K:
                end1 += "-" + end[item]
                counter = 0
            else:
                end1+= end[item]
            counter += 1
        print(end1[::-1])


inst = Solution()
print(inst.licenseKeyFormatting("5F3Z-2e-9-w",4))
print(inst.licenseKeyFormatting("2-5g-3-J",2))
