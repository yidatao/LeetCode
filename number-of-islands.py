class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    #merge adjacent islands
                    self.merge(grid, i, j)
        return count
    
    def merge(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return
        #because of replacement, here should be !='1' instead of == '0'
        if grid[i][j] != '1': return
        if grid[i][j] == '1': grid[i][j] = '2'
        self.merge(grid, i-1, j)
        self.merge(grid, i+1, j)
        self.merge(grid, i, j-1)
        self.merge(grid, i, j+1)