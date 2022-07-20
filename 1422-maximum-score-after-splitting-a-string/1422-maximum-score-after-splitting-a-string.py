class Solution:
    def maxScore(self, s: str) -> int:
        
        ans = 0
        for i in range(1,len(s)):
            count = 0 
            count += s[:i].count('0')
            count += s[i:].count('1')
            ans = max(ans, count)
        
        return ans 
        
        #return max([s[:i].count('0')+s[i:].count('1') for i in range(1, len(s))])