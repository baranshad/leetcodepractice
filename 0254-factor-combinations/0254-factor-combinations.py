class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []                       
        def dfs(temp, start, x):
            if temp: # 一开始n = n, 所以这里     
                res.append(temp[:] + [x])
            for i in range(start, int(sqrt(x))+1):  
                if x%i == 0:
                    temp.append(i)
                    dfs(temp, i, x//i)
                    temp.pop()
        dfs([], 2, n)
        return res
                
 