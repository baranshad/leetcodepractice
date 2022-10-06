class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        d = defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                d[i+j].append((i,j))
        
        res = []
        for i in range(len(d)):
            if i%2:
                d[i] = sorted(d[i], key= lambda x: x[0])
                for j, k in d[i]:
                    res.append(mat[j][k])
            elif i%2 ==0: 
                d[i] = sorted(d[i], key= lambda x: x[1])
                for j,k in d[i]:
                    res.append(mat[j][k])
        return (res)
                
         
        