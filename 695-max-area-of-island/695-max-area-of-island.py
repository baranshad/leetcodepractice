class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:            
        def helper(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
                return 0 
            visited.add((i,j))
            return 1 + helper(i+1, j) + helper(i-1,j) + helper(i, j+1) + helper(i, j-1)
            
            
        number = 0 
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    number = max(number, helper(i,j))
                    
        return number 
       
       
                