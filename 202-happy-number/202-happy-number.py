class Solution:
    def isHappy(self, n: int) -> bool:
        def gennext(n):
            sum1 = 0
            while n>0:
                n, digit = divmod(n, 10)
                sum1 += digit**2 
            return sum1 
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = gennext(n)
            
        return n == 1 