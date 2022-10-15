class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points1=[[0,0] for _ in range(len(points))]
        for i, point in enumerate(points):
            points1[i][0] = point[0]*point[0] + point[1]*point[1]
            points1[i][1] = i            
  
        
        points1 = sorted(points1, key=lambda x: x[0])
        topk = [j for i, j in points1[:k]]
        return [points[i] for i in topk]
        