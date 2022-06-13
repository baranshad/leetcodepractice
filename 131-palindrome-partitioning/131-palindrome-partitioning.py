class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def helper(temp, idx):
            
            if idx == len(s): 
                ans.append(temp[:])
                return 
                
            
            for i in range(idx, len(s)):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    temp.append(s[idx:i+1])
                    helper(temp, i+1)
                    temp.pop()
                    
        helper([], 0)
        return ans 
                
                