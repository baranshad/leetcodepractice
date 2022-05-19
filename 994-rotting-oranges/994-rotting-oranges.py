class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n =len(grid[0])
        t = -1
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        [q.append((i,j)) for i in range(m) for j in range(n) if grid[i][j]==2]
        while q:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()
                for c in d:
                    nx, ny = x+c[0], y+c[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        q.append((nx,ny))
                        
            t += 1 
            
        
        remaining_fresh = sum(grid[i][j] == 1 for i in range(m) for j in range(n))
        if remaining_fresh > 0:
            return -1 
        elif t == -1:
            return 0 
        else:
            return t 
                        
                    
        
        
                        
            