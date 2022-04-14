class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flt = []
        for i in range(len(matrix)):
            flt.extend(matrix[i])
 
        l = 0 
        r = len(flt) -1 
        while l<= r:
            m = l + (r-l)//2 
            if flt[m] == target:
                return True 
            if flt[m] < target:
                l = m+1 
            else:
                r = m-1 
                
        return False 
    
    

