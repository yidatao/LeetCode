class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []:
            return []
        row, col = len(board), len(board[0])
        queue = []
        visited = [[False for x in range(col)] for y in range(row)]
        #O in the four edges definitely not surrounded by X, so we first identify these Os
        for i in range(col):
            if board[0][i] == 'O':
                queue.append((0,i))
            if board[row-1][i] == 'O':
                queue.append((row-1,i))
        for i in range(row):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][col-1] == 'O':
                queue.append((i,col-1))
        #use BFS to get all Os that can be connected to these edges Os
        while queue:
            n = queue.pop(0)
            x,y = n[0],n[1]
            board[x][y] = '*'
            visited[x][y] = True
            #find its connected Os
            #up
            if x-1 >= 0 and board[x-1][y] == 'O' and not visited[x-1][y]:
                queue.append((x-1,y))
            #down
            if x+1 < row and board[x+1][y] == 'O' and not visited[x+1][y]:
                queue.append((x+1,y))
            #left
            if y-1 >= 0 and board[x][y-1] == 'O' and not visited[x][y-1]:
                queue.append((x,y-1))
            #right
            if y+1 < col and board[x][y+1] == 'O' and not visited[x][y+1]:
                queue.append((x,y+1))
        #final mark
        for i in range(row):
            for j in range(col):
                if board[i][j] == '*':
                    #reset it to O
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
