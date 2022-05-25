class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''
        def helper(i,j):
            while i>=0 and j< n and s[i] == s[j]:
                i -= 1
                j += 1 
            return s[i+1:j]
        
        for k in range(n):
            ans = max(ans, helper(k,k), helper(k-1, k), key = len)
            
        return ans 