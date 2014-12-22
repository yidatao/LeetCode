class Solution:
    # @return a list of lists of string
    # every row, every column, and every diagonal has only one queen
    def solveNQueens(self, n):
        #special representation of the board.
        #The location of each queen is (i, board(i))
        self.board = [-1 for x in range(n)]
        self.res = []
        self.solve(0, [], n)
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

    def solve(self, k, solution, n):
        if k == n:
            self.res.append(solution)
            return
        for col in range(n):
            if self.isValid(k, col):
                self.board[k] = col
                rstr = '.'*col + 'Q' + '.'*(n-col-1)
                self.solve(k+1, solution + [rstr], n)

print(Solution().solveNQueens(4))