class Solution:
    # @return an integer
    # dynamic programming
    def uniquePaths(self, m, n):
        matrix = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]


print(Solution().uniquePaths(23,12))