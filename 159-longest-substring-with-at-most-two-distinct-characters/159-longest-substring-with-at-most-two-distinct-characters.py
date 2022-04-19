class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s) 
        
        ans = 0 
        i = 0 
        j = 0 
        d = defaultdict()
        while j < len(s):
            d[s[j]] = j
            
            if len(d) == 3:
                idx = min(d.values())
                del d[s[idx]]
                i = idx + 1 
            ans=max(ans, j-i+1)
            j += 1 
        return ans 
            


            