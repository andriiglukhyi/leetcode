class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_sum = None
        sum = 0
        def walk(i,j, sum):
            print(sum)
            nonlocal min_sum
            if i == len(triangle) or j < 0 or j > len(triangle[i]):
                return
            sum += triangle[i][j]
            if i == len(triangle)-1:
                if min_sum is None:
                    min_sum = sum
                else:
                    min_sum = min(sum, min_sum)
            walk(i+1,j,sum)
            walk(i+1,j-1,sum)
            walk(i+1,j+1,sum)
        if len(triangle) == 0:
            return 0
        walk(0,0, sum)
        return min_sum