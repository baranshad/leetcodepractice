class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        j = 0
        i = 0 
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                count = max(count, len(seen))
                j +=1 
            else:
                seen.remove(s[i])
                i +=1 
            
        return count
        

        
        
       
                
                