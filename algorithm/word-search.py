class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                #find the starting point
                if board[i][j] == word[0]:
                    if self.dfs(board, word[1:], i, j):
                        return True
        return False

    def dfs(self, board, word, i, j):
        if len(word) == 0: return True
        #up
        if i > 0 and board[i-1][j] == word[0]:
            tmp = board[i][j]
            #mark it's used
            board[i][j] = '#'
            if self.dfs(board, word[1:], i-1, j):
                return True
            #recover
            board[i][j] = tmp
        #down
        if i < len(board)-1 and board[i+1][j] == word[0]:
            tmp = board[i][j]
            #mark it's used
            board[i][j] = '#'
            if self.dfs(board, word[1:], i+1, j):
                return True
            #recover
            board[i][j] = tmp
        #left
        if j > 0 and board[i][j-1] == word[0]:
            tmp = board[i][j]
            #mark it's used
            board[i][j] = '#'
            if self.dfs(board, word[1:], i, j-1):
                return True
            #recover
            board[i][j] = tmp
        #right
        if j < len(board[0])-1 and board[i][j+1] == word[0]:
            tmp = board[i][j]
            #mark it's used
            board[i][j] = '#'
            if self.dfs(board, word[1:], i, j+1):
                return True
            #recover
            board[i][j] = tmp
        return False