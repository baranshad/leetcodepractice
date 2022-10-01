class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        j = 0 
        ans = 0 
        d = {}
        for i, val in enumerate(s):
            d[val] = i 
            if len(d) > k:
                if d[s[j]] == j:
                    del d[s[j]]
                j += 1 
                
            ans = max(ans, i-j+1)
        return (ans)