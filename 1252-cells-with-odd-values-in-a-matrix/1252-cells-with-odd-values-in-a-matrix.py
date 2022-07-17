class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res = [[0]*n for _ in range(m)]
        for i, j in indices:
            for r in range(n):
                res[i][r] += 1 
            for c in range(m):
                res[c][j] += 1 
            
        return sum([1 for i in range(m) for j in range(n) if res[i][j]%2])
         
        
         