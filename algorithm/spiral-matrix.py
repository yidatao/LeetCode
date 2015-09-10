class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []: return []
        res = []
        direction = 0
        #boundary
        right, down, left, up = len(matrix[0]) - 1, len(matrix) - 1, 0, 0
        while up <= down and left <= right:
            #right
            if direction == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            elif direction == 1: #down
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction == 2: #left
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            else: #up
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return res