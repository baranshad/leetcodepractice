class Solution:
    def checkRecord(self, s: str) -> bool:
        numA = numL = ans = 0
        s += "P"
        
        for i in range(len(s)-1):
            if s[i+1] == s[i] and s[i]=="L":
                numL += 1 
            else:
                numL = 0
                if s[i] == "A":
                    numA += 1 
                    
            ans = max(numL+1, ans)
        
        return ans < 3 and numA < 2 