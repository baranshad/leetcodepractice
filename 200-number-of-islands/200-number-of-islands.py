class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(i,j):
            d = [(-1,0),(0,1), (0,-1), (1,0)]
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            for c in d:
                nx, ny = i+c[0], j + c[1]
                helper(nx, ny)
                
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    helper(i,j)
                    count += 1 
                    
        return count 
                    
        