class Solution:
    # @return an integer
    def totalNQueens0(self, n):
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

    #iterative solution
    def totalNQueens(self, n):
        self.board = [-1 for x in range(n)]
        row, col, sum = 0,0,0
        while row < n:
            #for row, find valid col
            while col < n:
                if self.isValid(row, col):
                    self.board[row] = col
                    break
                else:
                    col += 1
            #if failed to find a valid col for row
            if self.board[row] == -1:
                if row == 0:
                    break
                else:
                    #trace back to the previous row
                    row -= 1
                    #try the next column in the previous row
                    col = self.board[row] + 1
                    #retry the previous row
                    self.board[row] = -1
                    continue
            #if reach here, then it means we find the valid column for the last row
            elif row == n-1:
                #found a solution
                sum += 1
                #try the next column for this row
                col = self.board[row] + 1
                #retry this row
                self.board[row] = -1
                continue
            else:
                #move on to the next row
                row += 1
                col = 0
        return sum

