class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 
        r = [set() for _ in range(N)]
        c = [set() for _ in range(N)]
        b = [set() for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                val = board[i][j]
                if val == ".":
                    continue 
                    
                if val in r[i]: ## add the val to the i the row set 
                    return False 
                r[i].add(val)
                
                if val in c[j]:
                    return False 
                c[j].add(val)
                
                idx = (i//3) * 3 + j//3 
                if val in b[idx]:
                    return False 
                b[idx].add(val)
                
        return True 
                
        
        
        
            