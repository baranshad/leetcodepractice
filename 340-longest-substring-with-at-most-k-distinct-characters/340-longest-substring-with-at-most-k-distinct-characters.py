class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        init = 0
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]] = i 
            while len(d) > k:
                if d[s[init]] == init:
                    del d[s[init]]
                init += 1 
            
            ans = max(ans, i-init+1)
            
        return ans 
 
                