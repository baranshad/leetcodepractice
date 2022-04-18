class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        i = 0 
        j = 0 
        ans = 0 
        temp = set()
        while j < len(s):
            while j< len(s) and s[j] not in temp and j-i < k:
                temp.add(s[j])
                j += 1 
                
            if len(temp) == k: 
                ans += 1 
            temp.remove(s[i])
            i += 1 
            
         
        return ans 
            
            
                    
                