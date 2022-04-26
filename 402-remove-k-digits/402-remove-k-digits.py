class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for i in num:
            while res and k and res[-1] > i:
                res.pop()
                k -= 1 
                
            res.append(i)
        #print(res)    
        finals = res[:-k] if k else res
        return "".join(finals).lstrip('0') or '0'
        
            