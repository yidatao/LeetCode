class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # Dynamic programming
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][0] = grid[0][0]
        for i in range(1,m):
            matrix[i][0] = matrix[i-1][0] + grid[i][0]
        for j in range(1,n):
            matrix[0][j] = matrix[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]
        return matrix[m-1][n-1]
