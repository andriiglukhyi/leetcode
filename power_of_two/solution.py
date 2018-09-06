class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # check if this number 0 then False
        if n == 0:
            return False
        # check is 1 => 2^0 == 1
        if n == 1:            
            return True
        if  n%2 == 0:
            # go down recursevly and check if number is can be divided bu two
            return self.isPowerOfTwo(n/2)
        else:
            return False
            