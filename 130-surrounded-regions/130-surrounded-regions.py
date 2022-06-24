class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        ru = [[0,j] for j in range(n) if board[0][j]=="O"]
        rd = [[m-1,j] for j in range(n) if board[m-1][j]=="O"]
        cl = [[i, 0] for i in range(m) if board[i][0]=="O"]
        cr = [[i, n-1] for i in range(m) if board[i][n-1]=="O"]
        
        board_cells = ru + rd + cl + cr 
        
        def helper(i,j):
            board[i][j] = "%"
            for d in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or nj < 0 or ni >= m or nj >= n or board[ni][nj] != "O":
                    continue 
                helper(ni,nj)
                    
        for i,j in board_cells:
            helper(i,j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "%":
                    board[i][j] = "O"
                    
        return board 