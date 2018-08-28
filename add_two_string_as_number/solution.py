class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        rem = 0
        n, m = len(num1)-1, len(num2)-1
        if n <= m:
            a = n
            b = m
        else:
            a = m
            b = n
        st = ""
        while a > 0:
            temp = int(num1[a]) + int(num2[a]) + rem
            rem = 0
            if temp > 9:
                temp = temp % 9
                rem += 1
            st = str(temp) + st
            a -= 1
        print(st)