class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            ans = 0
            while n>0:
                n, digit = divmod(n,10)
                ans += digit * digit 
            return ans 
        
        seen = set()
        while n != 1 and n not in seen: 
            seen.add(n)
            n = helper(n)
            
        return n == 1 