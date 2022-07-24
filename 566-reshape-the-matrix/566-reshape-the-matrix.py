class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat 
        
        matrix = []
        row = []
        for i in mat:
            for j in i:
                row.append(j)
                
        for i in range(0, len(row), c):
            matrix.append(row[i:i+c])
        return matrix 
    