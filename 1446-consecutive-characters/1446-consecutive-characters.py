class Solution:
    def maxPower(self, s: str) -> int:
        count = 1 
        ans = 1 
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count = 1 
            else:
                count += 1 
                ans = max(count, ans)
        return ans 