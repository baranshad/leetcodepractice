class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        def dfs(i,j, visited):
            visited.add((i,j))
            d = [(1,0),(0,1),(-1,0),(0,-1)]
            for c in d:
                ni, nj = i+c[0], j+c[1]
                if ni < 0 or nj < 0 or ni >= len(heights) or nj >= len(heights[0]) or (ni,nj) in visited or heights[ni][nj] < heights[i][j]:
                    continue
                visited.add((ni,nj))
                dfs(ni,nj,visited)
            
        p = set()
        q = set()
        for i in range(len(heights)):
            dfs(i,0,p)
            dfs(i,len(heights[0])-1, q)
            
        for j in range(len(heights[0])):
            dfs(0,j, p)
            dfs(len(heights)-1, j, q)
            
        return list(p.intersection(q))
            