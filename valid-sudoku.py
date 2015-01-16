class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        #valid rows
        for i in range(9):
            tmp = []
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    tmp.append(board[i][j])
        #valid columns
        for i in range(9):
            tmp = []
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in tmp:
                        return False
                    tmp.append(board[j][i])

        for i in [0,3,6]:
            for j in [0,3,6]:
                if not self.isValidGrid(i, j, board):
                    return False
        return True

    def isValidGrid(self, row, col, board):
        tmp = []
        for i in range(row, row+3):
            for j in range(col, col+3):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    tmp.append(board[i][j])
        return True