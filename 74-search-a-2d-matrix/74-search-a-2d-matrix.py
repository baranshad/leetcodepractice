class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])-1
        
        rowidx = 0
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                rowidx = i
                
        
        
        left = 0 
        right = n
        while left <= right:
            mid = left+ (right-left)//2 
            if matrix[rowidx][mid] == target:
                return True 
            
            elif matrix[rowidx][mid] < target:
                left = mid + 1 
            else: 
                right = mid - 1 
                
                
        return False 
        