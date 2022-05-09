class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        def dfs(i,j, visited):
            visited.add((i,j))
            for (x,y) in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = x+i, y+j
                if nx <0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]) or (nx, ny) in visited or matrix[nx][ny] < matrix[i][j]:
                    continue 
                visited.add((nx, ny))
                dfs(nx, ny, visited)
                
        p = set()
        q = set()
        for i in range(len(matrix)):
            dfs(i, 0, p)
            dfs(i, len(matrix[0])-1, q)
        for i in range(len(matrix[0])):
            dfs(0, i, p)
            dfs(len(matrix)-1, i, q)
            
        return list(p.intersection(q))
            
            
                
        
        