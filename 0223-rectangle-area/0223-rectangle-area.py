class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        xoverlap = right - left 
        
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        yoverlap = top - bottom 
        
        area_of_overlap = 0
        if xoverlap > 0 and yoverlap > 0:
            area_of_overlap = xoverlap * yoverlap 
            
            
        total_area = (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1) - area_of_overlap
        
        return total_area