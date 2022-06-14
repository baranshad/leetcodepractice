class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[-1]*n for _ in range(m)]
        
        def helper(r,c):
            if r<0 or c<0 or r>= m or c >= n or obstacleGrid[r][c]:
                return 0 
            if r==m-1 and c == n-1:
                return 1 
            if d[r][c] > -1: # cannot put in the first conditional place 
                return d[r][c] ## memorized 
            d[r][c] = helper(r+1, c) + helper(r, c+1)
            return d[r][c]
        return helper(0,0)