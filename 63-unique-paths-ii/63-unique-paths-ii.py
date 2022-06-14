class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        d = [[0]*n for _ in range(m)]
        d[0][0] = 1 
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] or (i==0 and j ==0):
                    continue 
                d[i][j] = (d[i-1][j] if i>=1 else 0) + (d[i][j-1] if j >=1 else 0)
        return d[m-1][n-1]
        