class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        res = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if (i==0 or j == 0 ) and matrix[i][j] == "1":
                    res[i][j] = 1 
                elif matrix[i][j] == "1":
                    res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1])+1
        ans = max(max(row) for row in res)
        return ans * ans
    
    
   