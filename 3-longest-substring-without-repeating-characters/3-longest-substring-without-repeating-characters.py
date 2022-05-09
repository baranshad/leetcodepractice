class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        i = j = 0
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                num = max(num, len(seen))
                j += 1 
            else:
                seen.remove(s[i])
                i += 1 
                
        return num 

        
        
       
                
                