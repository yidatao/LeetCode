class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for x in range(col)] for y in range(row)]
        dp[0][0] = int(matrix[0][0])
        for j in range(1, col):
            if matrix[0][j] == '1':
                if dp[0][j-1] == j:
                    dp[0][j] = j+1
                else:
                    dp[0][j] = max(dp[0][j-1], 1)
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1, row):
            if matrix[i][0] == '1':
                if dp[i-1][0] == i:
                    dp[i][0] = i+1
                else:
                    dp[i][0] = max(dp[i-1][0],1)
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1' and dp[i-1][j] == i*(j+1) and dp[i][j-1] == (i+1)*j:
                    dp[i][j] = (i+1)*(j+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[row-1][col-1]