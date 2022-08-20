class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = [-1, 1][(dividend>= 0) == (divisor>=0)]
        ans = 0
        nu = abs(dividend)
        deno = abs(divisor)
        
        while deno <= nu:
            double = 1
            cur_divisor = deno 
            while (cur_divisor <<1) <= nu:
                cur_divisor <<= 1 
                double <<= 1 
            
            nu -= cur_divisor 
            ans += double 
            
        return min(max(-2147483648, ans*sign), 2147483647) 
    
    
    # idea: counting how many doubling divisor we can substract from dividend.
    
    #1: conduct unless shrinking dividend wouldn't be lower than divisor
    
    #2: double probable divisor unless it wouldn't be higher than dividend
    
    #3: decrease dividend, and count how many doubling we had done during this step
    
    # repeat from 1