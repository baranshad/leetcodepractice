class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []              
        factors = []           
        def dfs(start, n):
            if factors:      
                res.append(factors + [n])
            for i in range(start, int(sqrt(n))+1):  
                if n%i == 0:
                    factors.append(i)
                    dfs(i, n//i)
                    factors.pop()
        dfs(2, n)
        return res
                
        #res = []              
        #factors = []           
        #def dfs(start, n):
            #if factors:       # ensure x != n
               # res.append(factors + [n])
            #for i in range(start, int(sqrt(n))+1):  n
                #if n%i == 0:
                   # factors.append(i)
                   # dfs(i, n/i)
                   # factors.pop()
        #dfs(2, n)
        #return res