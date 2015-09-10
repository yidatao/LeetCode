class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        width = len(obstacleGrid)
        length = len(obstacleGrid[0])
        matrix = [[0 for x in range(length)] for x in range(width)]

        for i in range(length):
            if obstacleGrid[0][i] == 1:
                break
            matrix[0][i] = 1
        for j in range(width):
            if obstacleGrid[j][0] == 1:
                break
            matrix[j][0] = 1
        for i in range(1,width):
            for j in range(1, length):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return matrix[width-1][length-1]