class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        w = []
        total = [x for x in range(1, numRows+1)] + [x for x in reversed(range(2, numRows))]
        w = total * (len(s)//len(total)) + total[0:len(s)%len(total)]
        end = list(zip(list(s), w))
        st = []
        for number in range(1, len(total)+1):
            st += [x[0] for x in end if x[1] == number]
        return(''.join(st))
        