class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = ''
        for char in range(len(str)):
            if str[char].isnumeric():
                number += str[char]
        if len(number) == 0:
            return 0        
        if int(number) not in range(-2**31, 2**31-1):
            if str[0] == '-':
                return -2**31
            else:
                return 2**31 -1
        if str.replace(' ','')[0] == '-':
            return -int(number)
        return int(number)