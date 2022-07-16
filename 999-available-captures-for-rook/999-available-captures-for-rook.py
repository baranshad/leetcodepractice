class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m = 8
        for i in range(m):
            for j in range(m):
                if board[i][j] == "R":
                    x,y = i,j
                    break 
        res = 0
        for i in range(x-1,-1,-1):
            if board[i][y] == 'p':
                res += 1 
                break 
            elif board[i][y] == "B":
                break 
                
        for i in range(x+1,m):
            if board[i][y] == 'p':
                res += 1 
                break 
            elif board[i][y] == "B":
                break 
                
        for j in range(y-1, -1, -1):  # check west
            if board[x][j] == 'p':
                res += 1
                break
            if board[x][j] == 'B':
                break
        
        for j in range(y+1, m):  # check east
            if board[x][j] == 'p':
                res += 1
                break
            if board[x][j] == 'B':
                break
        
        return res
