class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = max(strs)
        n = min(strs)
        
        for i in range(len(n)):
            if m[i] != n[i]:
                return m[:i]
        return n 
             