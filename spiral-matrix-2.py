class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res = [[0 for x in range(n)] for y in range(n)]
        num = 1
        direction = 0
        #boundary
        right, down, left, up = n - 1, n - 1, 0, 0
        while up <= down and left <= right:
            #right
            if direction == 0:
                for i in range(left, right+1):
                    res[up][i] = num
                    num += 1
                up += 1
            elif direction == 1: #down
                for i in range(up, down+1):
                    res[i][right] = num
                    num += 1
                right -= 1
            elif direction == 2: #left
                for i in range(right, left-1, -1):
                    res[down][i] = num
                    num += 1
                down -= 1
            else: #up
                for i in range(down, up-1, -1):
                    res[i][left] = num
                    num += 1
                left += 1
            direction = (direction + 1) % 4
        return res