class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        res = resanti = 0
        for i in range(m):
            res += mat[i][i] 
            resanti += mat[i][m-i-1]
        if not m % 2: 
            return res+resanti
        else:
            return res+resanti - mat[int(m//2)][int(m//2)]