class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = bin(n)[2:]
        print(st)
        for item in range(len(st)-1):
            if st[item] == st[item+1]:
                return False
        return True