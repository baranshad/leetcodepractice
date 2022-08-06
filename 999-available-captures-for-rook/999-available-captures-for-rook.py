class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m = 8
        for o in range(m):
            for p in range(m):
                if board[o][p] == "R":
                    i,j = o,p
                    break 
                    
        total = 0 
        for y in range(j+1, m):
            if board[i][y] == "p":
                total += 1 
                break 
            elif board[i][y] == "B":
                break 
                
        for y in range(j-1, -1,-1):
            if board[i][y] == "p":
                total += 1 
                break 
            elif board[i][y] == "B":
                break 
                
        for x in range(i+1, m):
            if board[x][j] == "p":
                total += 1 
                break 
            elif board[x][j] == "B":
                break 
                
        for x in range(i-1,-1, -1):
            if board[x][j] == "p":
                total += 1 
                break 
            elif board[x][j] == "B":
                break 
                
                
        return total 
        
