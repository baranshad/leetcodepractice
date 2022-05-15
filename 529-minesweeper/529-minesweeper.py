class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        d = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1),(-1,-1)]
        
        def helper(r,c):
            if board[r][c] == "E":
                count = 0 
                for nr, nc in d:
                    i, j = nr + r, nc +c 
                    if 0 <= i < m and 0 <= j < n and board[i][j] == "M":
                        count +=1 
                if count > 0:
                    board[r][c] = str(count)
                    
                else:
                    board[r][c] = "B"
                    for nr, nc in d:
                        i, j = nr + r, nc +c 
                        if 0 <= i < m and 0 <= j < n and board[i][j] == "E":
                            helper(i,j)
                        
        x,y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = 'X'
        else:
            helper(x,y)
        
        return board
                