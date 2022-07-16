class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s):
            return len(set(s.lower())) == len(set(s))//2
        
        j = len(s)
        while j > 0: 
            for i in range(len(s)-j+1):
                temp = s[i:i+j]
                if helper(temp):
                    return temp 
            j -= 1 
        return ''
                
    
        
        