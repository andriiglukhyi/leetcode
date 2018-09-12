class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # check for base case
        if not grid:
            return 0
        # set count of islands to the 0
        count = 0
        #loop true each element in grid
        for i in range(len(grid)):
            # loop true each element in level
            for j in range(len(grid[0])):
                # check if curent rlrmrnt is island
                if grid[i][j] == 1:
                    # run dfs traversal
                    self.dfs(grid, i, j)
                    # increment counter
                    count += 1
        return count
        
    def dfs(self, grid, i, j):
        # if we found end of the island or end of grid
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
            return
        # set elements of grid to "#" means you been here
        grid[i][j] = 0
        # go all the way down 
        self.dfs(grid, i+1, j)
        # go up
        self.dfs(grid, i-1, j)
        # go rigth
        self.dfs(grid, i, j+1)
        # go left
        self.dfs(grid, i, j-1)

ex = Solution()
arr = [[1,1,1,0,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
print(ex.numIslands(arr))