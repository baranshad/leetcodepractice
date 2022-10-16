class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = -1
        q = deque()
        [q.append((i,j)) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==2]
        
        while q:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()
                for c in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nx, ny = x+c[0], y+c[1]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        q.append((nx,ny))
                        
            t += 1 
            
        
        remaining_fresh = sum(grid[i][j] == 1 for i in range(len(grid)) for j in range(len(grid[0])))
        if remaining_fresh > 0:
            return -1 
        elif t == -1:
            return 0 
        else:
            return t 
                        