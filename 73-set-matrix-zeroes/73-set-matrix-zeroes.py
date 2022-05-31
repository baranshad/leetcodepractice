class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        allzeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    allzeros.append((i,j))
        
        
        def helper(matrix, r, c):
            for i in range(len(matrix[0])):
                matrix[r][i] = 0   
            for j in range(len(matrix)):
                matrix[j][c] = 0 
                    
        for i,j in allzeros:
            helper(matrix,i,j)
        
                    
                    
                    
        
                
            