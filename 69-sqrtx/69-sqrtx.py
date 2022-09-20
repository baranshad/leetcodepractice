class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x 
        i = 0
        j = x 
        while i <= j:
            mid = i + (j-i)//2 
            temp = mid * mid 
            if temp == x:
                return mid 
            elif temp < x:
                i = mid + 1 
            else:
                j = mid - 1 
                
        return j 