class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat 
        
        matrix = [[None for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(m):
            for j in range(n):
                matrix[count//c][count%c] = mat[i][j]
                count += 1 
        return matrix
            
        
        #m, n, count = len(nums), len(nums[0]), 0
        #if m*n != r*c: return nums
        #res = [[0] * c for _ in range(r)]
        #for i, j in product(range(m), range(n)):
            #res[count//c][count%c] = nums[i][j]
            #count += 1      
        #return res