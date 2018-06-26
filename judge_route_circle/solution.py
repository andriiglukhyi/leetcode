class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dict = {'L':1, 'R': -1, 'U':2, 'D': -2}
        
        sum = 0
        for item in moves:
            sum+=dict[item]
        if sum == 0:
            return True
        return False
        