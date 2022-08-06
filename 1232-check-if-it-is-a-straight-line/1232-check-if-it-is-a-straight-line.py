class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l=len(coordinates)
        y1 = (coordinates[1][1] - coordinates[0][1]) 
        x1 = (coordinates[1][0] - coordinates[0][0])
        
        for i in range(1, l):
            if (coordinates[i][1] - coordinates[0][1]) * x1  != y1 * (coordinates[i][0] - coordinates[0][0]) :
                return False 
        return True 