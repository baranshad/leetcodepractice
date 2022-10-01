class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        d = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        newm = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = 0
                for c in d:
                    nx, ny = i+c[0], j+c[1]
                    if nx>= 0 and ny >=0 and nx< len(board) and ny < len(board[0]) and newm[nx][ny] == 1:
                        temp += 1
                if newm[i][j]==1 and (temp <2 or temp >3):
                    board[i][j] = 0
                if newm[i][j]==0 and (temp == 3):
                    board[i][j] = 1
                    
  