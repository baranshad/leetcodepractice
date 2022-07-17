class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0]* 3 for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i][0], moves[i][1]
            if i%2==0:
                board[x][y] = "X"
            else:
                board[x][y] = "O"
        def row(r, x):
            countr =[]
            for i in range(3):
                countr.append(len([val for val in board[i] if val == x]))
            return max(countr)
        def col(c, x):
            countc = []
            for i in range(3):
                countc.append(len([val for val in [board[k][i] for k in range(3)] if val == x]))
            return max(countc)
        
        def diag(x):
            return len([val for val in [board[0][0], board[1][1], board[2][2]] if val ==x])
        
        def antidiag(x):
            return len([val for val in [board[2][0], board[1][1], board[0][2]] if val ==x])
        
        # for x 
        allvals = [row(0,"X"), row(1,"X"), row(2,"X"), 
                   col(0,"X"), col(1,"X"), col(2,"X"), diag("X"), antidiag("X")]
        allvals_0 = [row(0,"O"), row(1,"O"), row(2,"O"), 
                   col(0,"O"), col(1,"O"), col(2,"O"), diag("O"), antidiag("O")]
        
        maxx = max(allvals)
        maxo = max(allvals_0)
        if maxx == 3: return "A"
        elif maxo == 3 and maxx < 3: return "B"
        elif maxx < 3 and maxo < 3 and len(moves) < 9 : return "Pending"
        elif maxx<3 and maxo < 3 and len(moves) >=9: return "Draw"
        
        
        
                
                    
                