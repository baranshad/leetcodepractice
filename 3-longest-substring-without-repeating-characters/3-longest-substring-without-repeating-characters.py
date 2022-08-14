class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d= set()
        ans = 0
        i= j = 0
        while j < len(s):
            if s[j] not in d:
                d.add(s[j])
                ans = max(ans, len(d))
                j += 1 
            else:
                d.remove(s[i])
                i += 1 
            
        return ans