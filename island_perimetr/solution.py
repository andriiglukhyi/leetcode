class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == len(grid[0]) == 1:
            return 4
        # traverse grid and count stripes
        stripes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or i == len(grid)-1:
                        stripes += 1
                    if j == 0 or j == len(grid[0])-1:
                        stripes += 1
                    if i-1 >=0:
                        if grid[i-1][j] == 0:
                            stripes += 1
                    if i+1 <= len(grid)-1:
                        if grid[i-i][j] == 0:
                            stripes += 1
                    if j-1 >= 0:
                        if grid[i][j-1] == 0:
                            stripes += 1
                    # elif j == 0:
                    #     stripes += 1
                    if j+1 <= len(grid[0])-1:
                        if grid[i][j+1] == 0:
                            stripes += 1
                    # elif j == len(grid[0]):
                    #     stripes += 1
        return stripes