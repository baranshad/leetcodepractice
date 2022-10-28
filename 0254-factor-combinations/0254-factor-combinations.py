class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []              
        #factors = []           
        def dfs(temp, start, n):
            if temp:      
                res.append(temp[:] + [n])
            for i in range(start, int(sqrt(n))+1):  
                if n%i == 0:
                    temp.append(i)
                    dfs(temp, i, n//i)
                    temp.pop()
        dfs([], 2, n)
        return res
                
 