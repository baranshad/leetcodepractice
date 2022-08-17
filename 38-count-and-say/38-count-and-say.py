class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        
        x = self.countAndSay(n-1)
        res = ""
        i = 0 
        counter = 0 
        while i < len(x):
            cur = x[i]
            while i < len(x) and x[i] == cur:
                counter += 1 
                i += 1 
                
            res += str(counter) + str(cur)
            counter = 0 
        return res 
            