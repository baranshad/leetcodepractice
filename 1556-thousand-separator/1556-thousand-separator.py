class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        ans = str(n)[::-1]
        res = ""
        for i in range(0, len(ans), 3):
            res += ans[i:i+3] 
            res += "."
        
        return res[:len(res)-1][::-1]
    
     
                