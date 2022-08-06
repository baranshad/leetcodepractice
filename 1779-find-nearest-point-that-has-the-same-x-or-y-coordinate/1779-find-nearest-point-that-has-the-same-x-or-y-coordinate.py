class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mind = inf
        idx = cur = 0
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                cur = abs(points[i][0]-x) + abs(points[i][1]- y)
                if cur < mind:
                    mind = cur 
                    idx = i 
                    
        if mind == inf:
            return -1 
        else:
            return idx 
        