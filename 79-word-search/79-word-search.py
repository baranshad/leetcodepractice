class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        b = board 
        
        def helper(i,j, suffix):
            if len(suffix) == 0:
                return True 
            
            if i < 0 or i >= m or j < 0 or j >= n or suffix[0] != b[i][j]:
                return False 
            
            b[i][j] = "#"
            for (x,y) in [(0,1), (1,0), (-1,0), (0,-1)]:
                if helper(x+i, y+j, suffix[1:]):
                    return True 
            b[i][j] = suffix[0]
            return False 
        
        for i in range(m):
            for j in range(n):
                if helper(i,j, word):
                    return True 
            
        return False 
                