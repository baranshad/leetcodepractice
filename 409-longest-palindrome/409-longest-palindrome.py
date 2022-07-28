class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddset = set()
        ans = 0
        for char in s:
            if char in oddset:
                ans += 1 
                oddset.remove(char)
            else:
                oddset.add(char)     
        return ans * 2 + 1 if oddset else ans * 2 
        