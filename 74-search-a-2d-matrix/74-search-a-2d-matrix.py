class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0 
        for j in range(len(matrix)):
            if matrix[j][0] <= target <= matrix[j][-1]:
                i = j

        left = 0 
        right = len(matrix[0])-1
        while left <= right:
            mid = left+ (right-left)//2 
            if matrix[i][mid] == target:
                return True 
            
            elif matrix[i][mid] < target:
                left = mid + 1 
            else: 
                right = mid - 1 
                
                
        return False 