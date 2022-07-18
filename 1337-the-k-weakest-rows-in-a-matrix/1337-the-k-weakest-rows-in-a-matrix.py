class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            d[i] = sum(mat[i])
            
        sd= sorted(d.items(), key=lambda x: (x[1],x[0]))
        res = [i for i, j in sd]
        return res[:k]