class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        count = 0 
        previous = None 
        for c in s:
            if c==previous:
                count += 1 
            else:
                previous = c
                count = 1 
            ans = max(count, ans)
        return ans 