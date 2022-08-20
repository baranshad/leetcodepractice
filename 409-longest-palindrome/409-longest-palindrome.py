class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        ans = 0
        for i in s:
            if i in odd:
                ans += 1 
                odd.remove(i)
            else:
                odd.add(i)
                
        return ans* 2 + 1 if odd else ans * 2 
                