class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        whole = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                whole.add(matrix[i][j])
                
        return target in whole 