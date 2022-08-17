class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        
        x = self.countAndSay(n-1)
        res = ""
        i= 0 
        count = 0
        while i < len(x):
            cur = x[i]
            while i < len(x) and x[i] == cur:
                count += 1 
                i += 1 
                
            res += str(count) + str(cur)
            count = 0 
            
        return res 