class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n) - 1)
        if len(n)%2 == 0:
            midle = len(n)//2 -1
            temp =n[:midle+1]
            return n[:midle+1]+temp[::-1]
        else:
            midle = len(n)//2
            temp = n[:midle]
            return n[:midle+1]+temp
            
        