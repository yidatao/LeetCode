class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        #remember whether first row and col originally have 0
        firstRowZero = False
        firstColZero = False
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        for i in range(rows):
            if matrix[i][0] == 0:
                firstColZero = True
                break

        #use first row and col to mark
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        #set 0 according to the marks
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0