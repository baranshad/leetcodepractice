class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return []
        
        res = []
        
        def helper(dot, cur, i):
            if dot ==4 and i == len(s):
                res.append(cur[:-1])
            
            if dot > 4:
                return 
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <=255 and (i==j or s[i]!= "0"):
                    helper(dot+1, cur+s[i:j+1]+".", j+1)
                    
        helper(0, '', 0)
        return res 