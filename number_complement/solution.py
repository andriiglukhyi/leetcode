class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = list(bin(num)[2:])
        for item in range(len(bits)):
            if bits[item] == '0':
                bits[item] = '1'
            elif bits[item] == '1':
                bits[item] = '0'
        return int(''.join(bits), 2)