class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        d = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        def bfs(x,y):
            visited = set()
            q = deque([(0,0)])
            steps= 0 
            while q:
                s = len(q)
                for i in range(s):
                    cx, cy = q.popleft()
                    if (cx, cy) == (x,y):
                        return steps 
                    
                    for dx, dy in d:
                        nx, ny = dx + cx, dy + cy
                        if (nx,ny) not in visited:
                            visited.add((nx,ny))
                            q.append((nx,ny))
                            
                steps += 1 
                
        return bfs(x,y)