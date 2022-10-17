class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def nbs(r,c):
            for dx, dy in d:
                nx, ny = r+dx, c+dy 
                if nx < 0 or ny < 0 or nx>= m or ny >= n or grid[nx][ny] != 0:
                    continue 
                yield(nx, ny)
                
        if grid[0][0] != 0 or grid[m-1][n-1] !=0:
            return -1 
        
        q =deque()
        q.append((0,0))
        grid[0][0] = 1 
        while q:
            r, c = q.popleft()
            distance = grid[r][c]
            if (r,c) == (m-1, n-1):
                return distance 
            for nx, ny in nbs(r,c):
                grid[nx][ny] = distance + 1 
                q.append((nx,ny))
                
        return -1 
        
        
        
        
        
        
        
        
        
        
        
        
        