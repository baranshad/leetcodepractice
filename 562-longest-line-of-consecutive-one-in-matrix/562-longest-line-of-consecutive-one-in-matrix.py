class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        d = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(4)]
        res = 0 
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if c == 0:
                        d[0][r][c] = 1 
                    else:
                        d[0][r][c] = 1 + d[0][r][c-1]
                        
                    if r == 0:
                        d[1][r][c] = 1
                    else:
                        d[1][r][c] = 1 + d[1][r-1][c]
                        
                    if c == 0 or r == 0:
                        d[2][r][c] = 1 
                    else:
                        d[2][r][c] = 1 + d[2][r-1][c-1]
                        
                    if r == 0 or c == n-1:
                        d[3][r][c] = 1 
                    else:
                        d[3][r][c] = 1 + d[3][r-1][c+1]
                        
                    res = max(res,d[0][r][c], d[1][r][c], d[2][r][c], d[3][r][c] )
                    
        return res 
                        