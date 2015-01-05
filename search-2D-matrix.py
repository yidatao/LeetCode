class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        nRows = len(matrix)
        nCols = len(matrix[0])
        #Given the definition of the matrix, it's actually a sorted array
        start, end = 0, nRows*nCols-1
        while start <= end:
            mid = (start + end) // 2
            #figure out the row and column for mid
            row = mid // nCols
            col = mid % nCols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

x = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print(Solution().searchMatrix(x, 7))