class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def helper(i, j, wordlist):
            if not len(wordlist):
                return True 
            if i < 0 or j < 0 or i >= m or j >= n or wordlist[0] != board[i][j] :
                return False 
           
            board[i][j] = "#"
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = i+dx, j+dy 
                if helper(nx, ny, wordlist[1:]):
                    return True 
            board[i][j] = wordlist[0]
            return False 
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(i,j, word):
                        return True 
        return False 
            