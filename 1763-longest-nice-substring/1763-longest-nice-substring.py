class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def valid(s):
            for k in s.upper():
                if k.lower() not in s or k.upper() not in s:
                    return False
            return True 
            
        
        j = len(s)
        while j:
            for i in range(len(s)- j + 1):
                temp = s[i:i+j]
                
                if valid(temp):
                    return temp 
                
            j -= 1 
            
        return ''
                
                
                
        
        