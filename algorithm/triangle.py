class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal0(self, triangle):
        for row in range(1,len(triangle)):
            l = len(triangle[row])
            for col in range(l):
                #if the location is at the start or end, only one location from previous row can reach it
                #otherwise, col-1 and col from previous row can reach it
                if col == 0:
                    triangle[row][col] += triangle[row-1][0]
                elif col == l - 1:
                    triangle[row][col] += triangle[row-1][col-1]
                else:
                    triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])
        return min(triangle[-1])

    #Clearer solution, from bottom to top
    def minimumTotal(self, triangle):
        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        return triangle[0][0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
