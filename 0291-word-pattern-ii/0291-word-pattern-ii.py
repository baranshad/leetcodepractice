class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(p, s, d):
            if len(p) == 0 and len(s) > 0:
                return False 
            if len(p) == 0 and len(s) == 0:
                return True 
            
            for j in range(1, len(s)-len(p)+2):
                if p[0] not in d and s[:j] not in d.values():
                    d[p[0]] = s[:j]
                    if helper(p[1:], s[j:], d):
                        return True 
                    
                    del d[p[0]]
            
                elif p[0] in d and d[p[0]] == s[:j]:
                    d[p[0]] == s[:j]
                    if helper(p[1:], s[j:], d):
                        return True 
                
            return False 
        
        return helper(pattern, s, {})