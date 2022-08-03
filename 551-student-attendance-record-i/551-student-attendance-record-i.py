class Solution:
    def checkRecord(self, s: str) -> bool:
        numA = numL = maxA = 0
        s = s + "P"
        for i in range(len(s)-1):
            if s[i] == s[i+1] and s[i] == "L":
                numL += 1 
            else:
                numL = 0 
                if s[i] == "A":
                    numA += 1 
            
            maxA = max(numL+1, maxA)
            
        return maxA < 3 and numA < 2 
                
                
            
            