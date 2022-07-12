class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[i][j] for i in range(len(matrix))]):
                    res.append(matrix[i][j])
                    
        return res 