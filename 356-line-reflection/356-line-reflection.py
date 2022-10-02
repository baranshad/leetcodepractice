class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        
        points = set(map(tuple, points))
        print(points)
        minx, _ = min(points, key=lambda x: x[0])
        #print(minx,_)
        maxx, _ = max(points, key=lambda x: x[0])
        rx = (minx + maxx) / 2
        print(rx)

        return all((2 * rx - x, y) in points for x, y in points)