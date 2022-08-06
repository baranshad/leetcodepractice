class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {'N': (0,1), 'S': (0,-1), 'E': (1,0), 'W': (-1,-0)}
        i = j = 0
        seen = [(0,0)]
        for char in path:
            i = i+ d[char][0]
            j = j+ d[char][1]
            if (i,j) in seen:
                return True 
            seen.append((i,j)) 
        return False 
        
        