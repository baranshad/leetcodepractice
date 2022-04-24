class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return None 
        
        ans = []
        def helper(idx, temp):
            if idx >= len(s):
                ans.append(temp[:])
                return 
            
            for i in range(idx, len(s)):
                if valid(s[idx:i+1]):
                    temp.append(s[idx:i+1])
                    helper(i+1, temp)
                    temp.pop()
                
        def valid(s):
            return s == s[::-1]
        
        
        helper(0, [])
        return ans 
                    