class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1 
                j += 1 
            return s[i+1:j]
        
        ans = ''
        for k in range(len(s)):
            ans = max(ans, helper(k,k), helper(k-1,k), helper(k,k+1), key = len)
            
        return ans 