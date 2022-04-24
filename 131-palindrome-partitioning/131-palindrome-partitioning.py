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
                if (s[idx:i+1] == s[idx:i+1][::-1]):
                    temp.append(s[idx:i+1])
                    helper(i+1, temp)
                    temp.pop()
            
        
        
        helper(0, [])
        return ans 
                    