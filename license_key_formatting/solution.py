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
        counter = 1
        for item in reversed(range(len(end))):
            counter += 1
            if counter == K:
                end1 += "-" + end[item]
                counter = 1
            else:
                end1+= end[item]
            print(end1)