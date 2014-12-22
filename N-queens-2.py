class Solution:
    # @return an integer
    def totalNQueens(self, n):
        #special representation of the board.
        #The location of each queen is (i, board(i))
        self.board = [-1 for x in range(n)]
        self.res = 0
        self.solve(0, n)
        return self.res

    #whether it's okay to place the queen in [row][col]
    def isValid(self, row, col):
        #for each previous row i
        for i in range(row):
            #if there is already queen on the same column
            #or on the diagonal, then cannot place queen in row,col
            if self.board[i] == col or abs(row - i) == abs(col - self.board[i]):
                return False
        return True

    def solve(self, k, n):
        if k == n:
            self.res += 1
            return
        for col in range(n):
            if self.isValid(k, col):
                self.board[k] = col
                self.solve(k+1, n)