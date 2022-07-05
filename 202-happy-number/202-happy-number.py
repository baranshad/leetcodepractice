class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            ans = 0
            while n>0:
                n, digit = divmod(n,10)
                ans += digit * digit 
            return ans 
        
        seen = set()
        while n not in seen: #n != 1 and 
            seen.add(n)
            n = helper(n)
            
        return n == 1 
    
    
    #take n 
    ## 98 81 + 64 = 145 
    ## 145 1+16+25 = 42
    #count digits square sum of n
    #run that in loop
    #conditions: newN == n: return false
    #if(newN == 1): return true
    #newN: 