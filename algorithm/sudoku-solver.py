class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.dfs(board)

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for v in [str(x) for x in range(1,10)]:
                        if self.isValid(i, j, v, board):
                            #if valid, put v
                            board[i][j] = v
                            #check the rest empty locations
                            if self.dfs(board):
                                return True
                            else:
                                #in this case, reset the location and try the next value
                                board[i][j] = '.'
                    #if this location hasn't been valid for all 9 values
                    return False
        #if no empty location exists, the solution has been found
        return True

    #check whether v is valid to be placed at row, col
    def isValid(self, row, col, v, board):
        for i in range(9):
            #row
            if board[row][i] == v:
                return False
            #col
            if board[i][col] == v:
                return False
        #get the starting point for its grid
        rowGrid = (row // 3) * 3
        colGrid = (col // 3) * 3
        for i in range(rowGrid, rowGrid+3):
            for j in range(colGrid, colGrid+3):
                if board[i][j] == v:
                    return False
        return True

print(Solution().solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]))